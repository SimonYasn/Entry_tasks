import sys
import numpy as np
with open(sys.argv[1], 'r') as f:
    data = []
    for i in f:
        s = i.rstrip()
        data.append(int(s))
print("{:.2f}".format(np.percentile(data, 90)),'\n'
      "{:.2f}".format(np.median(data)),'\n'
      "{:.2f}".format(np.max(data)),'\n'
      "{:.2f}".format(np.min(data)),'\n'
      "{:.2f}".format(np.mean(data)))





