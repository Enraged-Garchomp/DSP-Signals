import signals
import matplotlib.pyplot as plt

N = int(input("Enter number of samples to take: "))
plot_signal = signals.choose_signals(N)

print(f"Values: {plot_signal}")

plt.plot(range(N), plot_signal)
plt.xlabel("Samples")
plt.ylabel("Values")
plt.show()
