import math
import os
import random
import re
import sys


n = int(input("Sayi giriniz: "))

if n % 2 == 1:
    print("Weird")
elif (n % 2 == 0)&(n > 20):
    print("Not Weird")
elif (n % 2 == 0)&(n > 6):
    print("Weird")
elif (n % 2 == 0)&(n > 2):
    print("Not Weird")