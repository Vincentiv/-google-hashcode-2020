import numpy as np

def get_order_value(library):
    return library[5] / int(library[2]) * int(library[3])


def do_sth(books_count, libraries_count, days_count, book_scores, libraries):
    books_sent = [False for _ in range(int(books_count))]
    for library in libraries:
        library += [sum([int(book_scores[int(book)]) for book in library[4]])]
        library[4] = sorted(library[4], key=lambda x: book_scores[int(x)], reverse=True)
    libraries_ordered = reversed(sorted(libraries, key=get_order_value))
    libraries_solution = []
    for library in libraries_ordered:
        library[4] = [book for book in library[4] if not books_sent[int(book)]]
        for book in library[4]:
            books_sent[int(book)] = True
        if len(library[4])>0:
            libraries_solution += [library, ]
    # la liste des libraries sous la forme [[library_id1, [book_id0, book_id1, book_id2]], [library_id2, [book_id3, book_id4]]
    solution = [[library[0], library[4]] for library in libraries_ordered]
    return solution


def do_sth_bis(books_count, libraries_count, days_count, book_scores, libraries):
    libraries_scores = [np.dot(create_one_hot(library[4]), book_scores) for library in libraries]
    for library in libraries:
        lib_one_hot = create_one_hot(library[4])
        library_score = np.dot(lib_one_hot, book_scores)
        library += [sum([int(book_scores[int(book)]) for book in library[4]])]
        library[4] = sorted(library[4], key=lambda x: book_scores[int(x)], reverse=True)
    libraries_ordered = reversed(sorted(libraries, key=get_order_value))
    # la liste des libraries sous la forme [[library_id1, [book_id0, book_id1, book_id2]], [library_id2, [book_id3, book_id4]]
    solution = [[library[0], library[4]] for library in libraries_ordered]
    return solution


def create_one_hot(v):
    targets = np.array(v).reshape(-1)
    return list(np.sum(np.eye(nb_classes)[targets], axis=0))

def new_score(scores, one_hot):
    inverse_one_hot = np.subtract([1]*6,one_hot_targets)
    return list(np.multiply(l,inverse_one_hot))
