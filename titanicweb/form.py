from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    errors = []
    results = {}
    if request.method == "POST":
        # get url that the user has entered
        try:
            age = int(request.form['age'])
            print(age)
            print(type(age))
            gender = str(request.form['gender'])
            print(gender)
            print(type(gender))
            embarked = str(request.form['embarked'])
            print(embarked)
            print(type(embarked))

            json = [
                {"Age": age, "Sex": gender, "Embarked": embarked},
                
            ]
            r = requests.post("http://0.0.0.0:5000/predict", json=json)
            print(r.text)

            data = r.json()
            print(data)
            pred = data['prediction']

            
            survive = int(pred[1])
            print(survive)
            if survive == 0:
                results = "You would have died!"
            elif survive == 1:
                results = "Congrats, you have survived!"
            print(results)
        except:
            errors.append(
                "Unable to reach API. Please make sure it's running and try again."
            )
    return render_template('index.html', errors=errors, results=results)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, debug=True)