from collections import defaultdict
import string


def part1(all_steps, restrictions, first):
    done = first
    all_steps.remove(first)
    next_step = ''
    while all_steps:
        aviables = aviables_steps(done, all_steps, restrictions)
        next_step = min(aviables)
        all_steps.remove(next_step)
        done += next_step
    print(done)
    return(done)


def aviables_steps(done, all_steps, restrictions):
    aviables = set()
    done = set(done)
    for step in all_steps:
        if restrictions[step].issubset(done):
            aviables.add(step)
    aviables = aviables.difference(done)
    return aviables


def part2(all_steps, restrictions, first):
    times = defaultdict(str)
    for i, letter in enumerate(string.ascii_uppercase, 61):
        times[letter] = i
    done = first
    all_steps.remove(first)
    aviables = set()
    seconds_counter = 0
    while all_steps:
        aviables = sorted(aviables_steps(done, all_steps, restrictions))
        for i in range(min(5, len(aviables))):
            times[aviables[i]] -= 1
        for aviable in aviables:
            if times[aviable] < 1:
                done += aviable
                all_steps.remove(aviable)
        seconds_counter += 1
    print(seconds_counter)


file_handler = open('input').read().split('\n')
root = file_handler[0].split()[1]
restrictions = defaultdict(set)
all_steps = set()
for step in file_handler:
    step = step.split()
    first, second = step[1], step[7]
    all_steps.update((first, second))
    restrictions[second].add(first)

# expected output LAPFCRGHVZOTKWENBXIMSUDJQY
part1(all_steps.copy(), restrictions, root)
part2(all_steps, restrictions, first)  # expected output 936
