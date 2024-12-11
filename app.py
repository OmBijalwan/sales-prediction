from flask import Flask, jsonify, render_template, request
import joblib
import numpy as np

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("home.html")


@app.route('/predict', methods=['POST', 'GET'])
def result():
    item_weight = float(request.form['item_weight'])
    item_fat_content = float(request.form['item_fat_content'])
    item_visibility = float(request.form['item_visibility'])
    item_type = float(request.form['item_type'])
    item_mrp = float(request.form['item_mrp'])
    outlet_establishment_year = float(request.form['outlet_establishment_year'])
    outlet_size = float(request.form['outlet_size'])
    outlet_location_type = float(request.form['outlet_location_type'])
    outlet_type = float(request.form['outlet_type'])

    X = np.array([[item_weight, item_fat_content, item_visibility, item_type, item_mrp, outlet_establishment_year,
                   outlet_size, outlet_location_type, outlet_type]])

    #scaler_path = r'C:\Users\ACER\Desktop\python\models\sc.sav'

    #scaler_path = r'E:\python\models\sc.sav'

    scaler_path = './models/sc.sav'

    sc = joblib.load(scaler_path)

    X_std = sc.transform(X)

    # model_path = r'C:\Users\ACER\Desktop\python\models\rf.sav'

    # model_path = r'E:\python\models\rf.sav'

    model_path = './models/rf.sav'

    model = joblib.load(model_path)

    Y_pred = model.predict(X_std)

    prediction = f"The predicted success rate is {round(float(Y_pred[0]), 2)}%"

    # Rendering result.html
    return render_template('result.html', prediction=prediction)

if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host='0.0.0.0', port=port)

