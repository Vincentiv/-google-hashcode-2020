def do_sth(max_slices, pizza_types_count, pizza_slices):
    max_found, pizza_ids = brute_force(max_slices, pizza_types_count, pizza_slices)
    print("Max found : ", str(max_found))
    return pizza_ids


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
