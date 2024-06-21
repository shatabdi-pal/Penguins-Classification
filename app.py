import numpy as np
from flask import Flask, render_template, request
import pickle

app = Flask(__name__)
model = pickle.load(open('rf_model.pkl', 'rb'))

# Mapping for categorical features
sex_mapping = {'male': 0, 'female': 1}

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    features = request.form
    sex = sex_mapping.get(features['sex'])
    bill_length_mm = float(features['bill_length_mm'])
    bill_depth_mm = float(features['bill_depth_mm'])
    flipper_length_mm = float(features['flipper_length_mm'])
    body_mass_g = float(features['body_mass_g'])
    
    # Ensure the order of features matches the training data
    final_features = np.array([[bill_length_mm, bill_depth_mm, flipper_length_mm, body_mass_g, sex]])
    
    prediction = model.predict(final_features)
    output = prediction[0]
    
    return render_template('index.html', prediction_text=f'Penguin species is {output}')

if __name__ == "__main__":
    app.run(debug=True)
