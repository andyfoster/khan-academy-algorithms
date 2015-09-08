a = [6, 45, 2, 78, 23, 12, 2]

def sort(seq):
    for n in range(1, len(seq)):
        item = seq[n]
        print('item is ', item)
        hole = n
        print('hole is ', hole)
        while hole > 0 and seq[hole - 1] > item:
            seq[hole] = seq[hole - 1]
            hole = hole - 1
        seq[hole] = item
        print(' ')
    return seq
