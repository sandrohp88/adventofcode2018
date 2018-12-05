import string

# part1


def react(polymer_chain):
    lowercase_alphabet = string.ascii_lowercase
    possible_reactions = list()
    for letter in lowercase_alphabet:
        reaction = letter+letter.upper()
        possible_reactions.append(reaction)
        reaction = letter.upper() + letter
        possible_reactions.append(reaction)

    previous_size = -1
    actual_size = len(polymer_chain)
    while previous_size != actual_size:
        previous_size = len(polymer_chain)
        for reaction in possible_reactions:
            polymer_chain = polymer_chain.replace(reaction, '')
        actual_size = len(polymer_chain)
    return actual_size


def part2(polymer_chain):
    best_reaction_size = len(polymer_chain) + 1
    for letter in string.ascii_lowercase:
        new_polymer_chain = polymer_chain.replace(letter, '')
        new_polymer_chain = new_polymer_chain.replace(letter.upper(), '')
        current_reaction_size = react(new_polymer_chain)
        if current_reaction_size < best_reaction_size:
            best_reaction_size = current_reaction_size
    print(best_reaction_size)


# load data
file_handler = open('input')
polymer_chain = file_handler.read()

# print(possible_reactions)
print(react(polymer_chain))  # expected output 10496
part2(polymer_chain)  # expected output 5774
