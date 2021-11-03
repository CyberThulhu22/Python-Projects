#!/bin/python

def mode( *args ):
    lst = list( args )
    n = len( lst )
    if n < 1:
        return None
    else:
        return sum(lst[:])/n


def median( *args ):
    lst = list( args )
    n = len( lst )
    if  n < 1:
        return None
    elif  n % 2 == 1:
        return sorted(lst)[n//2]
    else:
        return sum( sorted( lst )[ n//2-1 : n//2+1 ])/2.0 


def addition ( *args ):
    lst = list(args)
    start = lst[0]
    for each in lst[1:]:
        if each == str(each):
            continue
        else:
            start += each
    return start


def subtraction ( *args ):
    lst = list(args)
    start = lst[0]
    for each in lst[1:]:
        if each == str(each):
            continue
        else:
            start -= each
    return start


def multiplication ( *args ):
    lst = list(args)
    start = lst[0]
    for each in lst[1:]:
        if each == str(each):
            continue
        else:
            start *= each
    return start


def division ( *args ):
    lst = list(args)
    start = lst[0]
    for each in lst[1:]:
        if each == str(each):
            continue
        else:
            start //= each
    return start
