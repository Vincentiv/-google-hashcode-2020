from algorithms import *
import os

def parse_in(in_file):
    with open(in_file, 'r') as f:
        lines = f.readlines()
        max_slices = int(lines[0].rstrip('\n').split(" ")[0])
        pizza_types_count = int(lines[0].rstrip('\n').split(" ")[1])
        pizza_slices = list(map(int, lines[1].rstrip('\n').split(" ")))
        return max_slices, pizza_types_count, pizza_slices


def write_solution(out_file, pizza_ids=[]):
    with open(out_file, 'w') as f:
        f.writelines([str(len(pizza_ids))+"\n", " ".join([str(id) for id in pizza_ids])])


if __name__ == "__main__":
    dirname = os.path.dirname(__file__)
    path = os.path.join(dirname, 'data/a_example.in')
    max_slices, pizza_types_count, pizza_slices = parse_in(path)
    print(dynamic_prog(max_slices, pizza_types_count, pizza_slices))
