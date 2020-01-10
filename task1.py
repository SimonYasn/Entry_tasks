import numpy as np
dataset = input()
with open(dataset, 'r') as f:
    data = []
    for i in f:
        s = i.rstrip()
        data.append(int(s))
print("{:.2f}".format(np.percentile(data, 90)))
print("{:.2f}".format(np.median(data)))
print("{:.2f}".format(np.max(data)))
print("{:.2f}".format(np.min(data)))
print("{:.2f}".format(np.mean(data)))





