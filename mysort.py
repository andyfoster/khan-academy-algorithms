a = [8, 5, 6, 3, 1]

def my_sort(a):
    i = 1
    for items in a:
        if items[i] > items[i-1]:
            print(items[i], " is > than ", items[i-11])
        i = i+1

my_sort(a)
