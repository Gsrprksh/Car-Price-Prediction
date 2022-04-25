from flask import Flask, request,render_template
import pickle

import numpy as np

app = Flask(__name__)
model = pickle.load(open('pickle (1).sav','rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods = ['POST','GET'])
def predict():
    list = [float(i) for i in request.form.values()]
    array = [np.array(list)]
    predict = model.predict(array)[0]
    return render_template('index.html', result = predict)

if __name__ == '__main__':
    app.run(debug = True)