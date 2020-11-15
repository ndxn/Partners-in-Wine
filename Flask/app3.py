import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle

app = Flask(__name__)
model_red = pickle.load(open(model_red.pkl, 'rb'))
scaler_red = pickle.load(open(scaler_red.pkl, 'rb'))
one_hot_red = pickle.load(open(one_hot_red.pkl, 'rb'))
model_white = pickle.load(open(model_white.pkl, 'rb'))
scaler_white = pickle.load(open(scaler_white.pkl, 'rb'))
one_hot_white = pickle.load(open(one_hot_white.pkl, 'rb'))

soil_df: pd.DataFrame = pd.read_csv('soil.csv')
weather_df: pd.DataFrame = pd.read_csv('weather.csv')


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    color = request.form["Color"]
    vintage = request.form["1992-2016"]
    appellation = request.form["Appellation"]

    feature = [Vintage, Appellation]
    feature = [np.array(features)]

    if color == "Red Wine":
        weather_inputs = weather.loc[(weather['year'] == vintage) & (weather["appellation"] == appellation)]
        soil_params = soil_df.loc[(soil_df['appellation'] == appellation)].values.tolist()[0][1:]
        weather_params = weather_df.loc[(weather_df['year'] == year) & (weather_df['appellation'] == appellation)].values.tolist()[0][2:]
        
        
        prediction = Red_model.predict(features)
        output = prediction[0]
    else:
        prediction = White_model.predict(features)
        output = prediction[0]

    if output == 1:
        result = "Good"
    else:
        result = "Bad"


    return render_template('index.html', prediction_text='This wine is a good wine{}'.format(output))

# @app.route('/predict_api',methods=['POST'])
# def predict_api():
#     '''
#     For direct API calls trought request
#     '''
#     data = request.get_json(force=True)
#     prediction = Red_model.predict([np.array(list(data.values()))])

#     output = prediction[0]
#     return jsonify(output)

if __name__ == "__main__":
    app.run(debug=True)