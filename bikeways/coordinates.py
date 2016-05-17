import os
import json
import psycopg2
import urllib.parse


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
db = os.path.join(BASE_DIR,'db.sqlite3')


def connectDB(tableName):

    urllib.parse.uses_netloc.append('postgres')
    url = urllib.parse.urlparse('postgres://yccapuatcylbhs:yN4k4RVMIBiQfWwLamKfBiyZ_C@ec2-107-21-221-107.compute-1.amazonaws.com:5432/d8v71h5394a9ht')

    conn = psycopg2.connect(
    database=url.path[1:],
    user=url.username,
    password=url.password,
    host=url.hostname,
    port=url.port
    )

    c = conn.cursor()
    c.execute(tableName)
    rows = c.fetchall()
    c.close()
    conn.close()
    return rows


def getCoordsWithID():
    rows = connectDB('SELECT * FROM bikeways_coordinatewithid')
    coordinates = []
    for row in rows:
        coordinates.append({'key': row[1], 'lat': row[2], 'lng': row[3]})
    return json.dumps(coordinates)