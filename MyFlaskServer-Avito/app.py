# Import necessary modules
from flask import Flask, jsonify
from pymongo import MongoClient
from flask_cors import CORS 

app = Flask(__name__)
CORS(app) 

# Connect to MongoDB
client = MongoClient('mongodb://localhost:27017/')
db = client['MyVisualizations']

from bson import ObjectId 

@app.route('/api/visualization1')
def get_visualization1_data():
    collection1 = db['professional_publication_data']
    data_from_mongo = list(collection1.find())
    for item in data_from_mongo:
        item['_id'] = str(item['_id'])
    return jsonify(data_from_mongo)


@app.route('/api/visualization2')
def get_visualization2_data():
    collection2 = db['products_category_data']
    data_from_mongo = list(collection2.find())
    for item in data_from_mongo:
        item['_id'] = str(item['_id'])
    return jsonify(data_from_mongo)

@app.route('/api/visualization3')
def get_visualization3_data():
    collection3 = db['product_regions_data']
    data_from_mongo = list(collection3.find())
    for item in data_from_mongo:
        item['_id'] = str(item['_id'])
    return jsonify(data_from_mongo)

@app.route('/api/visualization4')
def get_visualization4_data():
    collection4 = db['product_citys_data']
    data_from_mongo = list(collection4.find())
    for item in data_from_mongo:
        item['_id'] = str(item['_id'])
    return jsonify(data_from_mongo)

@app.route('/api/visualization5')
def get_visualization5_data():
    collection5 = db['casablanca_prices_data']
    data_from_mongo = list(collection5.find())
    for item in data_from_mongo:
        item['_id'] = str(item['_id'])
    return jsonify(data_from_mongo)

@app.route('/api/visualization6')
def get_visualization6_data():
    collection6 = db['casablanca_stripplot_data']
    data_from_mongo = list(collection6.find())
    for item in data_from_mongo:
        item['_id'] = str(item['_id'])
    return jsonify(data_from_mongo)

@app.route('/api/visualization7')
def get_visualization7_data():
    collection7 = db['top_10_phones_casablanca_data']
    data_from_mongo = list(collection7.find())
    for item in data_from_mongo:
        item['_id'] = str(item['_id'])
    return jsonify(data_from_mongo)

@app.route('/api/visualization8')
def get_visualization8_data():
    collection8 = db['active_phone_data']
    data_from_mongo = list(collection8.find())
    for item in data_from_mongo:
        item['_id'] = str(item['_id'])
    return jsonify(data_from_mongo)

@app.route('/api/visualization9')
def get_visualization9_data():
    collection9 = db['active_phone_prices_data']
    data_from_mongo = list(collection9.find())
    for item in data_from_mongo:
        item['_id'] = str(item['_id'])
    return jsonify(data_from_mongo)

@app.route('/api/visualization10')
def get_visualization10_data():
    collection10 = db['rabat_stripplot_data']
    data_from_mongo = list(collection10.find())
    for item in data_from_mongo:
        item['_id'] = str(item['_id'])
    return jsonify(data_from_mongo)

@app.route('/api/visualization11')
def get_visualization11_data():
    collection11 = db['top_10_phones_rabat_data']
    data_from_mongo = list(collection11.find())
    for item in data_from_mongo:
        item['_id'] = str(item['_id'])
    return jsonify(data_from_mongo)

@app.route('/api/visualization12')
def get_visualization12_data():
    collection12 = db['active_phone_categories_rabat_data']
    data_from_mongo = list(collection12.find())
    for item in data_from_mongo:
        item['_id'] = str(item['_id'])
    return jsonify(data_from_mongo)

@app.route('/api/visualization13')
def get_visualization13_data():
    collection13 = db['active_phone_prices_rabat_data']
    data_from_mongo = list(collection13.find())
    for item in data_from_mongo:
        item['_id'] = str(item['_id'])
    return jsonify(data_from_mongo)

@app.route('/api/visualization14')
def get_visualization14_data():
    collection14 = db['active_phone_prices_casablanca_data']
    data_from_mongo = list(collection14.find())
    for item in data_from_mongo:
        item['_id'] = str(item['_id'])
    return jsonify(data_from_mongo)

@app.route('/api/visualization15')
def get_visualization15_data():
    collection15 = db['active_phone_categories_casablanca_data']
    data_from_mongo = list(collection15.find())
    for item in data_from_mongo:
        item['_id'] = str(item['_id'])
    return jsonify(data_from_mongo)

@app.route('/api/visualization16')
def get_visualization16_data():
    collection16 = db['rabat_stripplot_data']
    data_from_mongo = list(collection16.find())
    for item in data_from_mongo:
        item['_id'] = str(item['_id'])
    return jsonify(data_from_mongo)


@app.route('/api/visualization18')
def get_visualization18_data():
    collection_Info = db['Info']
    data_from_mongo = list(collection_Info.find())
    for item in data_from_mongo:
        item['_id'] = str(item['_id'])
    return jsonify(data_from_mongo)


if __name__ == '__main__':
    app.run(debug=True)
