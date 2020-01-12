import sys
import numpy as np
data = []
data_end = []
with open("txt.txt") as f:
    for line in f:
        data.append([float(x) for x in line.split()])
with open("txt2.txt") as f:
    for line in f:
        data_end.append([float(x) for x in line.split()])
for point in data_end:
            print(point)
            err = 0
            for i in data:  #проверка угла на вершине
                  if i == point:
                        print('na ugle')
                        err = 1
                        break
                
            if err == 0:
                    x11 = [data[0][0]- point[0], data[0][1]- point[1]]
                    x21 = [data[1][0]- point[0], data[1][1]- point[1]]
                    x31 = [data[2][0]- point[0], data[2][1]- point[1]] 
                    x41 = [data[3][0]- point[0], data[3][1]- point[1]]
                    tangle1 = math.acos((x11[0]*x21[0]+x11[1]*x21[1])/ (math.sqrt(x11[0]*x11[0]+x21[0]*x21[0])*math.sqrt(x11[1]*x11[1]+x21[1]*x21[1])))
                    print(tangle1) #если сумма всех углов, образованных векторами , которые берут начало в исследуемой точке, равна 360* => точка внутри, иначе - снаружи)

            # Если один из углов равен 180* => точка на лежит на одной из сторон





