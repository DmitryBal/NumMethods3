import numpy as np
from matplotlib import pyplot as plt


def f(x, y):
    return np.power(x, 2)*(np.power(y, 2) + 1.0)


def eiler(x, x_n, y, h):
    n = int((x_n - x)/h)
    Y = np.zeros(n+1)
    Y_2 = np.array([y]*(n+1))
    X = np.zeros(n+1)
    for i in range(n):
        Y[i+1] = Y[i] + h*f(x, Y[i])
        Y_2[i+1] = Y[i] + 0.5*h*(f(x, Y[i]) + f(x+h, Y[i+1]))
        x += h
        X[i+1] = x
    return X, Y, Y_2


def plot(x, y1, y2, title, label_1, label_2):
    plt.plot(x, y1, label=label_1)
    plt.plot(x, y2, label=label_2)
    plt.title(title)
    plt.legend()
    plt.grid(True)
    plt.show()


if __name__ == '__main__':
    x0 = 0.0
    xn = 1.0
    y0 = 0.0
    h1 = 0.1
    h2 = 0.01
    arr, res, res2 = eiler(x0, xn, y0, h1)
    text = 'h = 0.1'
    label1 = 'Метод Эйлера'
    label2 = 'Метод Эйлера с пересчетом'
    print(text)
    print(label1)
    print(res, '\n')
    print(label2)
    print(res2, '\n')
    plot(arr, res, res2, text, label1, label2)
    print('---------------------------')
    text = 'h = 0.01'
    arr, res, res2 = eiler(x0, xn, y0, h2)
    label1 = 'Метод Эйлера'
    label2 = 'Метод Эйлера с пересчетом'
    print(text)
    print(label1)
    print(res, '\n')
    print(label2)
    print(res2, '\n')
    plot(arr, res, res2, text, label1, label2)
