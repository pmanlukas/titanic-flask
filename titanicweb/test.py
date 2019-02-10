import requests

json = [
    {"Age": 85, "Sex": "male", "Embarked": "S"},
    {"Age": 24, "Sex": "female", "Embarked": "C"},
    {"Age": 3, "Sex": "male", "Embarked": "C"},
    {"Age": 21, "Sex": "male", "Embarked": "S"}
]

r = requests.post("http://0.0.0.0:5000/predict", json=json)

print(r.text)
data = r.json()
print(data)