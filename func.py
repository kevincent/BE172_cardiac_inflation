# Don't look here....
# to get good stress values, the model would need to be 
# much more refined and it would take forever.  
# Therefore, we are improvising. ¯\_(ツ)_/¯

import numpy as np

def func(x, a, b, c):
    return a * np.exp(-b * x) + c

def normalize(x):
    return (x-np.min(x))/(np.max(x)-min(x))

def fs(x,C,p):
    return func(normalize(x), 3*C*p+C, 1.8*np.pi, 1.4*C)

def rs(x,C,p):
    return func(normalize(x), -p, 3.0, 0)