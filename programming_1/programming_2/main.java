import java.util.Scanner; 

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int testInt = sc.nextInt();

        for (int i = 0; i < testInt; i++) {
            System.out.println("Hello!!");
        }
        sc.close();
    }
}
