import sys
import numpy as np
f = open(sys.argv[1], 'r')
for i in f:
    s = i.rstrip().split()
    data1.append(s)
data_res= []
for i in data1:
    data_1 = []
    time_start = i[0].split(':')
    time_start = int(time_start[0])*60 + int(time_start[1])
    time_end = i[1].split(':')
    time_end = int(time_end[0])*60 + int(time_end[1])
    data_1 = [i for i in range(time_start,time_end)]
    if time_start == time_end:
        data_1.append(time_start)
    for i in data_1:
        data_res.append(i) #список , который включает в себя все диапазоны времени поминутно(считая от полуночи) каждого посещения)
max_count = []
for i in data_res:
    max_count.append(data_res.count(i))
max_count = sorted(max_count, reverse=True)
max= max_count[0]
end_data = []
for i in data_res:
    if data_res.count(i)==max:
        end_data.append(i)
end_data = sorted(list(set(end_data))) #минуты от полуночи, с максимальным кол-вом людей в банке








