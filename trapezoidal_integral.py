from math import sin
import math
# --example--
# print(sin(0))
# >>> 0
# -----------

a = 0
b = math.pi / 2
N = 100
h = (b - a) / N
k = 1
S = 0

while k <= N:

    # 合計を算出
    S += h / 2 * (sin(a + (k - 1) * h) + sin(a + k * h))

    # インクリメント処理
    k += 1

print(S)

# https://anotools.com/python/1116/