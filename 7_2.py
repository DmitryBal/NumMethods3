import numpy as np
import matplotlib.pyplot as plt


def f(x, y):
    return y / x + np.power(x, 2)*np.sin(x)


def rungekutta(x0, y, x, h):
    n = int((x - x0) / h)
    Y = [y]*(n+1)
    print(f'Значение дифференциального уравнения в точке {x0}:', y)
    for i in range(1, n + 1):
        k1 = h * f(x0, y)
        k2 = h * f(x0 + 0.5 * h, y + 0.5 * k1)
        k3 = h * f(x0 + 0.5 * h, y + 0.5 * k2)
        k4 = h * f(x0 + h, y + k3)
        y = y + (1.0 / 6.0) * (k1 + 2.0 * k2 + 2.0 * k3 + k4)
        x0 = x0 + h
        Y[i] = y
        print(f'Значение дифференциального уравнения в точке {round(x0,3)}:', y)
    return Y


def plot(x, xn, y1, y2,y3, h_1, h_2, h_3):
    XNEW1 = np.linspace(x, xn, int((xn - x) / h_1 + 1))
    XNEW2 = np.linspace(x, xn, int((xn - x) / h_2 + 1))
    XNEW3 = np.linspace(x, xn, int((xn - x) / h_3 + 1))
    plt.plot(XNEW1, y1, label='h = 0.1')
    plt.plot(XNEW2, y2, label='h = 0.01')
    plt.plot(XNEW3, y3, label='h = 0.25')
    plt.title('Метод Рунге-Кутты 4го порядка')
    plt.legend()
    plt.grid(True)
    plt.show()


if __name__ == '__main__':
    y_0 = 1.3011687
    x_0 = 1.0
    b = 2.0
    h1 = 0.1
    h2 = 0.01
    h3 =0.25
    print(f'h = {h1}:')
    res = rungekutta(x_0, y_0, b, h1)
    print('------------------------------------------------------')
    print(f'h = {h2}:')
    res2 = rungekutta(x_0, y_0, b, h2)
    print('------------------------------------------------------')
    print(f'h = {h3}:')
    res3 = rungekutta(x_0, y_0, b, h3)
    plot(x_0, b, res, res2,res3, h1, h2, h3)
