# https://edabit.com/challenge/7vN8ZRw43yuWNoy3Y

import re

def parse_code(str):
    dic = {} 
    list = re.sub("(?:0)+", "/", str).replace(" ", "").split("/")
    dic['first_name'] = list[0]
    dic['last_name'] = list[1]
    dic['id'] = list[2]
    return dic

print(parse_code("John000Doe000123"))