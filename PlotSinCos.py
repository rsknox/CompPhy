# plot sine and cosine frrom -pi to +pi
import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots()
x = np.arange(-np.pi, np.pi, np.pi/100.0)
line1, = ax.plot(x, np.sin(x), 'b-', label = 'sine')
line2, =  ax.plot(x, np.cos(x), 'g--', label = 'cosine')
ax.set(xlabel = 'xvalue', ylabel = 'trig function value',
       title = 'Multiple Plots')
ax.grid()
#ax.legend(loc = 'upper left')
ax.legend(loc = 'lower right')
plt.show()