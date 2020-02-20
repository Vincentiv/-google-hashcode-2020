def get_order_value(library):
    return library[5]/int(library[2])*int(library[3])


def do_sth(books_count, libraries_count, days_count, book_scores, libraries):
    for library in libraries:
        library += [sum([int(book_scores[int(book)]) for book in library[4]])]
        library[4] = sorted(library[4], key=lambda x: book_scores[int(x)], reverse=True)
    libraries_ordered = reversed(sorted(libraries, key=get_order_value))
    # la liste des libraries sous la forme [[library_id1, [book_id0, book_id1, book_id2]], [library_id2, [book_id3, book_id4]]
    solution = [[library[0], library[4]] for library in libraries_ordered]
    return solution