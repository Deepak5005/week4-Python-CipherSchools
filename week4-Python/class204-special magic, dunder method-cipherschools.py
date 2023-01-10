# special magic methods / dunder methods
# operator overloading
# polymorphism

class Phone:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price
        
def phone_name(self):
    return f"{self.brand} {self.model}"

# str , repr
def __str__(self):
    return f'{self.band} {self.model}'

def __repr__(self):
    return f'{self.band} {self.model} and price is {self.price}'

# 1 = [1,2,3]
# print(l)
my_phone = Phone('nokia', '1100', 1000)
print(str(my_phone))
print(repr(my_phone))


# operator overloading
# polymorphism

class Phone:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price
        
def phone_name(self):
    return f"{self.brand} {self.model}"

# str , repr
def __str__(self):
    return f'{self.band} {self.model}'

def __repr__(self):
    return f'phone{self.brand}, {self.model}, {self.price}'

def __len__(self):
    return len(self.phone_name())


# 1 = [1,2,3]
# print(l)
my_phone = Phone('nokia', '1100', 1000)
print(str(my_phone))
print(repr(my_phone))
print(my_phone.__repr__())

# def __mul__(self, other):
#      return self.price * other.price

class SmartPhone(Phone):
    def __init__(self, brand, model, price, camera):
        super().__init__(brand,model, price)
        self.camera = camera