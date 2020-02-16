def parse_in(in_file):
    with open(in_file, 'r') as f:
        for line in f:
            print(line)


def write_solution(out_file,pizza_ids=[]):
    with open(out_file, 'w') as f:
        f.write(len(pizza_ids))
        f.write(" ".join(pizza_ids))


if __name__ == "__main__":
    path = "/home/anais/Downloads/a_example.in"
    parse_in(path)
