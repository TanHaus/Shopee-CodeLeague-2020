# Import data
# test
test = """2
3 6
apple lettuce limes avocado
onion cranberries apple limes
escarole corn28corn apple lettuce limes avocado
limes avocado
apple lettuce
limes
apple
app
apple limes
3 3
apple iphone se 2
iphone 11 max pro
iphone 11 pro max
apple iphone
max pro
iphone"""


class Node(object):
    """A node in the suffix tree.

    suffix_node
        the index of a node with a matching suffix, representing a suffix link.
        -1 indicates this node has no suffix link.
    """

    def __init__(self):
        self.suffix_node = -1

    def __repr__(self):
        return "Node(suffix link: %d)" % self.suffix_node


class Edge(object):
    """An edge in the suffix tree.

    first_char_index
        index of start of string part represented by this edge

    last_char_index
        index of end of string part represented by this edge

    source_node_index
        index of source node of edge

    dest_node_index
        index of destination node of edge
    """

    def __init__(self, first_char_index, last_char_index, source_node_index, dest_node_index):
        self.first_char_index = first_char_index
        self.last_char_index = last_char_index
        self.source_node_index = source_node_index
        self.dest_node_index = dest_node_index

    @property
    def length(self):
        return self.last_char_index - self.first_char_index

    def __repr__(self):
        return 'Edge(%d, %d, %d, %d)' % (self.source_node_index, self.dest_node_index, self.first_char_index, self.last_char_index)


class Suffix(object):
    """Represents a suffix from first_char_index to last_char_index.

    source_node_index
        index of node where this suffix starts

    first_char_index
        index of start of suffix in string

    last_char_index
        index of end of suffix in string
    """

    def __init__(self, source_node_index, first_char_index, last_char_index):
        self.source_node_index = source_node_index
        self.first_char_index = first_char_index
        self.last_char_index = last_char_index

    @property
    def length(self):
        return self.last_char_index - self.first_char_index

    def explicit(self):
        """A suffix is explicit if it ends on a node. first_char_index
        is set greater than last_char_index to indicate this.
        """
        return self.first_char_index > self.last_char_index

    def implicit(self):
        return self.last_char_index >= self.first_char_index


class SuffixTree(object):
    """A suffix tree for string matching. Uses Ukkonen's algorithm
    for construction.
    """

    def __init__(self, string, case_insensitive=False):
        """
        string
            the string for which to construct a suffix tree
        """
        self.string = string
        self.case_insensitive = case_insensitive
        self.N = len(string) - 1
        self.nodes = [Node()]
        self.edges = {}
        self.active = Suffix(0, 0, -1)
        if self.case_insensitive:
            self.string = self.string.lower()
        for i in range(len(string)):
            self._add_prefix(i)

    def __repr__(self):
        """
        Lists edges in the suffix tree
        """
        curr_index = self.N
        s = "\tStart \tEnd \tSuf \tFirst \tLast \tString\n"
        values = list(self.edges.values())
        values.sort(key=lambda x: x.source_node_index)
        for edge in values:
            if edge.source_node_index == -1:
                continue
            s += "\t%s \t%s \t%s \t%s \t%s \t" % (edge.source_node_index, edge.dest_node_index,
                                                  self.nodes[edge.dest_node_index].suffix_node, edge.first_char_index, edge.last_char_index)

            top = min(curr_index, edge.last_char_index)
            s += self.string[edge.first_char_index:top+1] + "\n"
        return s

    def _add_prefix(self, last_char_index):
        """The core construction method.
        """
        last_parent_node = -1
        while True:
            parent_node = self.active.source_node_index
            if self.active.explicit():
                if (self.active.source_node_index, self.string[last_char_index]) in self.edges:
                    # prefix is already in tree
                    break
            else:
                e = self.edges[self.active.source_node_index,
                               self.string[self.active.first_char_index]]
                if self.string[e.first_char_index + self.active.length + 1] == self.string[last_char_index]:
                    # prefix is already in tree
                    break
                parent_node = self._split_edge(e, self.active)

            self.nodes.append(Node())
            e = Edge(last_char_index, self.N, parent_node, len(self.nodes) - 1)
            self._insert_edge(e)

            if last_parent_node > 0:
                self.nodes[last_parent_node].suffix_node = parent_node
            last_parent_node = parent_node

            if self.active.source_node_index == 0:
                self.active.first_char_index += 1
            else:
                self.active.source_node_index = self.nodes[self.active.source_node_index].suffix_node
            self._canonize_suffix(self.active)
        if last_parent_node > 0:
            self.nodes[last_parent_node].suffix_node = parent_node
        self.active.last_char_index += 1
        self._canonize_suffix(self.active)

    def _insert_edge(self, edge):
        self.edges[(edge.source_node_index,
                    self.string[edge.first_char_index])] = edge

    def _remove_edge(self, edge):
        self.edges.pop(
            (edge.source_node_index, self.string[edge.first_char_index]))

    def _split_edge(self, edge, suffix):
        self.nodes.append(Node())
        e = Edge(edge.first_char_index, edge.first_char_index +
                 suffix.length, suffix.source_node_index, len(self.nodes) - 1)
        self._remove_edge(edge)
        self._insert_edge(e)
        # need to add node for each edge
        self.nodes[e.dest_node_index].suffix_node = suffix.source_node_index
        edge.first_char_index += suffix.length + 1
        edge.source_node_index = e.dest_node_index
        self._insert_edge(edge)
        return e.dest_node_index

    def _canonize_suffix(self, suffix):
        """This canonizes the suffix, walking along its suffix string until it
        is explicit or there are no more matched nodes.
        """
        if not suffix.explicit():
            e = self.edges[suffix.source_node_index,
                           self.string[suffix.first_char_index]]
            if e.length <= suffix.length:
                suffix.first_char_index += e.length + 1
                suffix.source_node_index = e.dest_node_index
                self._canonize_suffix(suffix)

    # Public methods

    def find_substring(self, substring):
        """Returns the index of substring in string or -1 if it
        is not found.
        """
        if not substring:
            return -1
        if self.case_insensitive:
            substring = substring.lower()
        curr_node = 0
        i = 0
        while i < len(substring):
            edge = self.edges.get((curr_node, substring[i]))
            if not edge:
                return -1
            ln = min(edge.length + 1, len(substring) - i)
            if substring[i:i + ln] != self.string[edge.first_char_index:edge.first_char_index + ln]:
                return -1
            i += edge.length + 1
            curr_node = edge.dest_node_index
        return edge.first_char_index - len(substring) + ln

    def has_substring(self, substring):
        return self.find_substring(substring) != -1\



