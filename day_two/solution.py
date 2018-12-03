def has_num_chars(string, num):
    # Return True if at least one character of string appears exactly num times
    # False otherwise
    char_counter = dict()
    for c in string:
        char_counter[c] = char_counter.get(c, 0) + 1
    return num in char_counter.values()


def close_id(id1, id2):
    # Return all commons characters between id1 and id2 if they only differ
    # in just one character position aware, otherwise returns an empty string
    diff, index = 0, 0
    common_characters = ''
    while index < len(id1) and diff < 2:
        if id1[index] != id2[index]:
            diff += 1
        else:
            common_characters += id1[index]
        index += 1
    if diff == 1:
        return common_characters
    else:
        return ''


def part1(data_input):
    count_two = 0
    count_three = 0
    for code in data_input:
        count_two += 1 if has_num_chars(code, 2) else 0
        count_three += 1 if has_num_chars(code, 3) else 0
    print(count_two * count_three)


def part2(input_data):
    for i in range(len(input_data) - 1):
        for j in range(i+1, len(input_data)):
            common_characters = close_id(input_data[i], input_data[j])
            if common_characters:
                print(common_characters)
                break


# load data
file_handler = open('input')
data_input = list()
for line in file_handler:
    data_input.append(line)
part1(data_input)  # expected output 6225
part2(data_input)  # expected output revtaubfniyhsgxdoajwkqilp
