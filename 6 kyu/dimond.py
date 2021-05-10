def diamond(n):
    if n < 1 or n % 2 == 0:
        return None
    diamondShape = ''
    for i in range(n):
        diamondRow = '*' * (i * 2 + 1) if i <= n / 2 else '*' * ((n - i) * 2 - 1)
        diamondShape += ' ' * int((n - len(diamondRow)) / 2) + diamondRow + '\n'
    return diamondShape