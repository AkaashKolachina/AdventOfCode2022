from sys import argv

def process(lines):
    s_to_b = {}
    for line in lines:
        parts = line.split(':')
        sens_parts = parts[0].split(' ')
        sens_x = sens_parts[2][:-1]
        sens_y = sens_parts[3]
        sens_pos = (int(sens_x.split('=')[1]), int(sens_y.split('=')[1]))

        beac_parts = parts[1].strip().split(' ')
        b_x = beac_parts[4][:-1]
        b_y = beac_parts[5].strip()
        b_pos = (int(b_x.split('=')[1]), int(b_y.split('=')[1]))
        s_to_b[sens_pos] = b_pos
        beacons.add(b_pos)
    return s_to_b

def get_dist(point_1, point_2):
    return abs(point_1[0] - point_2[0]) + abs(point_1[1] - point_2[1])

def add_points(x_1, x_2):
    for x in range(x_1, x_2 + 1):
        if (x,y) not in beacons:
            empty.add(x)

lines = []
beacons = set()
with open(argv[1],"r") as f:
    lines = f.readlines()

s_to_b = process(lines)
y = int(argv[2])
empty = set()


for sensor in s_to_b:
    beacon = s_to_b[sensor]
    dist = get_dist(sensor, beacon)
    y_d = abs(sensor[1] - y)
    if y_d > dist:
        continue
    x_d = dist - y_d
    min_x = sensor[0] - x_d
    max_x = sensor[0] + x_d
    add_points(min_x,max_x)


print(len(empty))
