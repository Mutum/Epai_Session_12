# ReLU.py

def relu(x):
    return print(f'{max(0,x)}')

def dif_relu(x):
    
    if type(x) == float or type(x) == int :
        
        if x < 0:
            return 0
        elif x > 0:
            return 1
        else:
            return 0
    else:
              
        raise ValueError('Input float or int')