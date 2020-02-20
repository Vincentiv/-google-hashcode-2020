def do_sth(books_count, libraries_count, days_count, book_scores, libraries):
    # la liste des libraries sous la forme [[library_id1, [book_id0, book_id1, book_id2]], [library_id2, [book_id3, book_id4]]
    solution = []
    return solution

def dynamic_prog(w, nb_elements, w_array):
    matrix = [[0 for x in range(w)] for y in range(nb_elements)]

    for j in range(w):
        matrix[0][j] = 0
    print(matrix)

    for i in range(nb_elements):
        for j in range(w):
            if w_array[i] > j:
                matrix[i][j] = matrix[i-1][j]
            else:
                matrix[i][j] = max(matrix[i-1][j], matrix[i-1][j-w_array[i]] + w_array[i])

    return matrix[nb_elements-1][w-1]

def brute_force(m, n, slices):
    return types_reccurs(m, 0, n, slices, [], 0)


def types_reccurs(m, m_temp, n, slices, slices_temp, i):
    if len(slices) == 0:
        return m_temp, slices_temp
    if m_temp >= m:
        return 0, []
    if n == 0:
        return m_temp, slices_temp
    else:
        s0 = slices[0]
        m_temp0, slices_temp0 = types_reccurs(m, m_temp + s0, n - 1, slices[1:], slices_temp + [i], i+1)
        m_temp1, slices_temp1 = types_reccurs(m, m_temp, n, slices[1:], slices_temp, i+1)
        if m_temp0 < m_temp1:
            if m_temp1 <= m:
                return m_temp1, slices_temp1
            elif m_temp0 <= m:
                return m_temp0, slices_temp0
            else:
                return 0, []
        else:
            if m_temp0 <= m:
                return m_temp0, slices_temp0
            elif m_temp1 <= m:
                return m_temp1, slices_temp1
            else:
                return 0, []