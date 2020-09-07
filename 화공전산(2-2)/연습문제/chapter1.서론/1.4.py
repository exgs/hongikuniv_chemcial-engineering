import math
from matplotlib import pyplot as plt
import numpy as np

#그래프를 넣을 도화지 생성
fig, ax = plt.subplots(2,2, figsize=(8,8))
fig.suptitle('problem 1.4')
#(a)
x_range = np.linspace(0.2, 0.4, 20)
y_range = list(map(lambda x : x * math.cos(x) - 2*x**2 + 3*x -1 , x_range))
ax[0][0].plot(x_range, y_range)
ax[0][0].plot(x_range, [0]*20, c='red')
ax[0][0].set_title('(a)')

#(b)
x_range = np.linspace(1, 2, 20)
y_range = list(map(lambda x : (x-2)**2 - math.log(x) , x_range))
ax[0][1].plot(x_range, y_range)
ax[0][1].plot(x_range, [0]*20, c='red')
ax[0][1].set_title('(b)')

#(c)
x_range = np.linspace(2, 3, 20)
y_range = list(map(lambda x : 2*x*math.cos(2*x) - (x-2)**2 , x_range))
ax[1][0].plot(x_range, y_range)
ax[1][0].plot(x_range, [0]*20, c='red')
ax[1][0].set_title('(c)')

#(d)
x_range = np.linspace(4, 5, 20)
y_range = list(map(lambda x : x - (math.log(x)**x), x_range))
ax[1][1].plot(x_range, y_range)
ax[1][1].plot(x_range, [0]*20, c='red')
ax[1][1].set_title('(d)')

fig.set_dpi(100)
plt.show()