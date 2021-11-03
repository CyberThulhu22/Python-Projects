def boxy(number):
    my_list = []
    my_list.append("X" * number)
    for ea in range(0,(number-2)):
        my_list.append("X" + ' '*(number - 2) + "X")
    my_list.append("X" * number)
    return my_list



def unique(lst):
    #for ea in lst:
    #   if lst.count(ea) is 1:
    return (ea for ea in lst if lst.count(ea) is 1)

print(unique([1,1,1,1,1,1,1,14,1,1,1,1]))

