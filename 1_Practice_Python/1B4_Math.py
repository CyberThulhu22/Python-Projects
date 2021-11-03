#!/usr/bin/env python3

#!!!# NEED TO FINISH MEAN FUNCTION #!!!#

#from math import pi, sqrt

# Robust function for simple addition for multiple numbers
def addition(*args):
    add_list = [*args]
    add_length = len(add_list)
    add_firstnum = add_list[0]
    if add_length <= 1:
        print("Please provide more numbers to add together")
        return None
    for num in add_list[1:]:
        if type(num) != int:
            try:
                add_firstnum += int(num)
            except ValueError:
                continue
        else:
            add_firstnum += int(num)
    return add_firstnum


# Robust function for simple subtraction for multiple numbers
def subtraction(*args):
    sub_list = [*args]
    sub_length = len(sub_list)
    sub_firstnum = sub_list[0]
    if sub_length <= 1:
        print("Please provide more numbers to subtract from")
        return None
    for num in sub_list[1:]:
        if type(num) != int:
            try:
                sub_firstnum -= int(num)
            except ValueError:
                continue
        else:
            sub_firstnum -= int(num)
    return sub_firstnum


# Robust function for simple multiplication of multiple numbers
def multiplication(*args):
    multi_list = [*args]
    multi_length = len(multi_list)
    multi_firstnum = multi_list[0]
    if multi_length <= 1:
        print("Please provide more numbers to multiply together")
        return None
    for num in multi_list[1:]:
        if type(num) != int:
            try:
                multi_firstnum *= int(num)
            except ValueError:
                continue
        else:
            multi_firstnum *= int(num)
    return multi_firstnum


# Robust function for simple floor division for multiple numbers
def floor_division(*args):
    fdiv_list = [*args]
    fdiv_length = len(fdiv_list)
    fdiv_firstnum = fdiv_list[0]
    if fdiv_length <= 1:
        print("Please provide more numbers to do floor division with")
        return None
    for num in fdiv_list[1:]:
        if type(num) != int:
            try:
                fdiv_firstnum //= int(num)
            except ValueError:
                continue
        else:
            fdiv_firstnum //= int(num)
    return fdiv_firstnum


# Robust function for simple float division for multiple numbers
def float_division(*args):
    fldiv_list = [*args]
    fldiv_length = len(fldiv_list)
    fldiv_firstnum = fldiv_list[0]
    if fldiv_length <= 1:
        print("Please provide more numbers to do float division with")
        return None
    for num in fldiv_list[1:]:
        if type(num) != float:
            try:
                fldiv_firstnum /= float(num)
            except ValueError:
                continue
        else:
            fldiv_firstnum /= float(num)
    return fldiv_firstnum

## NEED TO FINISH MEAN FUNCTION
def math_mean(*args):
    mean_list = [*args]
    mean_length = len(mean_list)
    if mean_length < 1:
        print("Please provide more numbers to find the mean")
        return None
    elif mean_length is 1:
        return None
## NEED TO FINISH MEAN FUNCTION


def math_median(*args):
    return None


def math_mode(*args):
    return None


### BELOW IS POSSIBLE MATH FUNCTIONS TO CREATE IN THE FUTURE
# Calculate the probability or percentage
def math_probability():
    return None


# Quadratic formula?
def math_quad_form():
    return None


# Distance Formula?
def math_distance(x,y):
    return None


# Slope Formulat Angle:
def math_slope():
    return None


# Area of a Triangle
def math_area_triangle():
    return None

# Pythagorean Theorem= a**2 + b**2 = c**2
def pythagorean():
    return None