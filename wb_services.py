from flask import Flask, request, jsonify, abort, redirect, url_for, render_template
import joblib
import numpy as np
from sklearn.neighbors import KNeighborsClassifier
import pandas as pd

app = Flask(__name__)

knn = joblib.load('model.pkl')

@app.route('/iris/<param>')
def iris(param):
    param = list(map(float,param.split(',')))
    param = np.array(param).reshape(1, -1)
    predict = knn.predict(param)
    return str(predict)

@app.route('/badrequest400')
def bad_request():
    return abort(400)

@app.route('/api', methods=['POST'])
def api_post():

    try:
        content = request.get_json()
        print(content)
        
        sepal_length  = list(map(float,list(content["sepal_length"])))
        sepal_width  = list(map(float,list(content["sepal_width"])))
        petal_length  = list(map(float,list(content["petal_length"])))
        petal_width  = list(map(float,list(content["petal_width"])))
        param = np.array(list(zip(sepal_length, sepal_width, petal_length, petal_width)))

        predict = knn.predict(param)

        predict = {'class': list(map(str,list(predict)))}

        return jsonify(predict)
    except:
        return redirect(url_for('bad_request'))

from flask_wtf import FlaskForm
from wtforms import StringField, FloatField
from wtforms.validators import DataRequired, NumberRange

app.config.update(dict(
    SECRET_KEY="powerful secretkey",
    WTF_CSRF_SECRET_KEY="a csrf secret key"
))

class MyForm(FlaskForm):
    sepal_length = FloatField('Длина чашелистика (см)', 
        validators=[NumberRange(min=0.1, max=50, message='Длина чашелистика от 0.1 до 50 см')])
    sepal_width = FloatField('Ширина чашелистика (см)', 
        validators=[NumberRange(min=0.1, max=50, message='Ширина чашелистика от 0.1 до 50 см')])
    petal_length = FloatField('Длина лепестка (см)', 
        validators=[NumberRange(min=0.1, max=50, message='Длина лепестка от 0.1 до 50 см')])
    petal_width = FloatField('Ширина лепестка (см)', 
        validators=[NumberRange(min=0.1, max=50, message='Ширина лепестка от 0.1 до 50 см')])
    name=""
    photo=""

from werkzeug.utils import secure_filename
import os

@app.route('/form', methods=['GET', 'POST'])
def form_predict():
    form = MyForm()
    if form.validate_on_submit():
        df = np.array([form.sepal_length.data, form.sepal_width.data,
                       form.petal_length.data, form.petal_width.data]).reshape(1, -1)

        predict = knn.predict(df)

        if predict[0] == 0:
            form.name="Iris setose"
            form.photo="static/Irissetosa.jpg"
        elif predict[0] == 1:
            form.name="Iris virginica"
            form.photo="static/Irisvirginica.jpg"
        elif predict[0] == 2:
            form.name="Iris versicolor"
            form.photo="static/Irisversicolor.jpg"
        else:
            form.name=""
            form.photo=""

    return render_template('submit.html', form=form)