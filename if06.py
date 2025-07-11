a=-3
b=1
c=9
def main(a,b,c):
    x=0
    y=0
    if a>0:
        x=x+1
    if a<0:
        y=y+1
    if b>0:
        x=x+1
    if b<0:
        y=y+1
    if c>0:
        x=x+1
    if c<0:
        y=y+1
    if x>y:
        return("there are many positive numbers")
    if x<y:
        return("there are many negative numbers")
    """
    Find how many positive and how many negative numbers there are in the given numbers.
    check the following conditions:
    "there are a lot of positive numbers",
    "there are a lot of negative numbers"

    Args:
        a: first number
        b: second number
        c: third number

    Returns:
        string: string with the result
    """
    return x,y
print(main(a,b,c))