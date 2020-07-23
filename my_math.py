import math

def cos(t):
    t %= math.pi * 2
    if (t < math.pi * 0.25):
        return _cos(t)
    elif (t < math.pi * 0.75):
        return -_sin(t - math.pi * 0.5)
    elif (t < math.pi * 1.25):
        return -_cos(t - math.pi)
    elif (t < math.pi * 1.75):
        return _sin(t - math.pi * 1.5)
    else:
        return _cos(t - math.pi * 2)

def _sin(t):
    result = current = t;
    # テイラー展開
    for i in range(2, 8, 2):
        current *= - t * t / (i * (i + 1))
        result += current
    return result

def _cos(t):
    result = current = 1;
    # テイラー展開
    for i in range(1, 9, 2):
        current *= - t * t / (i * (i + 1))
        result += current
    return result
