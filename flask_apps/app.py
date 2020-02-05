from flask import Flask, jsonify, request, render_template

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


@app.route('/')
def home():
    return render_template('index.html')

# Isso é um servidor backend entao quando recebemos uma requisição do tipo:
# post: estamos recebendo dados.
# get: enviando dados.
# no browser é o contrario.

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
