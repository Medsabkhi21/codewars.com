def descending_order(num):
 L=list(str(num)) ; k=""
 L.sort(reverse=True)
 for i in L :
    k+=i
 return int(k)