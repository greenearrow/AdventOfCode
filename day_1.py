with open(r'data\day_1.txt','r') as file:
    data = [int(line.rstrip()) for line in file]
print(len([1 for i, j in zip(data[0:-1],data[1:]) if j > i]))
#Simpler day 2 solution
print(len([1 for i, j in zip(data[0:-1],data[3:]) if j > i]))
windows = [i+j+k for i, j, k in zip(data[0:-2], data[1:-1], data[2:])]
print(len([1 for i, j in zip(windows[0:-1],windows[1:]) if j > i]))