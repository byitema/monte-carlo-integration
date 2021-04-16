import math
import random
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
import numpy as np
import threading


def function_1(x):
    return math.tan(1 / x) / (math.pow(x, 2) + x - 3)


def function_2(x, y):
    return (x + 4) / (math.pow(x, 2) + math.pow(y, 4) + 1)


def monte_carlo_integrate_1d(function, a, b, n):
    result = 0
    for _ in range(n):
        result += function(random.uniform(a, b))
    
    return result * (b - a) / float(n)


def monte_carlo_integrate_2d(function, a, b, c, d, n):
    count = 0
    result = 0
    z_limit = 15000
    for _ in range(n):
        x = random.uniform(a, b)
        y = random.uniform(c, d)
        z = random.uniform(0, z_limit)
        if z <= function_2(x, y):
        	count += 1

    V = (b - a) * (d - c) * z_limit

    return count * V / n


def draw3D():
	f = lambda x,y: (x + 4) / (x**2) + y**4 + 1

	fig = plt.figure(figsize=(12, 6))

	ax = fig.add_subplot(1, 2, 1, projection='3d')

	xvalues = np.linspace(-2,2,100)
	yvalues = np.linspace(-2,2,100)
	xgrid, ygrid = np.meshgrid(xvalues, yvalues)
	zvalues = f(xgrid, ygrid)

	surf = ax.plot_surface(xgrid, ygrid, zvalues, rstride=5, cstride=5, linewidth=0, cmap=cm.plasma)

	ax = fig.add_subplot(1,2,2)

	plt.contourf(xgrid, ygrid, zvalues, 30,	cmap=cm.plasma)

	fig.colorbar(surf, aspect=18)

	plt.tight_layout()
	plt.show()


def draw2D():
	xvalues = np.linspace(-10, 10, num=1000)
	ys = []
	for x in xvalues:
		ys.append(function_1(x))
	yvalues1 = np.array(ys)

	plt.plot(xvalues, yvalues1, lw=2, color='red', label='tg(1/x)/(x^2 + x - 3)')
	
	plt.xlabel('x')
	plt.ylabel('y')

	plt.axhline(0, lw=0.5, color='black')
	plt.axvline(0, lw=0.5, color='black')

	plt.legend()
	plt.show()


if __name__ == '__main__':
    draw2D()
    draw3D()

    print('Calculated integral: ', end='')
    print(monte_carlo_integrate_1d(function_1, 2, 1000, 1000000))
    print('Expected result: 0.1383644781770419')
    print('Calculated integral: ', end='')
    print(monte_carlo_integrate_2d(function_2, -3, 4, -4, 3, 1000000))
    print('Expected result: 28.2765010231188')

    ns = []
    results = []
    for n in range(1, 1000000, 50000):
        if n != 0:
            ns.append(n)
            results.append(monte_carlo_integrate_1d(function_1, 2, 1000, n))

    plt.plot(ns, results)
    plt.axhline(y = 0.1383644781770419, color = 'r', linestyle = 'dashed')
    plt.ylabel('value')
    plt.xlabel('n')
    plt.show()

    ns = []
    results = []
    for n in range(1, 1000000, 50000):
        if n != 0:
            ns.append(n)
            results.append(monte_carlo_integrate_2d(function_2, -3, 4, -4, 3, n))

    plt.plot(ns, results)
    plt.axhline(y = 28.2765010231188, color = 'r', linestyle = 'dashed')
    plt.ylabel('value')
    plt.xlabel('n')
    plt.show()
