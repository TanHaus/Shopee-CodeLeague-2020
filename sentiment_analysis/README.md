# Sentiment Analysis

Kaggle competition page: https://www.kaggle.com/c/student-shopee-code-league-sentiment-analysis

## Dataset

Dataset can be downloaded from the Kaggle competition page. A zip file is also included in this repo `student-shopee-code-league-sentiment-analysis.zip`

# Solutions

Approach | Description | Comment
---------|-------------|---------
FastText |Run supervised word embedding learning with FastText|Simple and very fast to run and train, but performance is not good, prone to overfitting
NNLM from TensorFlow Hub|Use a pre-trained NNLM embedding layer from TensorFlow Hub to build a neural network classifier|Performance is the best out of three approaches. Training time is pretty fast
BERT fine-tuning|Use BERT from Hugging Face to train a classifier|Performance is slightly worse than NNLM embedding in TensorFlow. Training time is quite long

## FastText

Notebook: [fasttext.ipynb](fasttext.ipynb)

Based on Official FastText Tutorial: https://fasttext.cc/docs/en/supervised-tutorial.html

Use [cleaning.ipynb](cleaning.ipynb) to clean the dataset. See below for more information.

Use Moses Tokenizer from `sacremoses` package to tokenize the review. This is to not use the default white space tokenizer provided by FastText. Data is also prepared for FastText input format.

```
"But I have put a call saying I'm not hearing it." __label__1
"Excellent product quality, use makeup remover cotton soft, clean skin" __label__5
```

Model training was done in IPython shell because FastText output during training is not shown inside Jupyter Notebook.

```python
import fasttext

model = fasttext.train_supervised('train_fasttext.csv', dim=300, wordNgrams=3)
model.test('val_fasttext.csv')
model.save_model('fasttext.bin')
```

The notebook also includes code to perform interference on the test set.

## NNLM from TensorFlow Hub

Notebook: [tensorflow.ipynb](tensorflow.ipynb)

Based on Official TensorFlow Text Classification Tutorial: https://www.tensorflow.org/tutorials/keras/text_classification_with_hub

Use [cleaning.ipynb](cleaning.ipynb) to generate cleaned datasets for this approach. The notebook will generate the following 3 datasets:
- `test_clean.csv`: cleaned test set from the competition `test.csv`
- `val_clean.csv`: cleaned train set from the competition `train.csv` and sample `1000` examples from each class
- `train_clean.csv`: the rest of the clean trained set

Cleaning strategy:
- Normalize to lowercase
- Remove hyperlinks, hashtags (with regex)
- Remove or replace some punctuations (with regex)
- Remove some common repeated words (with regex)
- Remove stopwords (from `nltk.corpus.stopwords`)
- Remove emojis except the first two, and convert them to text (with regex and `emoji` library)

A pre-trained NNLM embedding layer is imported from TensorFlow Hub. A dense layer and a classification layer was appended to form a Sequential model. The NNLM embedding layer was set trainable `trainable=True`

Adam optimizer was used, with learning rate `0.001` and train for 1 epoch. It seems to be the fastest way while achieving reasonable accuracy.

Code for generating test set submission was also included in the notebook.

See [tensorflow.ipynb](tensorflow.ipynb) for more details.

## BERT fine-tuning

Notebook: [bert.ipynb](bert.ipynb)

Based on BERT Fine-tuning notebook by Chris McCormick and Nick Ryan: https://colab.research.google.com/drive/1pTuQhug6Dhl9XalKB0zUGf4FIdYFlpcX

Use [bert_data_clearning.ipynb](bert_data_cleaning.ipynb) to clean data for this approach. It follows the exact same steps and strategy as the above approach, but does not remove stopwords. This is because BERT requires stopwords to understand meaning from the sentences.
- `test_bert.csv`
- `val_bert.csv`
- `train_bert.csv`

With Hugging Face library `transformers`, BERT Tokenizer and BERT Classifier are imported. BERT Tokenizer tokenizes the reviews and prepare it in the right format for the pre-trained BERT model.

Reviews are truncated to 64 tokens `max_length=64`. Although there are a few samples with more than 64 tokens, 64 was chosen to have a reasonable training time.

The model was trained with Adam optimizer for 1 epoch.

Code for generating test set submission was also included in the notebook.

See [bert.ipynb](bert.ipynb) for more details.