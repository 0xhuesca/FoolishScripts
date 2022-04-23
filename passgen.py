
# Password Generator
# Author: Armando Huesca - https://0xhuesca.com

import string
import random

lenght = int(input("Please enter the lenght of the password: "))
select=[0, 1, 2]
def _generator(A):
    passwd=""
    mylist= [string.ascii_letters, string.punctuation, string.digits]
    for i in range(A):
        passwd+=random.choice(mylist[random.choice(range(len(mylist)))]) 
    return passwd

print("The password is: " + str(_generator(lenght)))
