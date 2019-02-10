import pandas as pd 
import numpy as np 

#import dataset
url = "http://s3.amazonaws.com/assets.datacamp.com/course/Kaggle/train.csv"
df = pd.read_csv(url)
cols = ['Age','Sex','Embarked','Survived']
df_ = df[cols]

#preprocess data
categoricals = []

for col, col_type in df_.dtypes.iteritems():
    if col_type == 'O':
        categoricals.append(col)
    else:
        df_[col].fillna(0, inplace=True)

#one hot encode the data
df_ohe = pd.get_dummies(df_,columns=categoricals, dummy_na=True)

#train the model
from sklearn.linear_model import LogisticRegression

dependent_var = 'Survived'

X = df_ohe[df_ohe.columns.difference([dependent_var])]
Y = df_ohe[dependent_var]
clf = LogisticRegression()

clf.fit(X,Y)

#export the model
from sklearn.externals import joblib
joblib.dump(clf, 'model.pkl')

model_cols = list(X.columns)
joblib.dump(model_cols, 'model_cols.pkl')


