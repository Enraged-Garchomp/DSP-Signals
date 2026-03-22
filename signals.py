import math

#Signal for y = 1
def constant_signal(N):
    """Creates constant signal of 1"""
    signal = []
    for _ in range(N):
        signal.append(1)
    return signal

#Impulse signal
def impulse_signal(N):
    """Creates Impulse Signal of 1 and 0"""
    signal = []
    for n in range(N):
        if n == 0:
            signal.append(1)
        else:
            signal.append(0)
    return signal

def sine_signal(N, f):
    """Creates a Sine signal with sampling number N and frequency f"""
    signal = []
    for n in range(N):
        x = math.sin(2 * math.pi * f * n / N)
        signal.append(x)
    return signal

def cosine_signal(N, f):
    """Creates a Cosine signal with sampling number N and frequency f"""
    signal = []
    for n in range(N):
        x = math.cos(2 * math.pi * f * n / N)
        signal.append(x)
    return signal

def add_signals(x, y):
    """Adds two signals x and y"""
    if len(x) != len(y):
        raise ValueError("Signals must have same length")

    new_signal = []
    for n in range(len(x)):
        new_signal.append(x[n] + y[n])

    return new_signal

def choose_signals(N):
    """Gives you signals you choose"""
    should_add_signals = input("Would you like to add 2 signals? (yes/no) ")
    if should_add_signals == "yes":
        signal_type_1 = input("What type of signal would you like (function 1)? (sine, cosine, linear, impulse) ")
        signal_type_2 = input("What type of signal would you like (function 2)? (sine, cosine, linear, impulse) ")
        if signal_type_1 == "sine":
            f = int(input("What is the frequency you would like to add (function 1)? "))
            signal1 = sine_signal(N, f)
        elif signal_type_1 == "cosine":
            f = int(input("What is the frequency you would like to add (function 1)? "))
            signal1 = cosine_signal(N, f)
        elif signal_type_1 == "linear":
            signal1 = constant_signal(N)
        elif signal_type_1 == "impulse":
            signal1 = impulse_signal(N)
        else:
            raise ValueError("Must respond with (sine, cosine, linear, impulse)")
        if signal_type_2 == "sine":
            f1 = int(input("What is the frequency you would like to add (function 2)? "))
            signal2 = sine_signal(N, f1)
        elif signal_type_2 == "cosine":
            f1 = int(input("What is the frequency you would like to add (function 2)? "))
            signal2 = cosine_signal(N, f1)
        elif signal_type_2 == "linear":
            signal2 = constant_signal(N)
        elif signal_type_2 == "impulse":
            signal2 = impulse_signal(N)
        else:
            raise ValueError("Must respond with (sine, cosine, linear, impulse)")
        final_signal = add_signals(signal1, signal2)
        return final_signal

    elif should_add_signals == "no":
        signal_type = input("What type of signal would you like? (sine, cosine, linear, impulse) ")
        if signal_type == "sine":
            f = int(input("What frequency would you like? "))
            signal = sine_signal(N, f)
        elif signal_type == "cosine":
            f = int(input("What frequency would you like? "))
            signal = cosine_signal(N, f)
        elif signal_type == "linear":
            signal = constant_signal(N)
        elif signal_type == "impulse":
            signal = impulse_signal(N)
    else:
        raise ValueError("Must respond with yes/no")
    return signal