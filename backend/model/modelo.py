import numpy as np
import pickle


class Model:

    def carrega_modelo(path):
        """Dependendo se o final for .pkl ou .joblib, carregamos de uma forma ou de outra
        """
        model = pickle.load(open(path, 'rb'))
        return model

    def preditor(model, form):
        """Realiza a predição de um paciente com base no modelo treinado
        """
        X_input = np.array([
            form.radius_mean, form.texture_mean, form.perimeter_mean, form.area_mean,
            form.smoothness_mean, form.compactness_mean, form.concavity_mean, form.concave_points_mean,
            form.symmetry_mean, form.fractal_dimension_mean, form.radius_se, form.texture_se,
            form.perimeter_se, form.area_se, form.smoothness_se, form.compactness_se,
            form.concavity_se, form.concave_points_se, form.symmetry_se, form.fractal_dimension_se,
            form.radius_worst, form.texture_worst, form.perimeter_worst, form.area_worst,
            form.smoothness_worst, form.compactness_worst, form.concavity_worst, form.concave_points_worst,
            form.symmetry_worst, form.fractal_dimension_worst
        ])

        # Faremos o reshape para que o modelo entenda que estamos passando
        diagnosis = model.predict(X_input.reshape(1, -1))
        print(f'Este é o diagnóstico: {diagnosis[0]}')
        return int(diagnosis[0])
