import signals
import matplotlib.pyplot as plt


N = int(input("Enter number of samples to take: "))
should_add_signals = input("Would you like to add 2 signals? (yes/no) ")
if should_add_signals == "yes":
    signal_1 = input("What type of signal would you like (function 1)? (sine, cosine, linear, impulse) ")
    signal_2 = input("What type of signal would you like (function 2)? (sine, cosine, linear, impulse) ")
    f1 = int(input("What is the frequency you would like to add (function 1)? "))
    f2 = int(input("What is the frequency you would like to add (function 2)? "))
    signal_to_plot = signals.two_signals(signal_1, signal_2, N, f1, f2)
elif should_add_signals == "no":
    signal_type = input("What kind of signal would you like? (sine, cosine, linear, impulse) ")
    f = int(input("What is the frequency you would like? "))
    signal_to_plot = signals.one_signal(signal_type, N, f)
else:
    raise ValueError("Please enter either 'yes' or 'no'")

plot_signal = signal_to_plot

print(f"Values: {plot_signal}")

plt.plot(range(N), plot_signal)
plt.xlabel("Samples")
plt.ylabel("Values")
plt.show()
