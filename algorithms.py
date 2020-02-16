import numpy as np
from scipy import sparse


def zeros(rows, cols):
    return sparse.lil_matrix((rows, cols), dtype=int)


def getUsedItems(w, c):
    # item count
    i = len(c.rows) - 1
    currentW = len(c.rows[0]) - 1
    # set everything to not marked
    marked = []
    for i in range(i + 1):
        marked.append(0)
    while (i >= 0 and currentW >= 0):
        if (i == 0 and c[i, currentW] > 0) or c[i, currentW] != c[i - 1, currentW]:
            marked[i] = 1
            currentW = currentW - w[i]
        i = i - 1
    return marked


def zeroOneKnapsack(v, w, W):
    # c is the cost matrix
    c = []
    n = len(v)
    c = zeros(n, W + 1)
    for i in range(0, n):
        # for ever possible weight
        for j in range(0, W + 1):
            # can we add this item to this?
            if (w[i] > j):
                c[i, j] = c[i - 1, j]
            else:
                c[i, j] = max(c[i - 1, j], v[i] + c[i - 1, j - w[i]])
    return [c[n - 1, W], getUsedItems(w, c)]


def backwards(max_slices, pizza_types_count, pizza_slices):
    c = 0
    a = np.zeros([pizza_types_count])
    for p in reversed(range(pizza_types_count)):
        if c + pizza_slices[p] <= max_slices:
            print(p)
            a[p] = 1
            c += pizza_slices[p]
    return [i for i in range(len(a)) if a[i] == 1]


def do_sth(max_slices, pizza_types_count, pizza_slices):
    try:
        answer = zeroOneKnapsack(pizza_slices, pizza_slices, max_slices)
        return [i for i in range(len(answer[1])) if answer[1][i] == 1]
    except MemoryError:
        return backwards(max_slices, pizza_types_count, pizza_slices)


def brute_force(m, n, slices):
    return types_reccurs(m, 0, n, slices, [])


def types_reccurs(m, m_temp, n, slices, slices_temp):
    if len(slices) == 0:
        return m_temp, slices_temp
    if m_temp >= m:
        return 0, []
    if n == 0:
        return m_temp, slices_temp
    else:
        s0 = slices[0]
        m_temp0, slices_temp0 = types_reccurs(m, m_temp + s0, n - 1, slices[1:], slices_temp + [s0])
        m_temp1, slices_temp1 = types_reccurs(m, m_temp, n, slices[1:], slices_temp)
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
