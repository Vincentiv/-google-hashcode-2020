from algorithms import *
import os


def parse_in(in_file):
    with open(in_file, 'r') as f:
        lines = f.readlines()
        books_count = lines[0].rstrip('\n').split(" ")[0]
        libraries_count = lines[0].rstrip('\n').split(" ")[1]
        days_count = lines[0].rstrip('\n').split(" ")[2]
        book_scores = lines[1].rstrip('\n').split(" ")
        libraries = []
        for i in range(3, len(lines), 2):
            line1 = lines[i].rstrip('\n').split(" ")
            line2 = lines[i+1].rstrip('\n').split(" ")
            libraries += [line1[0], line1[1], line1[2], line2]
        return books_count, libraries_count, days_count, book_scores, libraries


def write_solution(out_file, pizza_ids=[]):
    with open(out_file, 'w') as f:
        f.writelines([str(len(pizza_ids))+"\n", " ".join([str(id) for id in pizza_ids])])


if __name__ == "__main__":
    dirname = os.path.dirname(__file__)
    path = os.path.join(dirname, 'data/a_example.in')
    max_slices, pizza_types_count, pizza_slices = parse_in(path)
    print(dynamic_prog(max_slices, pizza_types_count, pizza_slices))
