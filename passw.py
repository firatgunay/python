
import random
import string


LETTERS = string.ascii_letters
NUMS = '0123456789'
SPE = '-+*%&!_$'
SYMBOLS = LETTERS + NUMS + SPE
len = int(input("enter password lenght :"))
password = "" .join(random.sample(SYMBOLS , len))
print(password)
