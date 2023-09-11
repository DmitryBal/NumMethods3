import numpy as np
import matplotlib.pyplot as plt


def f(x, y):
    return (np.power(x, 2)*np.log(x) - y) / x


def adams(x0, xn, y0, h):
    n = int((xn - x0) / h)
    x = np.linspace(x0, xn, n+1)
    y = np.zeros(n+1)
    y[0] = y0

    for i in range(3):
        k1 = h * f(x[i], y[i])
        k2 = h * f(x[i] + 0.5 * h, y[i] + 0.5 * k1)
        k3 = h * f(x[i] + 0.5 * h, y[i] + 0.5 * k2)
        k4 = h * f(x[i] + h, y[i] + k3)
        y[i+1] = y[i] + (1.0 / 6.0) * (k1 + 2.0 * k2 + 2.0 * k3 + k4)

    for i in range(3, n):
        y[i + 1] = y[i] + h * (55.0 * f(x[i], y[i]) - 59.0 * f(x[i - 1], y[i - 1]) + 37.0 * f(x[i - 2], y[i - 2]) -
                               9.0 * f(x[i - 3], y[i - 3])) / 24.0

    return y


def plot(x, xn, y1, y2, h_1, h_2):
    x_new1 = np.linspace(x, xn, int((xn - x) / h_1 + 1))
    x_new2 = np.linspace(x, xn, int((xn - x) / h_2 + 1))
    plt.plot(x_new1, y1, label='h = 0.1')
    plt.plot(x_new2, y2, label='h = 0.01')
    plt.title('Метод Адамса')
    plt.legend()
    plt.grid(True)
    plt.show()


if __name__ == '__main__':
    y_0 = 0.5
    x_0 = 1.0
    b = 2.0
    h1 = 0.1
    h2 = 0.01
    res = adams(x_0, b, y_0, h1)
    print(f'h = {h1}:')
    print(res)
    print('------------------------------------------------------')
    print(f'h = {h2}:')
    res2 = adams(x_0, b, y_0, h2)
    print(res2)
    plot(x_0, b, res, res2, h1, h2)

