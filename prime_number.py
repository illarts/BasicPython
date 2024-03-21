a = input("aの値を入力: ")

a = int(a)

# TODO
def is_prime(n):
    
    for j in range(2, int(n**0.5) + 1):
        if n == 1:
            return False
        if n % j == 0:
            return False
        
    return True

def int_checker(n):
    if (n <= 1) or (type(n) is not int):
        print("Please input int number more than 1")        
    else:
        print(str(a) + 'は素数？',is_prime(a))

int_checker(a)

# https://ictsr4.com/py/m0130.html 
# #5 素数かどうかを判定する関数            