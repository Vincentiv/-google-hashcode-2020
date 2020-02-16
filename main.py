from input_output import *
from algorithms import *
import os
from datetime import datetime

dirname = os.path.dirname(__file__)

if __name__ == "__main__":
    input_file = "a_example.in"
    input_path = os.path.join(dirname, f'data/{input_file}')
    max_slices, pizza_types_count, pizza_slices = parse_in(input_path)
    solution = do_sth(max_slices, pizza_types_count, pizza_slices)
    write_solution(f"results/{input_file}.{datetime.now().strftime('%H%M%S')}.result", solution)
