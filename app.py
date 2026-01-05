from flask import Flask, request, jsonify
import pickle
import numpy as np

app = Flask(__name__)

clf = pickle.load(open("classification_model.pkl", "rb"))
reg = pickle.load(open("regression_model.pkl", "rb"))

@app.route("/predict", methods=["POST"])
def predict():
    data = request.json
    features = np.array([[ 
        data["study_time"],
        data["sleep_hours"],
        data["attendance"]
    ]])

    performance = clf.predict(features)[0]
    score = reg.predict(features)[0]

    return jsonify({
        "predicted_score": float(score),
        "performance_level": int(performance)
    })

if __name__ == "__main__":
    app.run()
