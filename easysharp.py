flag = "144260662546426066"
solved = ''
# split the string on every second character
flag_list = [flag[i:i+2] for i in range(0, len(flag), 2)]
# for every item in the list, convert it from string to int, add 55, pass to chr() and concatanate to the `solved` string
for i in flag_list:
    solved += chr(int(i) + 55)
print(solved)