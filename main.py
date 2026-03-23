import signals
import matplotlib.pyplot as plt

def get_param(signal_type):
    if signal_type in ["sine", "cosine"]:
        param = int(input("What is the frequency you would like? "))
    elif signal_type in ["constant", "impulse"]:
        param = int(input("What is the amplitude you would like? "))
    else:
        raise ValueError("Please enter either a supported signal type")
    return param

N = int(input("Enter number of samples to take: "))
should_add_signals = input("Would you like to add 2 signals? (yes/no) ")
if should_add_signals == "yes":
    signal_1 = input("What type of signal would you like (function 1)? (sine, cosine, constant, impulse) ")
    param1 = get_param(signal_1)
    signal_2 = input("What type of signal would you like (function 2)? (sine, cosine, constant, impulse) ")
    param2 = get_param(signal_2)
    signal_to_plot = signals.two_signals(signal_1, signal_2, N, param1, param2)
elif should_add_signals == "no":
    signal_type = input("What kind of signal would you like? (sine, cosine, constant, impulse) ")
    param = get_param(signal_type)
    signal_to_plot = signals.one_signal(signal_type, N, param)
else:
    raise ValueError("Please enter either 'yes' or 'no'")

plot_signal = signal_to_plot

print(f"Values: {plot_signal}")

plt.plot(range(N), plot_signal)
plt.xlabel("Samples")
plt.ylabel("Values")
plt.show()
