a = input("aの値を入力: ")
b = input("bの値を入力: ")

# TODO

def is_prime(i):
    if i <= 1:
        return False
    for j in range(2, int(i**0.5) + 1):
        if i % j == 0:
            return False
    return True

print(str(a) + 'は素数？',is_prime(int(a)))
print(str(b) + 'は素数？',is_prime(int(b)))

# https://ictsr4.com/py/m0130.html 
# #5 素数かどうかを判定する関数