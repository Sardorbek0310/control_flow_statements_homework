a=-2
b=-9
c=-1
def main(a,b,c):
    x=0
    if a<0:
        x=x+1
    if b<0:
        x=x+1
    if c<0:
        x=x+1
    """
    Find number of negative numbers there are in the given numbers.
    Args:
        a: integer
        b: integer
        c: integer
    returns:
        integer: the number of negative numbers in the given numbers
    """
    return x
print (main(a,b,c))