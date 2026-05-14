import numpy as np

def dot_product(x, y):
    """
    Compute the dot product of two 1D arrays x and y.
    Must return a float.
    """
    x,y=np.array(x),np.array(y)
    if len(x)==len(y):
        return np.dot(x,y)
    else :
        raise ValueError("not considered")
    # Write code here
    