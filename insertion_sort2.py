#improved insertion sort

def insertion_sort2(my_list):
    for index in range(1,len(my_list)):
        value = my_list[index]
        i = index - 1
        while i>=0 and (value < my_list[i]):
            my_list[i+1] = my_list[i] #shift number in slot i right to slot i+1
            my_list[i] = value # shift value left int slot i
            i = i - 1


