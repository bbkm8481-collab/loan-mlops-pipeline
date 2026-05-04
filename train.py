# train.py
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import mlflow
import mlflow.sklearn
from database import engine

def load_data():
    # Updated to point exactly to your schema and table
    query = "SELECT * FROM datasets.loan" 
    df = pd.read_sql(query, engine)
    return df
def train_model():
    print("Loading data from PostgreSQL...")
    df = load_data()
   # Drop both 'status' (our target) and 'id' (useless for training)
    X = df.drop(columns=['status', 'id'])
    y = df['status']
    
    X = pd.get_dummies(X)    
# ... rest of your code ...
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    mlflow.set_experiment("Loan_Risk_Prediction")
    
    with mlflow.start_run():
        print("Training Random Forest Model...")
        n_estimators = 100
        max_depth = 5
        
        mlflow.log_param("n_estimators", n_estimators)
        mlflow.log_param("max_depth", max_depth)

        model = RandomForestClassifier(n_estimators=n_estimators, max_depth=max_depth, random_state=42)
        model.fit(X_train, y_train)

        # Evaluate model
        predictions = model.predict(X_test)
        accuracy = accuracy_score(y_test, predictions)
        
        print(f"Model Accuracy: {accuracy * 100:.2f}%")
        
        # Log metrics and model to MLflow
        mlflow.log_metric("accuracy", accuracy)
        mlflow.sklearn.log_model(model, "random_forest_model")
        
        print("Model training complete and logged to MLflow!")

if __name__ == "__main__":
    train_model()
