your_input = ""

arr = [23,49,58,27,44,49,14,38,10,37,26,44,54,0,34,45]
c = 0

# X = 88
# o = 111
# r = 114
flag = ""

for i in range(0, 255):
    for j in range(len(arr)):
        flag += (chr(i ^ arr[j]))
    print(flag)
    if "Xor" in flag:
        print(f"Correct result is: {flag}")
        break
    flag = ""

if len(your_input) != 16 or "Xor" not in your_input:
    exit("Wrong Input")

for i in your_input:
    check = ord(i) ^ ord(your_input[13])
    if(check == arr[c]):
        print("Good Job!")
    else:
        exit("Wrong Answer")

    c += 1

