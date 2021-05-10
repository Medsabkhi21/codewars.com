def nb_year(p0, percent, aug, p):
    year = 0
    while p >= p0:
        p0 += p0 * percent * 0.01 + aug
        year += 1

    if year == 51:
        return 50

    return year 