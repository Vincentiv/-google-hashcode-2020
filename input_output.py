from algorithms import *

def parse_in(in_file):
    with open(in_file, 'r') as f:
        lines = f.readlines()
        max_slices = int(lines[0].rstrip('\n').split(" ")[0])
        pizza_types_count = int(lines[0].rstrip('\n').split(" ")[1])
        pizza_slices = list(map(int, lines[1].rstrip('\n').split(" ")))
        return max_slices, pizza_types_count, pizza_slices


def write_solution(out_file, line_to_write):
    with open(out_file, 'a') as f:
        f.write(line_to_write)


if __name__ == "__main__":
    path = "/home/anais/Downloads/d_quite_big.in"
    max_slices, pizza_types_count, pizza_slices = parse_in(path)
    print(dynamic_prog(max_slices, pizza_types_count, pizza_slices))