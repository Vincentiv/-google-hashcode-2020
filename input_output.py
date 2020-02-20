import os


def parse_in(in_file):
    with open(in_file, 'r') as f:
        lines = f.readlines()
        books_count = lines[0].rstrip('\n').split(" ")[0]
        libraries_count = lines[0].rstrip('\n').split(" ")[1]
        days_count = lines[0].rstrip('\n').split(" ")[2]
        book_scores = lines[1].rstrip('\n').split(" ")
        libraries = []
        for i in range(2, len(lines) - 1, 2):
            line1 = lines[i].rstrip('\n').split(" ")
            line2 = lines[i + 1].rstrip('\n').split(" ")
            libraries += [[i//2-1, line1[0], line1[1], line1[2], line2], ]
        return books_count, libraries_count, days_count, book_scores, libraries


def write_solution(out_file, solution):
    with open(out_file, 'w') as f:
        f.write(f'{str(len(solution))}\n')
        for library in solution:
            f.write(f'{library[0]} {len(library[1])}\n')
            f.write(" ".join([str(book_id) for book_id in library[1]]) + "\n")


if __name__ == "__main__":
    dirname = os.path.dirname(__file__)
    path = os.path.join(dirname, 'data/a_example.in')
    books_count, libraries_count, days_count, book_scores, libraries = parse_in(path)
    # print(dynamic_prog(max_slices, pizza_types_count, pizza_slices))
