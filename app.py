
from flask import Flask, jsonify, request

app = Flask (__name__) # init

stores = [
   {
       "name": "Apple",
       "items": [
           {
               "name": "iphone13",
               "price": 1299.99
           }
       ]
   },
   {
       "name": "Microsoft",
       "items": [
           {
               "name": "SurfacePro",
               "price": 1399.99
           }
       ]
   },
]
    
@app.route('/home')
def home():
    return "Hello World"

@app.route('/stores')
def get_stores():
    return jsonify({'stores' : stores})

@app.route('/stores/<string:name>')
def get_store(name):
    for store in stores:
        if (store['name'] == name):
            return jsonify({"items" : store['items']})
    return jsonify({"Message" : f"{name} not Found!"})

@app.route('/stores/<string:name>/<string:item_name>')
def get_item(name, item_name):
    for store in stores: 
        if name == store['name']:
            for item in store['items']:
                if item['name'] == item_name:
                    return jsonify ({'item':item})
            return jsonify({'Message': f'{item_name} not found!'}) 
    return   jsonify({'Message': f'{name} not found!'})      

@app.route('/new_store', methods=['POST'])
def new_store():
    storeToCreate = request.get_json()
    new_store = {
        "name" : storeToCreate['name'],
        "items" : storeToCreate['items'],
    }
    stores.append(new_store)
    return jsonify(new_store)

@app.route('/stores/<string:store_name>/', methods=['POST'])
def new_item(store_name):
    #check store exist or not
    for store in stores:
        if store['name'] == store_name:
            itemToCreate = request.get_json()
            new_item = {
                'name' : itemToCreate['name'],
                'price' : itemToCreate['price']
            }
            store['items'].append(new_item)
            return jsonify(new_item)
    return jsonify ({'Message': f'{store_name} not found!'})
    # if exist -> add new item
    # pass


app.run()
