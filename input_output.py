def parse_in(in_file):
    with open(in_file, 'r') as f:
        for line in f:
            print(line)


def write_solution(out_file, line_to_write):
    with open(out_file, 'a') as f:
        f.write(line_to_write)


if __name__ == "__main__":
    path = "/home/anais/Downloads/a_example.in"
    parse_in(path)