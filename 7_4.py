import numpy as np
import matplotlib.pyplot as plt


def f(x, y, z):
    return z / (x - 2.0) + 3.0 * y / np.power(x - 2.0, 2)


def rungekutta(x0, y, x, z, h):
    n = int((x - x0) / h)
    Y = [y]*(n+1)
    Z = [z]*(n+1)
    print(f'Значение дифференциального уравнения в точке {x0}:', y)
    for i in range(1, n + 1):
        k1 = h*z
        l1 = h * f(x0, y, z)
        k2 = h * (z + 0.5 * l1)
        l2 = h * f(x0 + 0.5 * h, y + 0.5 * k1, z + 0.5 * l1)
        k3 = h * (z + 0.5 * l2)
        l3 = h * f(x0 + 0.5 * h, y + 0.5 * k2, z + 0.5 * l2)
        k4 = h * (z + l3)
        l4 = h * f(x0 + h, y + k3, z + l3)
        y = y + (1.0 / 6.0) * (k1 + 2.0 * k2 + 2.0 * k3 + k4)
        z = z + (1.0 / 6.0) * (l1 + 2.0 * l2 + 2.0 * l3 + l4)
        x0 = x0 + h
        Y[i] = y
        Z[i] = z
        print(f'Значение дифференциального уравнения в точке {round(x0,3)}:', y)
    return Y


def plot(x, xn, y1, y2, h_1, h_2):
    XNEW1 = np.linspace(x, xn, int((xn - x) / h_1 + 1))
    XNEW2 = np.linspace(x, xn, int((xn - x) / h_2 + 1))
    plt.plot(XNEW1, y1, label='h = 0.1')
    plt.plot(XNEW2, y2, label='h = 0.01')
    plt.title('Метод Рунге-Кутты 4го порядка')
    plt.legend()
    plt.grid(True)
    plt.show()


if __name__ == '__main__':
    y_0 = 2.0
    z_0 = 2.0
    x_0 = 3.0
    b = 4.0
    h1 = 0.1
    h2 = 0.01
    print(f'h = {h1}:')
    res = rungekutta(x_0, y_0, b, z_0, h1)
    print('------------------------------------------------------')
    print(f'h = {h2}:')
    res2 = rungekutta(x_0, y_0, b, z_0, h2)
    plot(x_0, b, res, res2, h1, h2)
