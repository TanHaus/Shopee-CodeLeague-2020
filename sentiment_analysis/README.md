# Sentiment Analysis

Code for `fastText`

```python
import fasttext

# Train the model
model = fasttext.train_supervised('fasttext.txt', dim=50, epoch=25, wordNgrams=3)

# Evaluate the model
model.test('fasttext_val.txt')
```

Format for fastText input
```
"But I have put a call saying I'm not hearing it." __label__1
"Excellent product quality, use makeup remover cotton soft, clean skin" __label__5
```