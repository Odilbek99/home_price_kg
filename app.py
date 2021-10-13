import flask
import pandas as pd
from joblib import dump, load


with open(f"model/model.joblib", 'rb') as f:
    model = load(f)


app = flask.Flask(__name__, template_folder='templates')


@app.route('/', methods=['GET', 'POST'])
def main():
    if flask.request.method == 'GET':
        return (flask.render_template('index.html'))

    if flask.request.method == 'POST':
        address = flask.request.form['Адрес']
        mkr = flask.request.form['Микрорайон']
        area_m2 = flask.request.form['Площадь м2']
        n_room = flask.request.form['Количество комнат']
        condition = flask.request.form['Состояние']
        n_floor = flask.request.form['Этажность']
        floor = flask.request.form['Этаж']
        material = flask.request.form['Материал']
        heating = flask.request.form['Отопление']
        year = flask.request.form['ГОД']
        furniture = flask.request.form['Мебель']
        

        input_variables = pd.DataFrame([[address, mkr, area_m2, n_room, condition, n_floor, floor, material, heating, year,furniture]],
                                       columns=['Адрес','Микрорайон','Площадь м2','Количество комнат', 'Состояние','Этажность','Этаж','Материал', 'Отопление',
                                                'ГОД','Мебель'],
                                       dtype='float',
                                       index=['input'])

        predictions = model.predict(input_variables)[0]
        print(predictions)

        return flask.render_template('index.html', original_input={'Адрес': address,'Микрорайон': mkr, 'Площадь м2': area_m2, 'Количество комнат': n_room, 'Состояние': condition,'Этажность': n_floor,'Этаж': floor,'Материал': material, 'Отопление': heating,'ГОД': year, 'Мебель': furniture},
                                     result=predictions)

@app.route('/about/')
def about():
    return flask.render_template('about.html')

@app.route('/contacts/')
def contacts():
    return flask.render_template('contact.html')


if __name__ == '__main__':
    app.run(debug=True)
