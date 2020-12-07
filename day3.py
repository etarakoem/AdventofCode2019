file = 'day3.txt'
# file = 'scrap.txt'
f = open(file,'r')
lists = f.read().splitlines()
# Get individual list of input:
wire_1 = lists[0].split(',')
wire_2 = lists[1].split(',')
# print('wire 1:',wire_1)
# print('wire 2:',wire_2)

def where_tf_am_i(where_to):
    # I will make a dictionary, to take note of every single steps
    # Then look for each wires if they crossed at any similar cordinate
    # As known as, intersection
    all_turn = {}

    # x,y cordinate to take note at every single point of steps
    x_pos = 0
    y_pos = 0
    # Count up every turn, to do the latter part in part 2, count steps
    turn = 0

    for pos in where_to:
        # Get up,down,left,right, the direction
        heading = pos[0]

        # Get the value of steps needed
        steps = int(pos[1:])

        # Number of steps needed
        go_x = 0
        go_y = 0
        if heading == 'R':
            go_x = 1
        elif heading == 'L':
            go_x = -1
        elif heading == 'D':
            go_y = -1
        elif heading == 'U':
            go_y = 1
        for i in range(steps):
            x_pos += go_x
            y_pos += go_y
            turn += 1
            if (x_pos,y_pos) not in all_turn:
                all_turn[(x_pos,y_pos)] = turn
    return all_turn

# Turn off the comment to see all of the map.
wire_1_map = where_tf_am_i(wire_1)
wire_2_map = where_tf_am_i(wire_2)
# print('Wire_1 map:',wire_1_map)
# print('Wire_2 map:',wire_2_map)

# Get intersections:
intersections = set(wire_1_map).intersection(wire_2_map)
# print('intersections: ',intersections)

sum_cordinate = lambda x: abs(x[0])+ abs(x[1])

# Part 1 first answer, get all the distance
intersections_sum = list(map(sum_cordinate,intersections))
print('Final result part 1: ',min(intersections_sum))

# Part 2:
steps = [wire_1_map[i] + wire_2_map[i] for i in intersections]
# print(steps)
print('Minimum steps at part 2 = ',min(steps))
