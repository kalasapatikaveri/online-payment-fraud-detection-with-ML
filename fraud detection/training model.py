import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import joblib

data = pd.read_csv('data.csv')
data = data.dropna()

data = data.sample(200000, random_state=42)

le = LabelEncoder()
data['type'] = le.fit_transform(data['type'])

X = data[['step', 'type', 'amount',
          'oldbalanceOrg', 'newbalanceOrig',
          'oldbalanceDest', 'newbalanceDest']]
y = data['isFraud']

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

model = RandomForestClassifier(
    n_estimators=100,
    class_weight='balanced',
    random_state=42,
    n_jobs=-1
)

model.fit(X_train, y_train)


joblib.dump(model, 'model.pkl')
joblib.dump(le, 'encoder.pkl')

print("Model trained ")
