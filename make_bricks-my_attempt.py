def make_bricks(small, big, goal):
    big = 5 * big
    # take into account the rounding! need to be able to make exactly, 
    # even if over
    remain = goal % 5
    if small >= remain:
        return True
        if remain > big:
            if 
            return True
    
    
    if big == 0:
        #if there are no bigs, we can't use them
        if small >= goal:
            return True
        else:
            return False
    else:
        remain = goal % big
        if small >= remain:
            return True
        else:
            return False
