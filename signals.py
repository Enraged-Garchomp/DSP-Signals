import math

#Signal for y = 1
def constant_signal(N, number):
    """Creates constant signal of number"""
    signal = [number for _ in range(N)]

    return signal

#Impulse signal
def impulse_signal(N, number):
    """Creates an impulse signal with the given amplitude at n = 0."""
    signal = [number if n == 0 else 0 for n in range(N)]

    return signal

def sine_signal(N, f):
    """Creates a Sine signal with sampling number N and frequency f"""
    signal = [math.sin(2 * math.pi * f * n / N) for n in range(N)]

    return signal

def cosine_signal(N, f):
    """Creates a Cosine signal with sampling number N and frequency f"""
    signal = [math.cos(2 * math.pi * f * n / N) for n in range(N)]

    return signal

def add_signals(x, y):
    """Adds two signals x and y"""
    if len(x) != len(y):
        raise ValueError("Signals must have same length")
    new_signal = [x[n] + y[n] for n in range(len(x))]

    return new_signal

def one_signal(signal_type, N, f):
    """Creates one signal with sampling number N"""
    if signal_type in ["sine", "cosine"]:
        if signal_type == "sine":
            signal = sine_signal(N, f)
        else:
            signal = cosine_signal(N, f)
    else:
        if signal_type == "constant":
            signal = constant_signal(N, f)
        elif signal_type == "impulse":
            signal = impulse_signal(N, f)
        else:
            raise ValueError("Signal type not supported")
    return signal

def two_signals(type1, type2, N, f1, f2):
    signal1 = one_signal(type1, N, f1)
    signal2 = one_signal(type2, N, f2)
    signal = add_signals(signal1, signal2)
    return signal

