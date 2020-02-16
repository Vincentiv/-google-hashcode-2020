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


if __name__ == "__main__":
    w = 100
    i = 10
    w_array = [4, 14, 15, 18, 29, 32, 36, 82, 95, 95]
    print(dynamic_prog(w, i, w_array))