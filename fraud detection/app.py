import joblib
from flask import Flask, render_template, request

app = Flask(__name__)

model = joblib.load('model.pkl')
le = joblib.load('encoder.pkl')

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/predict', methods=['POST'])
def predict():
    step = int(request.form['step'])
    type_val = request.form['type']
    amount = float(request.form['amount'])
    oldbalanceOrg = float(request.form['oldbalanceOrg'])
    newbalanceOrig = float(request.form['newbalanceOrig'])
    oldbalanceDest = float(request.form['oldbalanceDest'])
    newbalanceDest = float(request.form['newbalanceDest'])

    type_encoded = le.transform([type_val])[0]

    new_data = [[step, type_encoded, amount,
                 oldbalanceOrg, newbalanceOrig,
                 oldbalanceDest, newbalanceDest]]

    pred = model.predict(new_data)

    result = "Fraud Transaction" if pred[0] == 1 else "Not a Fraud Transaction "

    return render_template("index.html", prediction_text=result)

# if __name__ == '__main__':
#     app.run(debug=True)

