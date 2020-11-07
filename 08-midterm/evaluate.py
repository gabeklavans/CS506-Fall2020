import pandas as pd
from sklearn.metrics import mean_squared_error

y_predict = pd.read_csv("08-midterm/data/submission_offline.csv")
train = pd.read_csv("08-midterm/data/X_train.csv")

y_id = y_predict.drop(columns=['Score'])
y_true = pd.merge(train, y_id, left_on='Id', right_on='Id')

y_predict = y_predict['Score']
y_true = y_true['Score']

print(y_predict.shape)
print(y_true.shape)

rmse = mean_squared_error(y_true, y_predict, squared=False)

print(rmse)