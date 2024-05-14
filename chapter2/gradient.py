weight = 0.5
goal_pred = 0.8
input = 2
alpha = 0.1  # альфа коэффициент, позволяет избежать сильных отклонений при большом input


def make_prediction(weight, input):
    for iteration in range(20):
        pred = input * weight
        error = (pred - goal_pred) ** 2
        derivative = input * (pred - goal_pred)  # производная; зависимость чистой ошибки от переменной input
        weight = weight - (alpha * derivative)

        print(f'Error: {str(error)}. Prediction: {str(pred)}')


make_prediction(weight, input)
