import numpy as np
X=np.array([[1,2],[3,6],[5,10]])

def minmax_scale(X, axis=0, eps=1e-12):
    """
    Scale X to [0,1]. If 2D and axis=0 (default), scale per column.
    Return np.ndarray (float).
    """
    if axis==0:    
        x_max=np.max(X,axis=0,keepdims=True)
        x_min=np.min(X,axis=0,keepdims=True)
        denominator=np.maximum(x_max-x_min,eps)
        result=(X-x_min)/denominator
        return np.array(result)
    else :
        x_max=np.max(X,axis=1,keepdims=True)
        x_min=np.min(X,axis=1,keepdims=True)
        denominator=np.maximum(x_max-x_min,eps)
        result=(X-x_min)/denominator
        return np.array(result)