# Marketing Analytics

Kaggle Competition page: https://www.kaggle.com/c/student-shopee-code-league-sentiment-analysis

Final submission is based on 4 models:
- Random Forest (from `sklearn`)
- Gradient Boosting (from `sklearn`)
- XGBoost
- CatBoost

XGBoost and CatBoost can be installed with `pip`

```
pip install xgboost
pip install catboost
```

Probability output across models are averaged, and using decision threshold of `0.5` to convert to `0` and `1` prediction.

Notebook [explore.ipynb](explore.ipynb) performs data cleaning and basic analysis of the data.

Notebook [training.ipynb](training.ipynb) does the main training and output logic. 