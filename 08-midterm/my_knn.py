import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import OneHotEncoder
from sklearn.model_selection import train_test_split

X = pd.read_csv("08-midterm/data/X_train.csv")
Y = pd.DataFrame(X['Score'])
X = X.drop(columns=['Score'])
x_train, x_test, y_train, y_test = train_test_split(X, Y, test_size=0.1)
x_train = pd.DataFrame(x_train)
x_test = pd.DataFrame(x_test)
y_train = pd.DataFrame(y_train)
y_test = pd.DataFrame(y_test)

x_train_features = x_train.drop(columns=['Id', 'UserId', 'Text', 'Summary'])
x_test_features = x_test.drop(columns=['Id', 'UserId', 'Text', 'Summary'])

predictionSet = pd.read_csv("08-midterm/data/prediction.csv")
x_predict = predictionSet.drop(columns=['Id', 'UserId', 'Text', 'Summary', 'Score'])

le = LabelEncoder()
x_train_features['ProductId'] = le.fit_transform(pd.DataFrame(x_train_features['ProductId']))
x_test_features['ProductId'] = le.fit_transform(pd.DataFrame(x_test_features['ProductId']))
x_predict['ProductId'] = le.fit_transform(pd.DataFrame(x_predict['ProductId']))

model = KNeighborsClassifier(n_neighbors=4).fit(x_train_features, y_train.values.flatten())
predictionSet['Score'] = model.predict(x_predict)
x_test['Score'] = model.predict(x_test_features)
x_test = x_test.sort_values(by=['Id'])
print(x_test)

submission = predictionSet[['Id', 'Score']]
submission_offline = x_test[['Id', 'Score']]
print(submission.head())
submission.to_csv("08-midterm/data/submission.csv", index=False)
submission_offline.to_csv("08-midterm/data/submission_offline.csv", index=False)
