from flask import Flask, request
from sklearn.externals import joblib
import numpy as np

app = Flask(__name__)

GPA_model = joblib.load('lm4.pkl')

@app.route('/')
def home():
    return 'GPA Prediction for Students'

@app.route('/predict')
def predict():
    # Get values from browser
    c1 = request.args['Core_1']
    c2 = request.args['Core_2']
    c3 = request.args['Core_3']
    pe1 = request.args['Prg_Elec_1']
    l3 = request.args['Lab_3']
        
    print(sepal_length)

    test_inp = np.array([c1, c2, c3, pe1, l3]).reshape(1, 5)
    gpa_predicted = int(GPA_model.predict(test_inp)[0])
    output = "Predicted GPA: " + str(gpa_predicted)

    return (output)
if __name__ == '__main__':
    #app.debug = True
    app.run()
