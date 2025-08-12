import requests

# Example car specs
car = {
    "cylinders": 4,
    "displacement": 135.0,
    "horsepower": 84.0,
    "weight": 2064.0,
    "acceleration": 15.5,
    "model_year": 82,
    "origin": 1
}

url = 'http://localhost:9696/predict'
response = requests.post(url, json=car)

print("Prediction response:", response.json())
