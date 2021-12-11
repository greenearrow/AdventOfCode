# %%
def load(file_name) -> list:
    output=[]
    with open(file_name) as f:
        data = f.readlines()
    for line in data:
        line = line.replace('\n','').split(' -> ')
        line = [line[0].split(','),line[1].split(',')]
        line = [tuple([int(i) for i in l]) for l in line]
        output.append(line)
    return output

if __name__ == '__main__':
    starts_stops = load(r'data\day_5.txt')

# %%
def give_path_for_all(starts_stops) -> list:
    paths = []
    for start_stop in starts_stops:
        paths.append(give_path(start_stop))
    return paths

def give_path(start_stop) -> list:
    start = start_stop[0]
    stop = start_stop[1]
    if len(start_stop)>2: raise ValueError
    if start[0] == stop[0] or start[1] == stop[1]:
        if start[0] == stop[0]:
            path = [[start[0],y] for y in range(start[1],stop[1]+1)]
        if start[1] == stop[1]:
            path = [[x,start[1]] for x in range(start[0],stop[0]+1)]
    else: path = [[],[]]
    return path





# %%
grid = [[0 for j in range(0,1000)] for i in range(0,1000)]


# %%
paths = give_path_for_all(load(r'data\day_5.txt'))
print(paths)

# %%



