def part1(data_input):
    frequency = 0
    for line in data_input:
        frequency += int(line)
    print(frequency)


def part2(data_input):
    current_frequency = 0
    frequencies = set()
    found = False
    index = 0
    while not found:
        current_frequency += data_input[index]
        if current_frequency in frequencies:
            found = True
        frequencies.add(current_frequency)
        # Start over if not found in each complete iteration
        index = (index+1) % len(data_input)
    print(current_frequency)


# load data
file_handler = open('input')
data_input = list()
for line in file_handler:
    data_input.append(int(line))
# data_input = [1, -2, 3, 1]
part1(data_input)  # expected output 477
part2(data_input)  # expected output 390
