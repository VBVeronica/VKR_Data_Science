from flask import Flask, request, render_template
import numpy as np
import tensorflow as tf
print("Версия TensorFlow:", tf.__version__)

app = Flask(__name__)

def nn_prediction(params):
    model = tf.keras.models.load_model('models/nn_model')
    y_pred = model.predict(params)
    return y_pred

@app.route('/')
def index():
    return "main"

@app.route('/predict/', methods=['post', 'get'])
def processing():
    message = ''
    if request.method == 'POST':
        mat_dens = request.form.get('Плотность')

        elast_mod = request.form.get('Модуль упругости')

        cur_agnt = request.form.get('Количество отвердителя')

        epox_gr = request.form.get('Содержание эпоксидных групп')

        flash_point = request.form.get('Температура вспышки')

        surf_dens = request.form.get('Поверхностная плотность')

        elast_mod_tens = request.form.get('Модуль упругости при растяжении')

        tensile = request.form.get('Прочность при растяжении')

        resin = request.form.get('Потребление смолы')

        patch_angle = request.form.get('Угол нашивки')

        patch_step = request.form.get('Шаг нашивки')

        patch_dens = request.form.get('Плотность нашивки')

        params = [mat_dens, elast_mod, cur_agnt, epox_gr, flash_point, surf_dens, elast_mod_tens, tensile, resin, patch_angle, patch_step, patch_dens]
        params = [float(i) for i in params]

        message = f'Рекомендуемое соотношение матрица-наполнитель: {nn_prediction(params)}'
    return render_template('Prediction_nn.html', message=message)


if __name__ == '__main__':
    app.run()
