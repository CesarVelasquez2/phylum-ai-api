from flask import Flask, jsonify, request
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.tree import DecisionTreeClassifier, plot_tree
from flask_cors import CORS

app = Flask(__name__)

""" @app.route("/", methods=["GET"])
def root():
    return jsonify({"message": "Hello World!"}) """

CORS(app, resources={r"/*": {"origins": "*"}})
def ia(data_answers):
  real_data = [
  [1,0,0,0,0,0,0], 
  [1,2,0,1,0,2,0],
  [2,1,0,0,0,0,0],
  [2,2,1,0,0,0,0],
  [2,2,2,0,1,0,0],
  [2,2,2,0,2,0,0],
  [2,2,3,1,1,0,0],
  [2,2,3,1,2,0,0],
  [2,2,3,2,1,0,0],
  [2,2,3,2,2,0,0],
  [2,2,3,3,0,1,0],
  [2,3,3,3,0,2,1],
  [2,3,3,3,0,2,2],
  [2,3,3,3,0,2,3],
  ]
    
  target=[
    'Protozoarios',
    'Protozoarios',
    'Poriferos',
    'Equinodermos',
    'Ctnoforos',
    'Cnidarios',
    'Nemertinos',
    'Platermintos',
    'Acantocefalos',
    'Asquelmintos',
    'Cordados', 
    'Moluscos',
    'Anelidos',
    'Artoprodos'
  ]
  
  # # Create the example dataset
  data = {'Feature': np.array(real_data), 'Target': target}
  feature_array = data['Feature']
  feature1 = feature_array[:, 0]
  feature2 = feature_array[:, 1]

  # Crear el DataFrame con las columnas separadas
  new_data = {'Feature1': feature1, 'Feature2': feature2, 'Target': data['Target']}
  df = pd.DataFrame(new_data)


  x = df[['Feature1', 'Feature2']]
  y = df['Target']
  # Fit a Decision Tree Classifier
  tree_classifier = DecisionTreeClassifier(random_state=2)
  # tree_classifier = DecisionTreeClassifier(random_state=42)

  tree_classifier.fit(real_data, target)
  #data_answers = [1,0,0,0,0,0,0]
  resultado = tree_classifier.predict([data_answers])
  convertido = np.ndarray.tolist(resultado)
  
  return convertido
  
    
@app.route("/answers", methods=["POST"])
def get_answers():
  data_answers = request.get_json()
    
  resultado = ia(data_answers)

  return jsonify(resultado[0]), 200
    

if __name__ == "__main__":
    app.run(debug=True)
    
""" @app.route("/answers", methods=["GET"])
def get_answers():
  data_answers = request.get_json()
    
  resultado = ia(data_answers)

  return jsonify(resultado[0]), 200
    

if __name__ == "__main__":
    app.run(debug=True) """
    

""" const data = {
  array: [1, 2, 3, 4, 5]
};

fetch('http://localhost:5000/process_array', {
  method: 'POST',
  headers: {
    'Content-Type': 'application/json',
  },
  body: JSON.stringify(data),
})
.then(response => response.json())
.then(result => {
  console.log(result);
})
.catch((error) => {
  console.error('Error:', error);
}); """