class KMP:
    def partial(self, pattern):
        """ Calculate partial match table: String -> [Int]"""
        ret = [0]

        for i in range(1, len(pattern)):
            j = ret[i - 1]
            while j > 0 and pattern[j] != pattern[i]:
                j = ret[j - 1]
            ret.append(j + 1 if pattern[j] == pattern[i] else j)
        return ret

    def search(self, T, P):
        """ 
        KMP search main algorithm: String -> String -> [Int] 
        Return all the matching position of pattern string P in T
        """
        partial, ret, j = self.partial(P), [], 0

        for i in range(len(T)):
            while j > 0 and T[i] != P[j]:
                j = partial[j - 1]
            if T[i] == P[j]:
                j += 1
            if j == len(P):
                ret.append(i - (j - 1))
                j = partial[j - 1]

        return ret


def search(haystack, needle):
    """
    Search list `haystack` for sub-list `needle`.
    """
    if len(needle) == 0:
        return False
    char_table = make_char_table(needle)
    offset_table = make_offset_table(needle)
    i = len(needle) - 1
    while i < len(haystack):
        j = len(needle) - 1
        while needle[j] == haystack[i]:
            if j == 0:
                return True
            i -= 1
            j -= 1
        i += max(offset_table[len(needle) - 1 - j],
                 char_table.get(haystack[i], -1))
    return False


def make_char_table(needle):
    """
    Makes the jump table based on the mismatched character information.
    """
    table = {}
    for i in range(len(needle) - 1):
        table[needle[i]] = len(needle) - 1 - i
    return table


def make_offset_table(needle):
    """
    Makes the jump table based on the scan offset in which mismatch occurs.
    """
    table = []
    last_prefix_position = len(needle)
    for i in reversed(range(len(needle))):
        if is_prefix(needle, i + 1):
            last_prefix_position = i + 1
        table.append(last_prefix_position - i + len(needle) - 1)
    for i in range(len(needle) - 1):
        slen = suffix_length(needle, i)
        table[slen] = len(needle) - 1 - i + slen
    return table


def is_prefix(needle, p):
    """
    Is needle[p:end] a prefix of needle?
    """
    j = 0
    for i in range(p, len(needle)):
        if needle[i] != needle[j]:
            return 0
        j += 1
    return 1


def suffix_length(needle, p):
    """
    Returns the maximum length of the substring ending at p that is a suffix.
    """
    length = 0
    j = len(needle) - 1
    for i in reversed(range(p + 1)):
        if needle[i] == needle[j]:
            length += 1
        else:
            break
        j -= 1
    return length


def run():
    T = int(input())

    for i in range(T):
        # Import data
        N, Q = [int(x) for x in input().split()]

        database = []
        for j in range(N):
            database.append(input().split())
            # database.append('{} '.format(input()))
            # database.append(SuffixTree('{} '.format(input())))
            # database.append(SuffixTree(input().split()))

        queries = []
        for j in range(Q):
            queries.append(input().split())
            # queries.append('{} '.format(input()))

        # Process data
        print('Case {}:'.format(i+1))
        for query in queries:
            # count = [0 for item in database if subfinder(item, query)]
            count = [
                # 0 for item in database if item.has_substring(query)]
                0 for item in database if search(item, query)]
            print(len(count))


run()
