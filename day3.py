# file = 'day3.txt'
file = 'scrap.txt'
f = open(file,'r')
lists = f.read().splitlines()
print(lists)

# Get cordinate of maximum up, and right
def final_vertex(array):
    result = []
    x_sum_r = 0
    x_sum_l = 0
    y_sum_u = 0
    y_sum_d = 0
    for string in array:
        parts = string.split(',')
        print(parts)
        cordinate = [int(i[1:]) for i in parts ]
        x = []
        y = []
        print('Cordinate: ',cordinate)
        for i in range(len(cordinate)):
            if parts[i][0] == 'L':
                x.append(-1*cordinate[i])
                x_sum_l += cordinate[i]
            elif parts[i][0] == 'R':
                x.append(cordinate[i])
                x_sum_r += cordinate[i]
            if parts[i][0] == 'D':
                y.append(-1*cordinate[i])
                y_sum_d += cordinate[i]
            elif parts[i][0] == 'U':
                y.append(cordinate[i])
                y_sum_u += cordinate[i]
        print('Cordinate after: ', (x,y))
        result.append((x,y))
    return result,(-1*x_sum_l,x_sum_r),(-1*y_sum_d,y_sum_u)
# print(final_vertex(lists))
# mapping,extend_
mapping,h,v =final_vertex(lists)
print('horizontal:', h)
print('vertical:',v)

def print_matrix(matrix):
    for i in range(len(matrix)):
        print(matrix[i])
def replace_at_index(matrix,row,position,char):
    string = matrix[row]
    return string[:position] + char + string[position+1:]
def mapping_generate(l,r,u,d,startpoint = [-1,0]):
    matrix = []
    startpoint = [startpoint[0]-1,startpoint[1]+1]
    col = 0
    col = abs(l) + abs(r)+2
    tmp = '.' * col
    for row in range(abs(u)+abs(d)+2):
        matrix.append(tmp)
        # print(matrix[row])
    matrix[startpoint[0]] = replace_at_index(matrix,startpoint[0],startpoint[1],'O')
    print_matrix(matrix)
    pass

mapping_generate(h[0],h[1],v[1],v[0])
