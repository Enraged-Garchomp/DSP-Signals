import signal
import matplotlib.pyplot as plt

N = 100
f = 1
signal1 = signal.add_signals(signal.sine_signal(100, 10), signal.sine_signal(100, 2))
x_values = range(N)
y_values = signal1
plt.plot(x_values, y_values)
plt.xlabel("Samples")
plt.ylabel("Values")
plt.show()
