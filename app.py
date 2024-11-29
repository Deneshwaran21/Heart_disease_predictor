from flask import Flask, render_template, request
import joblib
import numpy as np

app = Flask(__name__)

# Load the pre-trained model
model = joblib.load('heart_disease_model.pkl')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Extract data from form
        features = [float(request.form[field]) for field in [
            'age', 'sex', 'cp', 'trestbps', 'chol', 'fbs', 'restecg', 
            'thalach', 'exang', 'oldpeak', 'slope', 'ca', 'thal'
        ]]
        
        # Make prediction using the model
        prediction = model.predict([features])
        
        # Interpret prediction
        result = "No Heart Disease" if prediction[0] == 0 else "Heart Disease Detected"
        
        # Return the result to result.html
        return render_template('result.html', prediction=result)

    except Exception as e:
        return str(e)

if __name__ == "__main__":
    app.run(debug=True)

