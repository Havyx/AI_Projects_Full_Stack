from flask import Flask, jsonify, request, render_template
import numpy as np
import pandas as pd
import pickle

app = Flask(__name__, static_folder='static')


# class SavioLogisticModel():
      
#         def __init__(self, model_file):
#             with open('model.pkl','rb') as model_file:
#                 self.reg = pickle.load(model_file)
#                 self.data = None
                
#         def load_new_data(self, data_file):
#             #df = pd.read_csv(data_file,delimiter=',')
#             df = data_file
#             self.data = df.copy()
#             self.preprocessed_data = df.copy()
            
#         def predicted_probability(self):
#             if (self.data is not None):  
#                 pred = self.reg.predict_proba(self.data)
#                 return pred
            
#         def predicted_output_category(self):
#             if (self.data is not None):
#                 pred_outputs = self.reg.predict(self.data)
#                 return pred_outputs
            
#         def predicted_outputs(self):
#             if (self.data is not None):
#                 self.preprocessed_data['Probabilidade'] = 0
#                 self.preprocessed_data['Predito'] = 0
#                 self.preprocessed_data['Probabilidade'] = self.reg.predict_proba(self.data)[:,1]
#                 self.preprocessed_data['Predito'] = self.reg.predict(self.data)
#                 return self.preprocessed_data


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
    reg = pickle.load(open('static/model.pkl','rb'))
    data = df.copy()
    preprocessed_data = pd.DataFrame()
    if (data is not None):
        preprocessed_data['Probabilidade'] = 0
        preprocessed_data['Predito'] = 0
        preprocessed_data['Probabilidade'] = reg.predict_proba(data)[:,1]
        preprocessed_data['Predito'] = reg.predict(data)
    #model.load_new_data(df)
    #model.predicted_probability()[:,1]
    #model.predicted_output_category()
    #res = model.predicted_outputs()
    df_to_dict_data = preprocessed_data.to_dict(orient='list')
    return jsonify(df_to_dict_data)

app.run(port=3000)
