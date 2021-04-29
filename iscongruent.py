def iscongruent(a,b,n):
    """ a and b are congruent modulo n only if the absolute difference of both divides n"""
    return (abs(a-b) // n )  == 0

if __name__ == "__main__":
    print(iscongruent(4,6,12))
    print(iscongruent(5,12,60))

