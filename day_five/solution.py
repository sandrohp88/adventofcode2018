import string


def part1(polymer_chain):
    lowercase_alphabet = string.ascii_lowercase
    possible_reactions = list()
    for letter in lowercase_alphabet:
        reaction = letter+letter.upper()
        possible_reactions.append(reaction)
        reaction = letter.upper() + letter
        possible_reactions.append(reaction)
        previous_size = -1
    while previous_size != len(polymer_chain):
        previous_size = len(polymer_chain)
        for reaction in possible_reactions:
            polymer_chain = polymer_chain.replace(reaction, '')
    return len(polymer_chain)


def part2(polymer_chain):
    best_reaction_size = len(polymer_chain) + 1
    for letter in string.ascii_lowercase:
        new_polymer_chain = polymer_chain.replace(letter, '')
        new_polymer_chain = new_polymer_chain.replace(letter.upper(), '')
        current_reaction_size = part1(new_polymer_chain)
        if current_reaction_size < best_reaction_size:
            best_reaction_size = current_reaction_size
    print(best_reaction_size)


# load data
file_handler = open('input')
polymer_chain = file_handler.read()

# print(possible_reactions)
part1(polymer_chain)  # expected output 10496
part2(polymer_chain)  # expected output 136571
