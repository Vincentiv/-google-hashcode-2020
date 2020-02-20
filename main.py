from input_output import *
from algorithms import *
import os
from datetime import datetime

dirname = os.path.dirname(__file__)

if __name__ == "__main__":
    dir_name = os.path.dirname(__file__)
    data_path = os.path.join(dir_name, 'data')
    input_files = [f for f in os.listdir(data_path) if os.path.isfile(os.path.join(data_path, f))]
    for input_file in input_files:
        if (input_file)== ".DS_Store":
            continue
        input_path = os.path.join(dir_name, f'data/{input_file}')
        books_count, libraries_count, days_count, book_scores, libraries = parse_in(input_path)
        solution = do_sth(books_count, libraries_count, days_count, book_scores, libraries)
        write_solution(f"results/{datetime.now().strftime('%H%M%S')}.{input_file}.result", solution)
