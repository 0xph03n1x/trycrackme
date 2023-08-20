import string
alphabet = list(string.ascii_lowercase)
#alphabet = list(string.ascii_uppercase)

import itertools

password= bytes.fromhex("3a2a2e1e3659113a5f1a3c335d1b1a3a2d590d031b5b064413")
your_input = "****" # hint: (4 characters)
data_set_1 = alphabet
data_set_2 = alphabet
data_set_3 = alphabet
data_set_4 = alphabet
data_set_5 = alphabet
data_set_6 = alphabet

for permutation in itertools.product(data_set_1, data_set_2, data_set_3, data_set_4, data_set_5, data_set_6):
    print(permutation)
    your_input = permutation
    if(len(your_input) == 6):
     if ((128 & ord(your_input[0])) == False):
      if (16 & ord(your_input[3])== False):
       if ((32 & ord(your_input[0])) == False):
        if (8 & ord(your_input[3])== False):
         if ((128 & ord(your_input[2])) == False):
          if ((32 & ord(your_input[4]))== False):
           if ((32 & ord(your_input[5]))== False):
            if ((4 & ord(your_input[0])) == False):
             if ((128 & ord(your_input[5])) == False):
              if ((2 & ord(your_input[0])) == False):
               if ((128 & ord(your_input[4])) == False):
                if ((1 & ord(your_input[0])) == False):
                 if ((1 & ord(your_input[3])) == False):
                  if ((128 & ord(your_input[3])) == False):
                   if (8 & ord(your_input[5])== False):
                    if ((128 & ord(your_input[1])) == False):
                     if (16 & ord(your_input[1])== False):
                      if (8 & ord(your_input[4])== False):
                       if ((32 & ord(your_input[3]))== False):
                        if ((4 & ord(your_input[1])) == False):
                         if ((1 & ord(your_input[2])) == False):
                          if ((1 & ord(your_input[1])) == False):
                           if (16 & ord(your_input[2])== False):
                            if ((4 & ord(your_input[3]))== False):
                             if ((32 & ord(your_input[2]))== False):
                              if ((1 & ord(your_input[4])) == False):
                               if ((1 & ord(your_input[5]))):
                                if ((4 & ord(your_input[2]))):
                                 if ((2 & ord(your_input[4]))):
                                  if (64 & ord(your_input[5])):
                                   if ((2 & ord(your_input[1]))):
                                    if (16 & ord(your_input[4])):
                                     if (64 & ord(your_input[1])):
                                      if (64 & ord(your_input[3])):
                                       if (8 & ord(your_input[1])):
                                        if (64 & ord(your_input[0])):
                                         if ((2 & ord(your_input[5]))):
                                          if (16 & ord(your_input[0])):
                                           if (64 & ord(your_input[2])):
                                            if ((2 & ord(your_input[3]))):
                                             if ((4 & ord(your_input[5]))):
                                              if ((32 & ord(your_input[1]))):
                                               if (64 & ord(your_input[4])):
                                                if (8 & ord(your_input[0])):
                                                 if ((2 & ord(your_input[2]))):
                                                  if (8 & ord(your_input[2])):
                                                   if (16 & ord(your_input[5])):
                                                    if ((4 & ord(your_input[4]))):
                                                     print(your_input)
                                                     exit("Good Job!")
    print("", end="\r")