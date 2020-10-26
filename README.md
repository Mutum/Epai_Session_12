# Epai_Session_12

Here we build a calculator package with below functions and their derivative
Though functions and their derivatives are written in same module yet their call is split seperately for functions and derivatives.

For functions:
import calculator - this will allow access to all functions not derivations.
from calculator import derivatives - this will give access only to derivations



- Build a calculator package that has separate module for:
sin, cos, tan, tanh, SoftMax, Sigmoid, ReLU, log and e
- The modules shall include their derivatives as well
- If we do import calculator, we should be able to access all the above function (except deviratives)
- For derivates we must do: from package import derivatives. 
- Outputs are returned as well as printed using only f-string

