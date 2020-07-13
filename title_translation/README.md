# Title Translation

Dataset: https://drive.google.com/drive/folders/1M1xMwlp1kPkpPkcQA4JLbwu0r87U6B8s?usp=sharing

Command to run MUSE

```python
python unsupervised.py --src_lang en --tgt_lang zh --src_emb ../en_vect.bin --tgt_emb ../tcn_vect.bin --n_refinement 5 --normalize_embeddings center --emb_dim 300 --dis_most_frequent 20000
```

## Machine Translation Datasets

Parallel datasets for supervised learning

Name | Link
-----|------
Opus (parallel datasets) | http://opus.nlpl.eu/
WMT19 | http://www.statmt.org/wmt19/

## Tools

Libraries in TensorFlow

Name | Link | What
-----|------|------
Nematus | https://github.com/EdinburghNLP/nematus | Attention-based encoder-decoder model for neural machine translation built in Tensorflow 
OpenNMT-tf | https://github.com/OpenNMT/OpenNMT-tf | neural machine translation and neural sequence learning
Jieba tokenizer | https://github.com/fxsjy/jieba | Tokenizer for Traditional Chinese
Moses tokenizer (Python) | https://github.com/alvations/sacremoses| Tokenizer for English


## Learning

Free online resources to learn about NLP

Name | Link
-----|-------
Stanford CS224n | http://web.stanford.edu/class/cs224n/
(Jay Alammar) Illustrated Transformer | http://jalammar.github.io/illustrated-transformer/

## Papers

State-of-the-art research on Machine Translaion

Name | Link
-----|-------
Facebook MUSE | https://github.com/facebookresearch/MUSE 
Word Translation Without Parallel Data | https://arxiv.org/abs/1710.04087
Unsupervised Machine Translation Using Monolingual Corpora Only | https://arxiv.org/abs/1711.00043
