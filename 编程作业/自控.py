import control as ctr
import matplotlib.pyplot as plt
import numpy as np

Ka = 40
G = ctr.tf([5000], [1, 1020, 20000, 0])
sys = ctr.feedback(Ka * G, 1)
T = np.arange(0, 3, 0.01)
t1, y1 = ctr.step_response(sys, T)
plt.plot(t1, y1)
plt.title('Step Response')
plt.ylabel('Amplitude')
plt.xlabel('Time/sec')
plt.grid(1)
plt.xlim(0, 1)
plt.ylim(0, 1.2)
plt.show()