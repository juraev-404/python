import matplotlib.pyplot as plt
import numpy as np

# колокол

x = [i for i in np.arange(-5, 5.1, 0.1)]
x1 = [i for i in np.arange(5, 8.1, 0.1)]
x2 = [i for i in np.arange(-5, -8.1, -0.1)]
x3 = [i for i in np.arange(-8, 8.1, 0.1)]
x4 = [8, 8]
x5 = [-8, -8]
x6 = [i for i in np.arange(-8, 8.1, 0.1)]
x7 = [i for i in np.arange(-2, 2.1, 0.1)]
y = [(-2*(i**2))/25+12 for i in x]
y1 = [10/(i-4) for i in x1]
y2 = [-10/(i+4) for i in x2]
y3 = [(3*(i**2))/128+1 for i in x3]
y4 = [1, 2.5]
y5 = [1, 2.5]
y6 = [(3*(i**2))/128-0.5 for i in x6]
y7 = [0.5*(i**2)-2.5 for i in x7]
plt.plot(x, y, 'black')
plt.plot(x1, y1, 'black')
plt.plot(x2, y2, 'black')
plt.plot(x3, y3, 'black')
plt.plot(x4, y4, 'black')
plt.plot(x5, y5, 'black')
plt.plot(x6, y6, 'black')
plt.plot(x7, y7, 'black')
plt.grid()
plt.xlabel('Ось x')
plt.ylabel('Ось y')
plt.title('График')
plt.grid()

# шахматная фигура

x = [12, 12, 12.5, 13, 13.2, 13.5, 13, 12.5, 16.5, 16, 15.5, 15.8, 16, 16.5, 17, 17, -13, 22]
y = [12, 13.5, 13.5, 14.5, 14.5, 23.5, 23.5, 25, 25, 23.5, 23.5, 14.5, 14.5, 13.5, 13.5, 12, 12, 12]
x1 = [14, 13.5, 14.5, 15.5, 15]
y1 = [25, 25.5, 27.5, 25.5, 25]
x2 = [12.5, 16.5]
y2 = [13.5, 13.5]
x3 = [13, 16]
y3 = [14.5, 14.5]
x4 = [13.5, 15.5]
y4 = [23.5, 23.5]
plt.plot(x1, y1, 'black')
plt.plot(x2, y2, 'black')
plt.plot(x3, y3, 'black')
plt.plot(x4, y4, 'black')
plt.plot(x, y, 'black')
plt.grid()
plt.xlabel('Ось x')
plt.ylabel('Ось y')
plt.title('График')
plt.show()

