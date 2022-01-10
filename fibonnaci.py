def fibonnaci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        x = 0
        y = 1
        res = 0
        for i in range(2,n+1):
            res = x + y
            x = y 
            y = res
        return res

array = [fibonnaci(3),
         fibonnaci(8),
         fibonnaci(11)]

print(array)