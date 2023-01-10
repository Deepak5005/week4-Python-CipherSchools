# raise errors example 1
# NotImpletedError
# abstract method

class Animal:
    def __init__(self,name):
        self.name = name
        
    def sound(self):
        return 'meao meao'
    
class Dog(Animal):
    def __init__(self,name,breed):
        super().__init__(name)
        self.breed = breed
        
class Cat(Animal):
    def __init__(self,name,breed):
        super().__init__(name)
        self.breed = breed
        
doggy = Dog('boony','pug')
print(doggy.sound())

# NotImplementedError

class Animal:
    def __init__(self,name):
        self.name = name
        
    def sound(self):
      raise NotImplementedError('you have to define this method in subclasses')
    
class Dog(Animal):
    def __init__(self,name,breed):
        super().__init__(name)
        self.breed = breed
        
    def sound(self):
        return 'bhow bhow'
        
class Cat(Animal):
    def __init__(self,name,breed):
        super().__init__(name)
        self.breed = breed
        
    def sound(self):
        return 'meao meao'
        
doggy = Dog('boony','pug')
print(doggy.sound())