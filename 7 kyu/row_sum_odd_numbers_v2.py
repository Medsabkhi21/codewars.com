def row_sum_odd_numbers(n):
 odd=[numb for numb in range(n*(n+1)) if numb % 2 != 0 ]
 return sum(odd[-n:])