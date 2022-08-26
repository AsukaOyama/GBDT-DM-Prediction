# Code repository of the paper "Gradient Boosting Decision Tree Becomes More Reliable Than Logistic Regression in Predicting Probability for Diabetes With Big Data" (Seto et al. 2022) 

# Code requirements
The code was run using Python. The code require the installation of the following packages:

- Pickle
- Pandas
- LightGBM (https://lightgbm.readthedocs.io/en/latest/)

# Dataset
Put the CSV file you want to predict in the DATA folder (test.csv is already included).

- Data Description

|Name|Details|
|---|---|
|age| |
|sex|1: Women, 0: Men|
|bmi| |
|shuushuku_ketsuatsu| Systolic blood pressure|
|Chuusei_shibou| Triglyceride cholosterol|
|hdl_cholesterol| |
|ldl_cholesterol| |
|gpt| Alanine aminotransferase|
|hba1c| Glycated hemoglobin A1c|
|nyoutampaku| Urinary protein, 1: positive, 0: negative|
|kitsuen| Smoking|
|fukuyaku_ketsuatsu| Anti hypertension|
|fukuyaku_shishitsu| Anti dyslipidemia|
|kioureki_noukekkan| Medical history of Stroke|
|kioureki_shinkekkan| Medical history of Heart disease|
|kioureki_jinfuzen_jinkoutouseki| Medical HIstory of Renal failure|

# Running
```
$ Python prediction.py
```
