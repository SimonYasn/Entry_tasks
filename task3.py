import sys 
cash1 = open('{}/cash1.txt'.format(sys.argv[1]), 'r')
cash2 = open('{}/cash2.txt'.format(sys.argv[1]), 'r')
cash3 = open('{}/cash3.txt'.format(sys.argv[1]), 'r')
cash4 = open('{}/cash4.txt'.format(sys.argv[1]), 'r')
cash5 = open('{}/cash5.txt'.format(sys.argv[1]), 'r')
data1 = []
for i in cash1:
    s = i.rstrip()
    data1.append(float(s))
data2 = []
for i in cash2:
    s = i.rstrip()
    data2.append(float(s))
data3 = []
for i in cash3:
    s = i.rstrip()
    data3.append(float(s))
data4 = []
for i in cash4:
    s = i.rstrip()
    data4.append(float(s))
data5 = []
for i in cash5:
    s = i.rstrip()
    data5.append(float(s))
dict = {}
for i in range(16):
    dict[i] = data1[i]+data2[i]+data3[i]+data4[i]+data5[i]
dict.values()
val = dict.values()
val = list(val)
val.sort()
result = val[15]
for i in dict:
    if dict[i]==result:
        print(i+1)
        break





