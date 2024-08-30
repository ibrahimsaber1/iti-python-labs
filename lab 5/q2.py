# q2: ................... ............. ................... :)

import random
from typing import Optional, List

NUMBER_OF_GENERATIONS = 3
INDENT_LENGTH = 4

class Person:
    def __init__(self, parents: Optional[List['Person']], alleles: List[str]):
        # list of 2 elements of type Person
        self.parents = parents
        # list of 2 elements of type str
        self.alleles = alleles

def main():
    # create a new family with NUMBER_OF_GENERATIONS generations
    person = create_family(NUMBER_OF_GENERATIONS)
    
    # print out the family tree of blood types recursively
    print_family(person, 0)

def create_family(generations: int) -> Person:
    # Create a new person
    if generations > 1:
        # Recursively create parents
        parent_1: Person = create_family(generations - 1)
        parent_2: Person = create_family(generations - 1)
        
        # Set parents for the current person
        parents = [parent_1, parent_2]
        
        # Randomly assign current person's alleles based on the alleles of their parents
        allele_1 = random.choice(parent_1.alleles)
        allele_2 = random.choice(parent_2.alleles)
        alleles = [allele_1, allele_2]
    else:
        # Set parent pointers to None for the base generation
        parents = None
        
        # Randomly assign alleles for the initial generation
        allele_1 = get_random_allele()
        allele_2 = get_random_allele()
        alleles = [allele_1, allele_2]

    # Return newly created person
    return Person(parents, alleles)

def print_family(person: Optional[Person], number_of_generations: int):
    if not person:
        return
    print(f"{' ' * number_of_generations * INDENT_LENGTH}", end="")
    if number_of_generations == 0:
        print(f"Child (Generation {number_of_generations}): blood type {person.alleles[0]}{person.alleles[1]}")
    elif number_of_generations == 1:
        print(f"Parent (Generation {number_of_generations}): blood type {person.alleles[0]}{person.alleles[1]}")
    else:
        for i in range(number_of_generations - 2):
            print("great-", end="")
        print(f"grandparent (Generation {number_of_generations}): blood type {person.alleles[0]}{person.alleles[1]}")
    if person.parents:
        print_family(person.parents[0], number_of_generations + 1)
        print_family(person.parents[1], number_of_generations + 1)

def get_random_allele() -> str:
    return random.choice(["A", "B", "O"])

if __name__ == "__main__":
    main()



