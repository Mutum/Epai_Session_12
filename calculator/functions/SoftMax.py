# softmax.py
import numpy as np

def softmax(x):
    """Compute softmax values for each sets of scores in x."""
    result =  np.exp(x) / np.sum(np.exp(x), axis=0) 
    return print(f'{result}')