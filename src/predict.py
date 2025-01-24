import pickle

# Load the saved model
with open("model.pkl", "rb") as file:
    model = pickle.load(file)

# Example input
X_new = [[1.5]]

# Make a prediction
y_pred = model.predict(X_new)
print(f"Prediction for {X_new}: {y_pred}")