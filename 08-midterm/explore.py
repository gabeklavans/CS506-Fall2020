import pandas as pd

trainingSet = pd.read_csv("08-midterm/data/train.csv")
testingSet = pd.read_csv("08-midterm/data/test.csv")

print("train.csv shape is ", trainingSet.shape)
print("test.csv shape is ", testingSet.shape)

print()

print(trainingSet.head())
print()
print(testingSet.head())

print()

print(trainingSet.describe())
