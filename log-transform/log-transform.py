import math
values =[1,2,3,4]
def log_transform(values):
    """
    Apply the log1p transformation to each value.
    """
    # Write code here
    values=np.asarray(values,dtype=float)
    return [math.log1p(v) for v in values] 