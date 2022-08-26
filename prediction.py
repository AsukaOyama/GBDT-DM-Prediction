import pickle
import pandas as pd 

# model
model_file = "MODEL/model.pkl"
with open(model_file, 'rb') as f:
    model = pickle.load(f)

# data
data_file = "DATA/test.csv"
data = pd.read_csv(data_file)

# prediction
pred = model.predict(data)
print(pred)