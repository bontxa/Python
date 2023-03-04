import numpy as np

def calculate(lista):
    if len(lista) != 9:
        raise ValueError("List must contain nine numbers.")
    tmp = np.empty((3, 3))
    length = 0
    for j in range(3):
        for i in range(3):
            tmp[j][i] = lista[length]
            length += 1
    flattened = tmp.flatten()
    mean = np.array([tmp.mean(axis=0), tmp.mean(axis=1)])
    variance = np.array([tmp.var(axis=0), tmp.var(axis=1)])
    standard_deviation = np.array([np.std(tmp, axis=0), np.std(tmp, axis=1)])
    min = np.array([tmp.min(axis=0), tmp.min(axis=1)]).astype(int)
    max = np.array([tmp.max(axis=0), tmp.max(axis=1)]).astype(int)
    sum = np.array([tmp.sum(axis=0), tmp.sum(axis=1)]).astype(int)
    my_mean = mean.tolist()
    my_mean.append(flattened.mean().tolist())
    my_variance = variance.tolist()
    my_variance.append(flattened.var().tolist())
    my_standard_deviation = standard_deviation.tolist()
    my_standard_deviation.append(np.std(flattened).tolist())
    my_max = max.tolist()
    my_max.append(flattened.max().astype(int).tolist())
    my_min = min.tolist()
    my_min.append(flattened.min().astype(int).tolist())
    my_sum = sum.tolist()
    my_sum.append(flattened.sum().astype(int).tolist())
    calculations = {
        'mean': my_mean,
        'variance': my_variance,
        'standard deviation': my_standard_deviation,
        'min': my_min,
        'max': my_max,
        'sum': my_sum
    }
    return calculations