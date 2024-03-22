import sys

import threading



def count_letters_parallel(file_path):

    letter_counts = {}



    def count_in_thread(start, end):

        nonlocal letter_counts

        with open(file_path, 'r') as file:

            file.seek(start)

            chunk = file.read(end - start)

            for char in chunk:

                if char.isalpha():

                    char = char.lower()

                    letter_counts[char] = letter_counts.get(char, 0) + 1



    thread_count = 4  # You can adjust this based on your system's capability

    threads = []

    with open(file_path, 'r') as file:

        file_size = file.seek(0, 2)

        chunk_size = file_size // thread_count

        for i in range(thread_count):

            start = chunk_size * i

            end = chunk_size * (i + 1) if i < thread_count - 1 else file_size

            thread = threading.Thread(target=count_in_thread, args=(start, end))

            threads.append(thread)

            thread.start()



        for thread in threads:

            thread.join()



    return letter_counts



def write_output(letter_counts):

    with open('output.txt', 'w') as output_file:

        for letter, count in sorted(letter_counts.items()):

            output_file.write(f"{letter} {count}\n")



if __name__ == "__main__":

    if len(sys.argv) != 2:

        print("Usage: python parallel_count.py <input_file>")

        sys.exit(1)



    input_file = sys.argv[1]

    counts = count_letters_parallel(input_file)

    write_output(counts)

