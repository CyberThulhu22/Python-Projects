#!/usr/lib/env python3

# ------------------------------------------------------------- #
# Validates that a pin is 4 or 6 digits long
def validate_pin(pin):
    return len(pin) in (4, 6) and pin.isdigit()

""" # This was my code to the above: 
def validate_pin(pin):
    if pin.isdigit():
        if len(pin) is 4 or len(pin) is 6:
            return True
        else:
            return False
    else:
        return False
"""

# ------------------------------------------------------------- #
# Gets the middle letter out of a string

def get_middle(s):
    return s[(len(s)-1)//2:len(s)//2+1]

"""# This was my code to the above:
def get_middle(s):
    if len(s)%2 == 0:
        return s[len(s)//2-1:len(s)//2+1]
    else:
        return s[len(s)//2]
"""
# ------------------------------------------------------------- #
# This is to capitalize each word in a sentence
def toJadenCase(string):        
    return " ".join(w.capitalize() for w in string.split())

"""# This was my code to the above:
def toJadenCase(string):
    jaden_case = []
    for word in string.split():
        jaden_case.append(word[0].upper() + word[1:])
    return " ".join(jaden_case)
"""

# ------------------------------------------------------------- #
# Code to translate DNA
def DNA_strand(dna):
    return dna.translate(str.maketrans("ATCG","TAGC"))

""" This is my code
def DNA_strand(dna):
    rplace = {'A':'T','T':'A','C':'G','G':'C'}
    return ''.join([rplace.get(c, c) for c in dna])
"""

# ------------------------------------------------------------- #
# Code to convert into phone number
def create_phone_number(n):
    return "({}{}{}) {}{}{}-{}{}{}{}".format(*n)

"""
def create_phone_number(n):
    n = ''.join([str(e) for e in n])
    return f"({n[0:3]}) {n[3:6]}-{n[6:]}"
"""

# ------------------------------------------------------------- #
# Masking
def maskify(cc):
    return "#"*(len(cc)-4) + cc[-4:]

""" My code 
def maskify(cc):
    return "#"*(len(cc)-4) + cc[-4:]
"""

# ------------------------------------------------------------- #

def friend(x):
    return[].append([str(i)is])

# ------------------------------------------------------------- #

def find_missing(sequence):
    t = sequence
    return (t[0] + t[-1]) * (len(t) + 1) / 2 - sum(t)

# ------------------------------------------------------------- #