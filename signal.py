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

def add_signals(x, y):
    """Adds two signals x and y"""
    new_signal = []
    if len(x) != len(y):
        raise ValueError("Signals must have same length")
    else:
        for n in range(len(x)):
            new_signal.append(x[n] + y[n])

    return new_signal

def generate_x_values(N):
    """Generates x values for N samples"""
    values = []
    for n in range(N):
        values.append(n)
    return values

