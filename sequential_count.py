import sys



def count_letters_sequential(file_path):

    letter_counts = {}



    with open(file_path, 'r') as file:

        for line in file:

            for char in line:

                if char.isalpha():

                    char = char.lower()

                    letter_counts[char] = letter_counts.get(char, 0) + 1



    return letter_counts



def write_output(letter_counts):

    with open('output.txt', 'w') as output_file:

        for letter, count in sorted(letter_counts.items()):

            output_file.write(f"{letter} {count}\n")



if __name__ == "__main__":

    if len(sys.argv) != 2:

        print("Usage: python sequential_count.py <input_file>")

        sys.exit(1)



    input_file = sys.argv[1]

    counts = count_letters_sequential(input_file)

    write_output(counts)

