# RANDOM PASSWORD GENERATOR

import random


lower= "abcdefghijklmnopqrstuvwxyz"
upper= "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
number= "0123456789"
symbols= "!@#$%^&*()_+"
all= lower + upper + number + symbols
lenght=20
temp= random.sample(all,lenght)
password= "  " . join(temp)
print(" MY PASSWORD IS :  " ,password)