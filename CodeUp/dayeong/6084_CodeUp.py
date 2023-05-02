h, b, c, s = map(float, input().split())
byte = (h * b * c * s) / 8 / 1024/ 1024
print(format(byte, ".1f"), "MB")
