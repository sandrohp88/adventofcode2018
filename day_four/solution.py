from collections import defaultdict


def parse_time(time):
    return int(time.split(':')[-1])


def create_grid(data_input):
    grid = defaultdict(lambda: [0 for x in range(60)])
    fall = None
    wakes = None
    for line in data_input:
        if line[2] == "Guard":
            guard_id = line[3]
        elif line[2] == "falls":
            fall = parse_time(line[1])
        else:  # wake up
            wakes = parse_time(line[1])
            for minute in range(fall, wakes):
                grid[guard_id][minute] += 1
    return grid


def part1(grid):
    guards = create_grid(grid)
    # sort bye sum of minutes asleep
    guard = sorted(guards.keys(), key=lambda g: sum(
        guards[g]), reverse=True)[0]
    minutes = guards[guard]
    best_minute = minutes.index(max(minutes))
    guard = int(guard[1:])
    print(best_minute * guard)


def part2(grid):
    guards = create_grid(grid)
    guard = sorted(guards.keys(), key=lambda g: max(
        guards[g]), reverse=True)[0]
    minutes = guards[guard]
    best_minute = minutes.index(max(minutes))
    guard = int(guard[1:])
    print(best_minute * guard)


# load data
file_handler = open('input')
data_input = list()
for line in file_handler:
    line = line.replace('[', '')
    line = line.replace(']', '')
    line = line.split()
    data_input.append(line)
data_input = sorted(data_input)
part1(data_input)  # expected output 30630
part2(data_input)  # expected output 136571
