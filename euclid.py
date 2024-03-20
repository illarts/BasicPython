

# TODO

# 問 3. ユークリッドの互除法
# 問 4. 互いに素

a = int(a)
b = int(b)

def euclid(a, b):
    if a < b:
        a, b = b, a
    
    remain = a % b
    
    if remain == 0:
        print("最大公約数は" + str(b))
        return b
    elif remain == 1:
        print(str(a) + "と" + str(b) + "は互いに素である")
        return b
    else:
        return euclid(b, remain)

euclid(a, b)

# extra question

import random
import math

x = []
y = []

not_prime = []
prime = []


def extra(a, b):
    if a < b:
        a, b = b, a
    
    remain = a % b
    
    if remain == 0:
        not_prime.append(a)
    elif remain == 1:
        prime.append(a)
    else:
        return extra(b, remain)

for o in range(0, 100000):
    x = random.randint(1, 10000)
    y = random.randint(1, 10000)
    
    extra(x, y)

t = len(not_prime)
h = len(prime)

if t < h:
    t, h = h, t
    
answer = h / t
example_answer = 6 / math.pi**2


print("1 万以下の 2 つの自然数をランダムに 10 万組生成して、各組が互いに素である確率は" + str(answer))
print("6 / pi**2を少数で表すと" + str(example_answer))