def Primes(start,end):
 prime=[]
 for i in range(start, end+1):
  for j in range(1,(i+1)):
   if(i%j==0 and i!=j and j!=1):
    break
   elif (i%j==0 and i==j):
    prime.append(i)
   else:
    continue
 return prime

def Primes_sets(start,end,cup):
 primeset=[]
 prime=Primes(start,end)
 for i in range(len(prime)):
  if(i>(len(prime)-1)):
   break
  elif (prime[i]-prime[i-1]==cup):
   primeset.append([prime[i-1],prime[i]])
  else:
   continue
 return primeset

def NumOfPrimes(n):
 wprime=[]
 i=0
 k=0
 while k<n:
  i+=1
  for j in range (1,(i+1)):
   if(i%j==0 and i!=j and j!=1):
    break
   elif(i%j==0 and i==j):
    wprime.append(i)
    k+=1
    break
   else:
    continue
 return wprime

def Prime_B(n):
 temp=[1]
 multi=[]
 i=2
 while i<=n:
  if(n%i==0):
   n/=i
   if(max(temp)!=i):
    temp.append(i)
   else:
    multi.append(i)
  else:
   i+=1
 return temp, multi

print(Prime_B(400))
print(NumOfPrimes(10))
print(Primes_sets(0,37,2))
print(Primes(10,37))
