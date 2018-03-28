from flask import Flask, jsonify, request

app = Flask(__name__)

users = [{"email":"isainsrd@example.com", "firstName":"Inness","lastName":"Sains","gender":"Male"},
{"email":"nlimeburnre@example.com", "firstName":"Norris","lastName":"Limeburn","gender":"Male"},
{"email":"rdimmackrf@example.com", "firstName":"Ruthie","lastName":"Dimmack","gender":"Female"},
{"email":"kkarpfenrg@example.com", "firstName":"Kerri","lastName":"Karpfen","gender":"Female"},
{"email":"sbowditchrh@example.com", "firstName":"Sayre","lastName":"Bowditch","gender":"Male"},
{"email":"gparissri@example.com", "firstName":"Gaston","lastName":"Pariss","gender":"Male"},
{"email":"rverryrj@example.com", "firstName":"Robbert","lastName":"Verry","gender":"Male"},
{"email":"brubertirk@example.com", "firstName":"Bekki","lastName":"Ruberti","gender":"Female"},
{"email":"msilburnrl@example.com", "firstName":"Margret","lastName":"Silburn","gender":"Female"},
{"email":"ralbonerm@example.com", "firstName":"Ryon","lastName":"Albone","gender":"Male"},
{"email":"mgarriquern@example.com", "firstName":"Manny","lastName":"Garrique","gender":"Male"},
{"email":"dgrishaninro@example.com", "firstName":"Drusi","lastName":"Grishanin","gender":"Female"},
{"email":"bbrushneenrp@example.com", "firstName":"Bent","lastName":"Brushneen","gender":"Male"},
{"email":"akiosselrq@example.com", "firstName":"Adriaens","lastName":"Kiossel","gender":"Female"},
{"email":"gabbetsrr@example.com", "firstName":"Grenville","lastName":"Abbets","gender":"Male"}]

airports = [
    {
        "code": "AAM",
        "name": "Mala Mala",
        "stateCode": "",
        "city": "Mala Mala",
        "countryCode": "ZA",
        "countryName": "South Africa",
        "latitude": -3.140277777777778,
        "longitude": 28.24277777777778,
        "admiralsClubUrl": ""
    },
    {
        "code": "AAN",
        "name": "Al Ain",
        "stateCode": "",
        "city": "Al Ain",
        "countryCode": "AE",
        "countryName": "United Arab Emirates",
        "latitude": 2.033333333333333,
        "longitude": 55.266666666666666,
        "admiralsClubUrl": ""
    },
    {
        "code": "AAQ",
        "name": "Anapa",
        "stateCode": "",
        "city": "Anapa",
        "countryCode": "RU",
        "countryName": "Russia",
        "latitude": 45.001666666666665,
        "longitude": 37.348333333333336,
        "admiralsClubUrl": ""
    },
    {
        "code": "AAR",
        "name": "Aarhus Tirstrup",
        "stateCode": "",
        "city": "Aarhus",
        "countryCode": "DK",
        "countryName": "Denmark",
        "latitude": 56.300555555555555,
        "longitude": 10.620277777777778,
        "admiralsClubUrl": ""
    },
    {
        "code": "AAT",
        "name": "Altay",
        "stateCode": "",
        "city": "Altay",
        "countryCode": "CN",
        "countryName": "China",
        "latitude": 47.75,
        "longitude": 87.75,
        "admiralsClubUrl": ""
    },
    {
        "code": "AAX",
        "name": "Araxa",
        "stateCode": "MG",
        "city": "Araxa",
        "countryCode": "BR",
        "countryName": "Brazil",
        "latitude": -19.568055555555556,
        "longitude": -46.92916666666667,
        "admiralsClubUrl": ""
    }]

@app.route('/users')
def get_users():
	return jsonify({'users': users})

@app.route('/airports')
def get_airports():
	return jsonify({'airports': airports})	

app.run(port=5000)