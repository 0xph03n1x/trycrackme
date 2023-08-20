import pwn
import itertools

password= bytes.fromhex("3a2a2e1e3659113a5f1a3c335d1b1a3a2d590d031b5b064413")
your_input = "****" # hint: (4 characters)
data_set_1 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
data_set_2 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
data_set_3 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
data_set_4 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

for permutation in itertools.product(data_set_1, data_set_2, data_set_3, data_set_4):
    print(permutation)
    your_input = permutation

    enc_password = pwn.xor(password, your_input)

    if "TCM{X0r_1s" in str(enc_password):
        print(your_input)
        print(str(enc_password))
        print("Good Job!")
        break
    else:
        continue
