import numpy as np
import matplotlib.pyplot as plt


def f(x, y):
    return -2*y / (np.power(x, 2) + 1.0)


def rungekutta(x0, y, x, z, h):
    n = int((x - x0) / h)
    Y = [y]*(n+1)
    Z = [z]*(n+1)
    #print(f'Значение дифференциального уравнения в точке {x0}:', y)
    for i in range(1, n + 1):
        k1 = h*z
        l1 = h * f(x0, y)
        k2 = h * (z + 0.5 * l1)
        l2 = h * f(x0 + 0.5 * h, y + 0.5 * k1)
        k3 = h * (z + 0.5 * l2)
        l3 = h * f(x0 + 0.5 * h, y + 0.5 * k2)
        k4 = h * (z + l3)
        l4 = h * f(x0 + h, y + k3)
        y = y + (1.0 / 6.0) * (k1 + 2.0 * k2 + 2.0 * k3 + k4)
        z = z + (1.0 / 6.0) * (l1 + 2.0 * l2 + 2.0 * l3 + l4)
        x0 = x0 + h
        Y[i] = y
        Z[i] = z
        #print(f'Значение дифференциального уравнения в точке {round(x0,3)}:', y)
    return Y, Z


def plot(x, xn, y1, y2,_y1, _y2, h_1, h_2):
    XNEW1 = np.linspace(x, xn, int((xn - x) / h_1 + 1))
    XNEW2 = np.linspace(x, xn, int((xn - x) / h_2 + 1))
    plt.plot(XNEW1, y1, label='y(x) при h = 0.1')
    plt.plot(XNEW2, y2, label='y(x) при h = 0.01')
    plt.plot(XNEW1, _y1, label="y'(x) при h = 0.1")
    plt.plot(XNEW2, _y2, label="y'(x) при h = 0.01")
    plt.title('Метод Стрельбы')
    plt.legend()
    plt.grid(True)
    plt.show()


def shouting(_a, _b, x0, y0, x_n, z0, h, eps, _eps):
    res = _res = 0.0
    while (np.fabs(_eps) >= eps):
        res, _res = rungekutta(x0, y0, x_n, z0, h)
        _eps = -res[-1] + _res[-1] + 1.0
        if _eps > 0:
            _a = y0
        else:
            _b = y0
        y0 = 0.5*(_a+_b)   
    return res, _res


if __name__ == '__main__':
    a = 1.0
    b = 20.0
    z_0 = 0.0
    x_0 = 0.0
    xn = 2.0
    h1 = 0.1
    h2 = 0.01
    eps = 0.01
    epsilon = 1.0
    print(f'h = {h1}:')
    c = 0.5*(a + b)
    ans, _ans = shouting(a, b, x_0, c, xn, z_0, h1, eps, epsilon)
    print(f'h = {h2}:')
    ans2, _ans2 = shouting(a, b, x_0, c, xn, z_0, h2, eps, epsilon)
    plot(x_0, xn, ans, ans2,_ans, _ans2, h1, h2)
