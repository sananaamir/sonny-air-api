import json
import sqlite3
from flask import Flask, jsonify, request, g

app = Flask(__name__)

conn = sqlite3.connect('SONNY_AIR_DB.db')
c = conn.cursor()

def get_users_file():
    data = []
    with open('users.json') as json_data:
        data = json.load(json_data)

    return data

def get_airports_file():
    data = []
    with open('airports.json') as json_data:
        data = json.load(json_data)

    return data

def create_user_data():
    users = get_users_file()

    #Create table
    c.execute('CREATE TABLE IF NOT EXISTS users (email TEXT, firstName TEXT, lastName TEXT, gender TEXT)')

    for user in users:
        c.execute("INSERT INTO users (email, firstName, lastName, gender) VALUES(?,?,?,?)", (user['email'], user['firstName'], user['lastName'], user['gender']))
    conn.commit()

def create_airport_data():
    airports = get_airports_file()

    #Create table
    c.execute('CREATE TABLE IF NOT EXISTS airports (code TEXT, name TEXT, stateCode TEXT, city TEXT, countryCode TEXT, countryName TEXT, latitude REAL, longitude REAL, admiralsClubUrl TEXT)')

    for airport in airports:
        c.execute("INSERT INTO airports (code, name, stateCode, city, countryCode, countryName, latitude, longitude, admiralsClubUrl) VALUES(?,?,?,?,?,?,?,?,?)", (airport['code'], airport['name'], airport['stateCode'], airport['city'], airport['countryCode'], airport['countryName'], airport['latitude'], airport['longitude'], airport['admiralsClubUrl']))
    conn.commit()


create_user_data()
create_airport_data()


@app.route('/users')
def get_users():
    c.execute("SELECT * FROM users")
    users = c.fetchall()

    return jsonify({'users': users})

@app.route('/users-file')
def get_users_from_file():
    users = get_users_file()
    return jsonify({'users': users})


@app.route('/airports')
def get_airports():
    c.execute("SELECT * FROM airports")
    airports = c.fetchall()

    return jsonify({'airports': airports})

@app.route('/airports-file')
def get_airports_from_file():
    airports = get_airports_file()
    return jsonify({'airports': airports})

app.run()