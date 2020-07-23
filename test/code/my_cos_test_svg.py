import sys
import math

sys.path.append(__file__ + '/../../../')
import my_math

print("<!--ver:0.0-->") # このテストのバージョン
print("<!--my_math.cos()をSVGでプロット-->") # このテストの説明文

scale = 50
width = 600
height = 150
print('<svg width="{}" height="{}" xmlns="http://www.w3.org/2000/svg">'.format(width, height))

# 背景を塗りつぶし
print('<rect x="0" y="0" width="{}" height="{}" fill="white"/>'.format(width, height))

# 座標を画面上の位置に変換
def convert_x(x):
    return width / 2 + x * scale
def convert_y(y):
    return height / 2 + y * -scale

# 点を打つ
def plot(x, y):
    print('<circle cx="{}" cy="{}" r="1" fill="lightsteelblue"/>'.format(convert_x(x), convert_y(y)));


# 目盛り
for y in range(-1, 2):
    print('<rect x="0" y="{}" width="{}" height="0.0001" stroke="lavender" stroke-width="0.5"/>'.format(convert_y(y), width ))
    
for x in range(-7, 8):
    print('<rect x="{}" y="0" width="0.0001" height="{}" stroke="lavender" stroke-width="0.5"/>'.format(convert_x(x), height))

# 縦軸/横軸
print('<rect x="0" y="{}" width="{}" height="0.0001" stroke="lightgray"/>'.format(height / 2, width))
print('<rect x="{}" y="0" width="0.0001" height="{}" stroke="lightgray"/>'.format(width / 2, height))

# cos をプロット
resolution = 40
for i in range(-6 * resolution, 6 * resolution):
    t = i / resolution
    plot(t, my_math.cos(math.pi * t))

print("</svg>")
