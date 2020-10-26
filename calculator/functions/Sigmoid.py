# Sigmoid.py

from math import exp

def sigmoid(arg):
    result = 1/(1+exp(-arg))
    return print(f'{result}')

def dif_sigmoid(arg):
    
    def sigmoid(arg):
        return 1/(1+exp(-arg))

    result =  sigmoid(arg) * (1- sigmoid(arg))
    return print(f'{result}')