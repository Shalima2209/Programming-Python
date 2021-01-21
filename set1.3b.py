def sqsum(n) :
   sm = 0
   for i in range(1, n+1) :
      sm = sm + pow(i,2)
   return sm
n = 8
print(sqsum(n))
