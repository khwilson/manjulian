"""
This generates bounds for products of coefficients of points in our fundamental domain.

Pypy to be used. 
"""
import sys
sys.setrecursionlimit(2000)
import itertools
subsets = []
def findsubsets(S):
  A = []
  m = 0
  while(m <= len(S)):
    A.append(itertools.combinations(S,m))
    m+=1
  for k in A:
    for l in k:
       l = list(l)
       subsets.append(l)
findsubsets([0,1,2,3,4,5,6,7,8,9,10,11])
gamma = [[0,1,1,1],[0,1,2,1],[0,1,3,1],[0,2,2,1],[0,2,3,1],[0,3,3,1],[0,1,1,-1],[0,1,2,-1],[0,1,3,-1],[0,2,2,-1],[0,2,3,-1],[0,3,3,-1]]
print len(subsets)
def check(list):
  I = 0
  J = 0
  K = 0
  AB = 0
  i = 0
  while(i < len(list)):
    if(gamma[list[i]][1] == 1):
      I+=1
    if(gamma[list[i]][2] == 1):
      I+=1
    if(gamma[list[i]][1] == 2):
      J+=1
    if(gamma[list[i]][2] == 2):
      J+=1
    if(gamma[list[i]][1] == 3):
      K+=1
    if(gamma[list[i]][2] == 3):
      K+=1
    AB += gamma[list[i]][3]
  if(I+J >=2*K and 2*I>=J+K and AB>=0):
    return 0
  change=0
  while(I+J < 2*K or 2*I < J+K or AB < 0):
      I+=2
      AB+=1
      change+=1
  return change

abval = [[0,0,0,0,0,0,0,0,0,0,0,0],[0.5,0,0,0,0,0,0,0,0,0,0,0],[0.75,0.5,0,0,0,0,0,0,0,0,0,0],[0.25,1,0,0,0,0,0,0,0,0,0,0],[0.625,2.125,0.5,0.5,0,0,0,0,0,0,0,0],[23.0/16.0,3.625,1.5,0.25,1,0,0,0,0,0,0,0],[0.5,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0.5,0,0,0,0,0],[0,0,0,0,0,0,0.75,0.5,0,0,0,0],[0,0,0,0,0,0,0.25,1,0,0,0,0],[0,0,0,0,0,0,0.625,2.125,0.5,0.5,0,0],[0,0,0,0,0,0,23.0/16.0,3.625,1.5,0.25,1,0]]

cdval = [[1,0,0,0,0,0,0,0,0,0,0,0],[0.5,1,0,0,0,0,0,0,0,0,0,0],[0.5,0.5,1,0,0,0,0,0,0,0,0,0],[0.25,1,0,1,0,0,0,0,0,0,0,0],[0.25,1,0.5,0.5,1,0,0,0,0,0,0,0],[0.25,0.25,1,0.25,1,1,0,0,0,0,0,0],[0.5,0,0,0,0,0,1,0,0,0,0,0],[0.25,0.5,0,0,0,0,0.5,1,0,0,0,0],[0.25,0.25,0.5,0,0,0,0.5,0.5,1,0,0,0],[0.125,0.5,0,0.5,0,0,0.25,1,0,1,0,0],[0.125,0.5,0.25,0.25,0.5,0,0.25,0.5,0.5,1,0,0],[0.125,0.125,0.5,0.125,0.5,0.5,0.25,0.25,1,0.25,1,1]]

R = range(0,12)
def loop_product(current, array, S,t1,t2,t3,t):
  answer = 0
  if(current == len(array) - 1):   
    for j in R:
      S1=S
      if(gamma[j][1] == 1):
        t1+=1
      if(gamma[j][2] == 1):
        t1+=1
      if(gamma[j][1] == 2):
        t2+=1
      if(gamma[j][2] == 2):
        t2+=1
      if(gamma[j][1] == 3):
        t3+=1
      if(gamma[j][2] == 3):
        t3+=1
      t+= gamma[j][3]
      S1*=cdval[array[current]][j]
      l = min(min(t1,t2),t3)
      if(l!=0):
        t1=t1%l
        t2=t2%l
        t3=t3%l
      S1*= 1.07457**t
      S1*= 1.54701**(t1-t3)
      S1*= 0.895503**len(array)
      if(S1!=0):
        answer+=S1
  if(current < len(array) - 1):
    for j in R:
      if(gamma[j][1] == 1):
        t1+=1
      if(gamma[j][2] == 1):
        t1+=1
      if(gamma[j][1] == 2):
        t2+=1
      if(gamma[j][2] == 2):
        t2+=1
      if(gamma[j][1] == 3):
        t3+=1
      if(gamma[j][2] == 3):
        t3+=1
      t+= gamma[j][3]
      S*=cdval[array[current]][j]
      answer += loop_product(current+1, array, S,t1,t2,t3,t)
  return answer
for k in range(0, 4096):
  print k, loop_product(1,subsets[k],1,0,0,0,0)
