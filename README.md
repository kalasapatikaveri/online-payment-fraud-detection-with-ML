💳 Online Payment Fraud Detection System

A Machine Learning based web application that detects whether an online transaction is fraudulent or legitimate.
Built using Python, Flask, Scikit-learn, and HTML/CSS.

________________________________
📌 Project Overview

Online payment fraud is increasing rapidly. Traditional rule-based systems fail to detect complex fraud patterns.
This project uses a trained Machine Learning model to predict whether a transaction is:

•	✅ Not a Fraud Transaction

•	❌ Fraud Transaction

The system takes transaction details as input and provides instant prediction through a web interface.

________________________________________

🚀 Features

•	Web-based UI for entering transaction details
•	Real-time fraud prediction
•	Label Encoding for categorical variables
•	ML model integration using joblib
•	Error handling & input validation
•	Easy deployment on cloud platforms

________________________________________

🛠️ Tech Stack

•	Backend: Python, Flask
•	Machine Learning: Scikit-learn
•	Frontend: HTML, CSS
•	Model Storage: joblib (.pkl files)

________________________________________
________________________________________

⚙️ Installation & Setup

1️⃣ Clone the Repository

git clone https://github.com/kalasapatikaveri/online-payment-fraud-detection-with-ML.git
cd fraud-detection

2️⃣ Install Dependencies

pip install flask scikit-learn joblib numpy pandas

3️⃣ Run the Application

python app.py
Open browser and go to:
http://127.0.0.1:5000/

🧠 How It Works

User enters transaction details:

Step

Type

Amount

Old Balance (Sender)

New Balance (Sender)

Old Balance (Receiver)

New Balance (Receiver)

Transaction type is encoded using encoder.pkl.

Data is passed to trained ML model (model.pkl).

Model predicts:

1 → Fraud Transaction

0 → Not a Fraud Transaction

Result is displayed on the webpage.

