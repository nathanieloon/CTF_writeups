from itertools import chain

from sympy import isprime

in_val = [
    106,
    119,
    113,
    119,
    49,
    74,
    172,
    242,
    216,
    208,
    339,
    264,
    344,
    267,
    743,
    660,
    893,
    892,
    1007,
    975,
    10319,
    10550,
    10504,
    11342,
    11503,
    12533,
    12741,
    12833,
    13437,
    13926,
    13893,
    14450,
    14832,
    15417,
    15505,
    16094,
    16285,
    16599,
    16758,
    17488,
]

in_val2 = [
    93766,
    93969, 
    94440,
    94669,
    94952,
    94865,
    95934,
    96354,
    96443,
    96815,
    97280,
    97604,
    97850,
    98426,
]

in_val3 = [
    9916239,
    9918082,
    9919154,
    9921394,
    9923213,
    9926376,
    9927388,
    9931494,
    9932289,
    9935427,
    9938304,
    9957564,
    9965794,
    9978842,
    9980815,
    9981858,
    9989997,
    100030045,
    100049982,
    100059926,
    100111100,
    100131019,
    100160922,
    100404094,
    100656111,
    100707036,
    100767085,
    100887990,
    100998966,
    101030055,
    101060206,
    101141058,
]

A002385 = sorted((n for n in chain((int(str(x)+str(x)[::-1]) for x in range(1, 10**5)), (int(str(x)+str(x)[-2::-1]) for x in range(1, 10**5))) if isprime(n))) # Chai Wah Wu, Aug 16 2014

offset = 765 - 1
initial_num = A002385[offset]

i = 0
for val in in_val3:
    chr_val = in_val3[i]^A002385[offset]
    print("in:", in_val3[i], "\tkey:", A002385[offset], "\tchr:", chr_val, "\tout:", chr(chr_val))

    i += 1
    offset += 1

# def is_prime(num):
#     if num > 1:
#         for i in range(2,num):
#             if (num % i) == 0:
#                 return False
#         else:
#             return True
#     else:
#         return False

# def is_palindrome(num):
#     if str(num) == str(num)[::-1]:
#         return True
#     else:
#         return False

# initial_num = 2
# num = initial_num
# i = 0
# while i < len(in_val):

#     found = False
#     while not found:
#         if is_prime(num):
#             if is_palindrome(num):
#                 chr_val = in_val[i]^num
#                 print("\tin:", in_val[i], "\tkey:", num, "\tchr:", chr_val, "\tout:", chr(chr_val))
#                 found = True
#         num += 1
#     i += 1