import sys
import math

sys.path.append(__file__ + '/../../../')
import my_math

print("ver:0.0") # このテストのバージョン
print("my_math.cos()の戻り値に対するテスト") # このテストの説明文

resolution = 8
for i in range(-3 * resolution, 3 * resolution):
    t = i / resolution
    print("cos({:<6} * PI): {}".format(t, my_math.cos(math.pi * t)))
