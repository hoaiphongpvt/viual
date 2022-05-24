import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0, 5 * np.pi , 0.01)

y = np.cos(x)

z = np.sin(x)

plt.plot(x, y)
plt.plot(x, z)

plt.xlabel('X')
plt.ylabel('Y')

plt.title('Ham Cosine va Sine trong khoan  0 den 5pi')
plt.legend(['Cos(x)', 'Sin(x)'])


plt.show()



