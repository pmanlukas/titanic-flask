from flask import Flask, jsonify, request
from sklearn.externals import joblib
from sklearn.linear_model import LogisticRegression
import pandas as pd
import traceback


app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def predict():
    if model:
        try:
            json_ = request.json
            print(json_)
            query = preprocess_input(json_)

            prediction = model_pred(query)
            print("prediction: {}".format(prediction))
            return jsonify({'prediction': str(prediction)})
            
    
        except:
        
            return jsonify({'trace': traceback.format_exc()})
    else:
        print('Train a model first')
        return 'no model to use'

@app.route('/train', methods=['GET'])
def train():
    try:
        model = train_model(dataframe=load_process_data())
        print("trained model")
        return jsonify({'success': "trained model!"}) 
    except:
        return jsonify({'trace': traceback.format_exc()})

@app.route('/healthz', methods=['GET'])
def healt_check():
    return "api is running"

def load_process_data():
    #import dataset
    url = "http://s3.amazonaws.com/assets.datacamp.com/course/Kaggle/train.csv"
    df = pd.read_csv(url)
    cols = ['Age','Sex','Embarked','Survived']
    df_ = df[cols]
    
    categoricals = []

    for col, col_type in df_.dtypes.iteritems():
        if col_type == 'O':
            categoricals.append(col)
        else:
            df_[col].fillna(0, inplace=True)

    #one hot encode the data
    df_ohe = pd.get_dummies(df_,columns=categoricals, dummy_na=True)

    return df_ohe

def train_model(dataframe):
    dependent_var = 'Survived'

    X = dataframe[dataframe.columns.difference([dependent_var])]
    Y = dataframe[dependent_var]
    clf = LogisticRegression()

    clf.fit(X,Y)
    return clf

def preprocess_input(json):
    query = pd.get_dummies(pd.DataFrame(json))
    query = query.reindex(columns=model_columns, fill_value=0)
    return query

def model_pred(query):
    prediction = list(model.predict(query))
    return prediction

if __name__ == "__main__":
    try:
        port = int(sys.argv[1])
    except:
        port = 5000
    global model
    model = joblib.load('model.pkl')
    print("Model loaded!")
    model_columns = joblib.load('model_cols.pkl')
    print("Model columns loaded!")
    app.run(host='0.0.0.0', port=port, debug=True)