import unittest

def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
       return 1
    resultado = fibonacci(n-1) + fibonacci(n-2)
    return resultado
    
def TestFibonacci_0(self):
    resultado = fibonacci(0)
    self.assertEqual (resultado,0)
        
def TestFibonacci_1(self):
    resultado = fibonacci(1)
    self.assertEqual (resultado,1)
    
def TestFibonacci_2(self):
    resultado = fibonacci(2)
    self.assertEqual (resultado,1)
    
def TestFibonacci_3(self):
    resultado = fibonacci(3)
    self.assertEqual (resultado,2)
    
def TestFibonacci_4(self):
    resultado = fibonacci(4)
    self.assertEqual (resultado,3)
    
def TestFibonacci_5(self):
    resultado = fibonacci(5)
    self.assertEqual (resultado,5)
    
def TestFibonacci_6(self):
    resultado = fibonacci(6)
    self.assertEqual (resultado,8)
    
def TestFibonacci_7(self):
    resultado = fibonacci(7)
    self.assertEqual (resultado,13)
    
def TestFibonacci_8(self):
    resultado = fibonacci(8)
    self.assertEqual (resultado,21)

    
unittest.main()