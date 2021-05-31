 
def distance(str1, str2, m, n):
    if m == 0:
        return n
    if n == 0:
        return m
    if str1[m-1] == str2[n-1]:
        return distance(str1, str2, m-1, n-1)
    return 1 + min(distance(str1, str2, m, n-1),   
                   distance(str1, str2, m-1, n), 
                   distance(str1, str2, m-1, n-1)
                   )
str1 = str(input("enter 1st string"))
str2 = str(input("enter 2nd string"))
print(distance(str1, str2, len(str1), len(str2)))
 