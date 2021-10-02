""" def closest(lst, K):
      
    return lst[min(range(len(lst)), key = lambda i: abs(lst[i]-K))]
      
      
lst = [3.64, 5.2, 9.42, 9.35, 8.5, 8]
K = 4.2
print(closest(lst, K)) """
