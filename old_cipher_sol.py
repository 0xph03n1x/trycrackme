flag = "cr4ckme"
solution = ""

for c in flag:
    solution += chr(ord(c) - 1)

print(solution)