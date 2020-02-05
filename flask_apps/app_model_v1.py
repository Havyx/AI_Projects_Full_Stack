from flask import Flask, jsonify, request, render_template
import numpy as np
import pandas as pd
import pickle

app = Flask(__name__)

stores = [
    {
        'name': 'minha loja',
        'items': [
            {
                'name': 'My item',
                'price': 15.99
            },
        ]
    },
]

class SavioLogisticModel():
      
        def __init__(self, model_file):
            with open('model','rb') as model_file:
                self.reg = pickle.load(model_file)
                self.data = None
                
        def load_new_data(self, data_file):
            #df = pd.read_csv(data_file,delimiter=',')
            df = data_file
            self.data = df.copy()
            self.preprocessed_data = df.copy()
            
        def predicted_probability(self):
            if (self.data is not None):  
                pred = self.reg.predict_proba(self.data)
                return pred
            
        def predicted_output_category(self):
            if (self.data is not None):
                pred_outputs = self.reg.predict(self.data)
                return pred_outputs
            
        def predicted_outputs(self):
            if (self.data is not None):
                self.preprocessed_data['Probabilidade'] = 0
                self.preprocessed_data['Predito'] = 0
                self.preprocessed_data['Probabilidade'] = self.reg.predict_proba(self.data)[:,1]
                self.preprocessed_data['Predito'] = self.reg.predict(self.data)
                return self.preprocessed_data


@app.route('/')
def home():
    return render_template('index.html')

# Isso é um servidor backend entao quando recebemos uma requisição do tipo:
# post: estamos recebendo dados.
# get: enviando dados.
# no browser é o contrario.

@app.route('/model', methods=['POST'])  # '/' is homepage da aplicação.
def create_model():
    # get_json converte json para um pyton dictionaty
    request_data = request.get_json()
    df = pd.DataFrame(request_data['payload'])
    print(type(df))
    #model = SavioLogisticModel('model')
    #model.load_new_data(df)
    #model.predicted_probability()[:,1]
    #model.predicted_output_category()
    #res = model.predicted_outputs()
    #df_to_dict_data = res.to_dict(orient='list')
    return jsonify(request_data)

# somente acessivel por um post request.
# POST /store data: {name:}
@app.route('/store', methods=['POST'])  # '/' is homepage da aplicação.
def create_store():
    # get_json converte json para um pyton dictionaty
    request_data = request.get_json()
    new_store = {
        'name': request_data['name'],
        'items': []
    }

    stores.append(new_store)
    return jsonify(new_store)


@app.route('/store/<string:name>')  # http://127:0:0:1:5000/store/some_name
def get_store(name):
    for store in stores:
        if store == name:
            return jsonify(store)
    return jsonify({'message': 'store not found'})


@app.route('/store')
def get_stores():
    return jsonify({'stores': stores})
# transforma dicionario python em json que e uma string


@app.route('/store/<string:name>/item', methods=['POST'])
def create_item_in_store(name):
    request_data = request.get_json()
    for store in stores:
        if store['name'] == name:
            new_item = {
                'name': request_data['name'],
                'price': request_data['price']
            }
            store['items'].append(new_item)
            return jsonify(new_item)
    return jsonify({'message': 'store not found'})


@app.route('/store/<string:name>/item')
def get_items_in_store(name):
    for store in stores:
        if store['name'] == name:
            return jsonify({'items': store['items']})
    return jsonify({'message': 'store not found'})


app.run(port=3000)
