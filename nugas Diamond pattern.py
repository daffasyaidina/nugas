diamond = int(input("height "))

for i in range(diamond):
    print(" " * (diamond - i), "*" * (i * 2 + 1))
for i in range(diamond - 2, -1, -1):
    print(" " * (diamond - i), "*" * (i * 2 + 1))