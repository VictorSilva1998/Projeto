import pandas as pd

df = pd.read_csv("https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv")
df.set_index ("PassengerId", inplace= True)
df.head (12)
print (df.head(10))
print (df.tail(10))
print (df.info())