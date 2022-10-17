import numpy as np
import matplotlib.pyplot as plt

t=np.linspace(0,2*np.pi)

plt.plot(t,np.sin(t))

import numpy as np
import matplotlib.pyplot as plt

t=np.linspace(0,2*np.pi)

plt.subplot(221)
plt.xlim((0,2*np.pi))
plt.title('Sen$\pi$')
plt.plot(t,np.sin(t))

plt.subplot(222)
plt.xlim((0,2*np.pi))
plt.title('Sen2$\pi$')
plt.plot(t,np.sin(2*t))

plt.subplot(223)
plt.xlim((0,2*np.pi))
plt.title('Sen3$\pi$')
plt.plot(t,np.sin(3*t))

plt.subplot(224)
plt.xlim((0,2*np.pi))
plt.title('Sen4$\pi$')
plt.plot(t,np.sin(4*t))