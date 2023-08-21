your_input = "TryXorMeIfYouCan"

arr = [23,49,58,27,44,49,14,38,10,37,26,44,54,0,34,45]
c = 0

# X = 88
# o = 111
# r = 114
test = ""

for i in range(0, 255):
    for j in range(len(arr)):
        test += (chr(i ^ arr[j]))
    if "Xor" in test:
        print(f"Correct result is: {test}")
    test = ""

if len(your_input) != 16 or "Xor" not in your_input:
    exit("Wrong Input")

for i in your_input:
    check = ord(i) ^ ord(your_input[13])
    if(check == arr[c]):
        print("Good Job!")
    else:
        exit("Wrong Answer")

    c += 1

