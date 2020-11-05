import matplotlib
import matplotlib.pyplot as plt
import numpy as np

# data for plotting
#t = np.arange(0.0, 2.0, 0.01)
t = np.arange(0.0, 8.0, 0.01)
#s = 1 + np.sin(2 * np.pi * t)
s = np.cos(3.14/2 * t**2)
fig, ax = plt.subplots()
ax.plot(t, s)

ax.set(xlabel = 'time(s)', ylabel = 'volatage(mV)',
       title = 'About as simple as it gets, folks')
ax.grid()

#fig.savefig("test.png")
fig.savefig("t_cos.png")
plt.show()