def count(a, b):
    last = b[len(b)-1]
    res = 0
    for i in a:
        if i == last:
            res +=1
    return res

a = input()
b = input()
print(count(a, b))

