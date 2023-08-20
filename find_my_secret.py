import base64

your_input = "OCwmMDYnMCE="

def decode(x):
    decoded = base64.b64decode(x)
    decoded = decoded.decode("utf-8")
    
    password = ""
    for c in decoded:
        password += chr(ord(c) ^ 0x55)
    
    return password

def flag(x):

    password = ""
    for c in x:
        password += chr(ord(c) ^ 0x55)
    
    flag_bytes = password.encode('utf-8')
    flag = base64.b64encode(flag_bytes)
    print(password)
    print(flag)

try:
   if decode(your_input) == "mysecret":
       print("Good Job!")
   else:
      print("Wrong password")
except:
   print("Please enter correct Base64 data")

flag("mysecret")