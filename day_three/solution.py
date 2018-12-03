import re


def part1(claims):
    # rows, columns = find_matrix_size(claims)
    matrix = [['.']*1000 for _ in range(1000)]
    overlaps = 0
    for id_, l, t, w, h in claims:
        for i in range(t, t+h):
            for j in range(l, l+w):
                if matrix[i][j] == '.':
                    matrix[i][j] = id_
                else:
                    matrix[i][j] = 'X'
    for row in matrix:
        for cell in row:
            if cell == 'X':
                overlaps += 1
    print('overlaps:', overlaps)
    return matrix


def part2(matrix, claims):
    id_count = dict()
    for row in matrix:
        for id_ in row:
            if id_ != '.' and id_ != 'X':
                id_count[id_] = id_count.get(id_, 0) + 1
    for id_, _, _, w, h in claims:
        area = w * h
        if id_ in id_count.keys() and id_count[id_] == area:
            print('no-overlapped id:', id_)
            break


# load data
file_handler = open('input')
claims = list()
for line in file_handler:
    claim = list(map(int, re.findall(r'-?\d+', line)))
    claims.append(claim)

matrix = part1(claims)  # expected output 106501
part2(matrix, claims)  # expected output 632
