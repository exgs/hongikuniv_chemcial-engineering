import math
from matplotlib import pyplot as plt
import numpy as np

#그래프를 넣을 도화지 생성
fig, ax = plt.subplots(2,2, figsize=(8,8))
fig.suptitle('problem 1.5')
#(a)
x_range = np.linspace(0, 1, 20)
y_range = list(map(lambda x : 1 - math.exp(x) + (math.e-1)*math.sin(math.pi*x/2), x_range))
ax[0][0].plot(x_range, y_range)
ax[0][0].plot(x_range, [0]*20, c='red')
ax[0][0].set_title('(a)')

#(b)
x_range = np.linspace(0, 1, 20)
y_range = list(map(lambda x : (x-1)*math.tan(x) + x*math.sin(math.pi*x) , x_range))
ax[0][1].plot(x_range, y_range)
ax[0][1].plot(x_range, [0]*20, c='red')
ax[0][1].set_title('(b)')

#(c)
x_range = np.linspace(1, 2, 20)
y_range = list(map(lambda x : x*math.sin(math.pi*x) - (x-2)*math.log(x) , x_range))
ax[1][0].plot(x_range, y_range)
ax[1][0].plot(x_range, [0]*20, c='red')
ax[1][0].set_title('(c)')

#(d)
x_range = np.linspace(-1, 3, 20)
y_range = list(map(lambda x : (x-2)*math.log(x+2)*math.sin(x), x_range))
ax[1][1].plot(x_range, y_range)
ax[1][1].plot(x_range, [0]*20, c='red')
ax[1][1].set_title('(d)')

fig.set_dpi(100)
plt.show()