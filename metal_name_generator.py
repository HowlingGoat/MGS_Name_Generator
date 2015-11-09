#!/usr/bin/env python
import random
import argparse

## Arg Parsing Section
parser = argparse.ArgumentParser(description='Randomly generate MGS type names.')
parser.add_argument('-e', '--extended', help='Use the extended names (Not present in game).', action='store_true')
parser.add_argument('-n', help='Generate n number of names.', default=1, type=int)
parser.add_argument('-f', '--first', help='Add custom first names files.', nargs='*')
parser.add_argument('-l', '--last', help='Add custom last name files.', nargs='*')
seperator_help = """"Define a custom seperator. If it's not working or not giving the desired
 try using results 'single' or "double" quotes ' _ ' to help the parsing."""
parser.add_argument('-s', '--seperator', help=seperator_help, default=' ')

args = parser.parse_args()

n = args.n
extended = args.extended
args_first = args.first
args_last = args.last
seperator = args.seperator


## First in list will alway be run, every file preceding
# will be run in extended mode. This can be used to add permanently a file to
# the extended argument or to rename files.
first_files = ['First_Names.txt', 'First_Names_Extended.txt',]
last_files = ['Last_Names.txt', 'Last_Names_Extended.txt',]
## Change the separator, default is space.
# See the argparse argument

first_list = []
last_list = []




def add_lines(file_name, to_l):
    """Add lines to the proper list from a file."""
    with open(file_name, 'rb') as f:
        line = None
        while True:
            line = f.readline()
            line_stripped = line.strip('\n').strip('\r')
            line_lower = line_stripped.lower()
            transformed_line = line_lower
            if transformed_line == "":
                break
            else:
                to_l.append(transformed_line)


def random_gen(list_name):
    """Generate a random number that maps to a entry in the specified list."""
    number = len(list_name)
    ## Since it will be called from a list, has the range of 0 to len - 1
    rand = random.randint(0, (number - 1) )
    return rand


def generate_list(name_list, list_name):
    """Add items in the files to the list."""
    ## Add the main "official" list of names.
    try:
        add_lines(name_list[0], list_name)
    except IOError:
        exit('Sorry, the "%s" file is missing.' % name_list[0])
    ## Test for extended
    if extended == True:
        try:
            for i in name_list[1:]:
                add_lines(i, list_name)
        except IOError:
            exit('Sorry, the "%s" file is missing.' % i)
    # Test for optional -f or -l.
    try:
        for i in args_first:
            add_lines(i, list_name)
    except TypeError:
        ## Case that -f or -l are not defined.
        pass
    except IOError:
        exit('Sorry, I could not find "%s".' % i)


def main(count, seperator):
    """Main loop of the script. Generate both lists, then randomly selects
    from that list depending on how much times are needed. Returns everything
    as a list."""
    to_return = []
    ## Generate lists
    generate_list(first_files, first_list)
    generate_list(last_files, last_list)

    for i in range(count):
        ## Select the random number from the list of all possibilities.
        rand_f = random_gen(first_list)
        rand_l = random_gen(last_list)

        title_name = first_list[rand_f].title() + " " + last_list[rand_l].title()
        to_append = title_name.replace(" ", seperator)
        to_return.append(to_append)

    return to_return


if __name__ == "__main__":
    ## Main loop
    entries = main(n, seperator)

    for i in entries:
        print i

    exit()

