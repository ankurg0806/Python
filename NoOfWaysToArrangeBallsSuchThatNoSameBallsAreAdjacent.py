# Number of Ways to arrange Balls such that adjacent balls are of different types
# There are ‘p’ balls of type P, ‘q’ balls of type Q and ‘r’ balls of type R and 's' balls of type S. Using the balls we want to create a straight line such that no two balls of same type are adjacent.

def helper(a,b,c,d,last):
    mydict = {}
    if a <0 or b<0 or c<0 or d<0:
        return 0
    if a is 1 and b is 0 and c is 0 and d is 0 and last is 1:
        return 1
    if a is 0 and b is 1 and c is 0 and d is 0 and last is 2:
        return 1
    if a is 0 and b is 0 and c is 1 and d is 0 and last is 3:
        return 1
    if a is 0 and b is 0 and c is 0 and d is 1 and last is 4:
        return 1
    if (a,b,c,d,last) in mydict:
        return mydict[(a,b,c,d,last)]
    else:
        if last == 1:
            mydict[(a,b,c,d,last)] = helper(a-1,b,c,d,2) + helper(a-1,b,c,d,3) + helper(a-1,b,c,d,4)
        elif last == 2:
            mydict[(a,b,c,d,last)] = helper(a,b-1,c,d,1) + helper(a,b-1,c,d,3) + helper(a,b-1,c,d,4)
        elif last == 3:
            mydict[(a,b,c,d,last)] = helper(a,b,c-1,d,1) + helper(a,b,c-1,d,2) + helper(a,b,c-1,d,4)
        elif last == 4:
           mydict[(a,b,c,d,last)] = helper(a,b,c,d-1,1) + helper(a,b,c,d-1,2) + helper(a,b,c,d-1,3)
    return mydict[(a,b,c,d,last)]
def mymeth(a,b,c,d):
    sum = helper(a,b,c,d,1)+helper(a,b,c,d,2)+helper(a,b,c,d,3)+helper(a,b,c,d,4)
    return sum

a ,b, c, d = input().split()
print(mymeth(int(a),int(b),int(c),int(d)))