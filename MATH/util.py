from math import modf

def to_base(val:int|float, base:int)->str:
    integral, fractional = modf(val)
    int_output=''
    while(integral > 0):
        integral, remainder = (integral//base,integral%base)
        int_output+=remainder
        
    if fractional:
        pass

def find_bounds(v,s):
    expr = (10**-s)/2
    bounds = (-v*(expr-1),v*(expr+1)) # (lower bound , upper bound)
    return(bounds)

def abs(val):
    return (-val if val < 0 else val)

def err_abs(actual, approx):
    return abs(actual - approx)

def err_rel(actual, approx):
    return err_abs(actual, approx)/abs(actual)


def main():
    print(f'{find_bounds(500,3)}')
    print(f'{err_rel(15000000, 15500000)}')

if __name__ == '__main__':
    main()