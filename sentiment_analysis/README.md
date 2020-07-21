# Sentiment Analysis

Code for `fastText` (can try play with the parameters. Or even better, write a script to check all different possible combinations and use the parameter combination that gives the highest validation accuracy)

```python
import fasttext

# Train the model
model = fasttext.train_supervised('fasttext.txt', lr=0.001, dim=300, epoch=300, wordNgrams=2)

# Evaluate the model
model.test('fasttext_val.txt')
```

Format for fastText input
```
"But I have put a call saying I'm not hearing it." __label__1
"Excellent product quality, use makeup remover cotton soft, clean skin" __label__5
```