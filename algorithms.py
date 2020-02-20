def get_signup_time(library):
    return library[2]

def do_sth(books_count, libraries_count, days_count, book_scores, libraries):
    print(libraries)
    libraries_ordered = sorted(libraries, key=get_signup_time)
    # la liste des libraries sous la forme [[library_id1, [book_id0, book_id1, book_id2]], [library_id2, [book_id3, book_id4]]
    solution = [[library[0], library[4]] for library in libraries_ordered]
    return solution