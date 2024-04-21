
import unittest



def buscar_datos(database,*args,**kwargs):
  for key, value in database.items():
    if all(item in value for item in args) and all(value[k] == v for k, v in kwargs.items()):
      return key 
  return None
    

    
 
database = {
  "persona1":{
  
  "nombre1":"pablo",
  "nombre2":"diego",
  "apellido1":"ruiz",
  "apellido2":"picasso",
      },
  
  "persona2":{
    
  "nombre1":"candela",
  "apellido1":"gonzalez",
  "apellido2":"privitera",
  },
    
  "persona3":{
    
  "nombre1":"melina",
  "nombre2":"abril",
  "apellido1":"torres",
  "apellido2":"gomez",
    
  },
    
    
    }
    
    
def buscar_datos(self):
  resultado = buscar_datos(self.database,apellido1="ruiz")
  self.assertEqual(resultado, "persona1")
  
def buscar_datos(self):
  resultado = buscar_datos(self.database,apellido2="picasso")
  self.assertEqual(resultado, "persona1")
  
def buscar_datos(self):
  resultado = buscar_datos(self.database,nombre1="pablo")
  self.assertEqual(resultado, "persona1")
  
def buscar_datos(self):
  resultado = buscar_datos(self.database,apellido1="ruiz")
  self.assertEqual(resultado, "persona1")
  
def buscar_datos(self):
  resultado = buscar_datos(self.database,nombre1="melina")
  self.assertEqual(resultado, "persona3")
  
def buscar_datos(self):
  resultado = buscar_datos(self.database,apellido1="torres")
  self.assertEqual(resultado, "persona3")
  
def buscar_datos(self):
  resultado = buscar_datos(self.database,apellido2="privitera")
  self.assertEqual(resultado, "persona2")
  
def buscar_datos(self):
  resultado = buscar_datos(self.database,nombre1="candela")
  self.assertEqual(resultado, "persona2")
  
  
  
    
    
unittest.main()
    
    
    
    
    
    
    
    
    
    
    