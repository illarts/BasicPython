a = input("a の値を入力: ")
b = input("b の値を入力: ")

# TODO

a = int(a)
b = int(b)

def euclid(a, b):
    if a < b:
        a, b = b, a
    
    remain = a % b
    
    if remain == 0:
        return b
    else:
        return euclid(b, remain)

print(euclid(a, b))