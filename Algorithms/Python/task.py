""" lst=[8, 2, 3, 0, 7]

cem=0

for x in lst:
    cem+=x
print(cem) """

#//////////////////////////////////////////////////////////////////////  

''' import time
import datetime

print("Weekday of the week: ", datetime.date.today().strftime("%w")) '''

#//////////////////////////////////////////////////////////////////////  

''' n=input("eded: ")
n=int(n)

for i in range(2,int(n/2)+1):
    if i**2==n:
        print(i)
        break
    
else:
    print("NO") '''

#//////////////////////////////////////////////////////////////////////  


''' x=int(input("eded: "))

for n in range(x):
    print(n) '''

#//////////////////////////////////////////////////////////////////////  


''' def lastElement(myList):
    if myList:
        return f" son element: {myList[-1]} , say: {len(myList)}"
    
print(lastElement([5,6,7])) '''

#//////////////////////////////////////////////////////////////////////  

""" def SumOfElements(myList):
    sum = 0
    for x in myList:
        sum = sum + x

    return sum """

#//////////////////////////////////////////////////////////////////////  


''' def closest(lst, K):
      
    return lst[min(range(len(lst)), key = lambda i: abs(lst[i]-K))]
      
      
lst = [3.64, 5.2, 9.42, 9.35, 8.5, 8]
K = 6
print(closest(lst, K))
'''

#//////////////////////////////////////////////////////////////////////  
