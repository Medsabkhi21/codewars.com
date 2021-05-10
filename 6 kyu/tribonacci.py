def tribonacci(signature, n):
 assert n>=0
 sequence=signature
 for i in range(n+1) :
        sequence+=[sum(sequence[i:i+3])]
 return sequence[:-4]  