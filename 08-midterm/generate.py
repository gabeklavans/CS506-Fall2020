import pandas as pd

trainingSet = pd.read_csv("08-midterm/data/train.csv")
testingSet = pd.read_csv("08-midterm/data/test.csv")

predictionSet = pd.merge(trainingSet, testingSet, left_on='Id', right_on='Id')
print(predictionSet.columns)

predictionSet = predictionSet.drop(columns=['Score_x'])
predictionSet = predictionSet.rename(columns={'Score_y': 'Score'})

print(predictionSet.columns)
predictionSet.to_csv("08-midterm/data/prediction.csv", index=False)

X_train = trainingSet[trainingSet['Score'].notnull()]
print(trainingSet.shape)
print(X_train.shape)
X_train.to_csv("08-midterm/data/X_train.csv", index=False)
