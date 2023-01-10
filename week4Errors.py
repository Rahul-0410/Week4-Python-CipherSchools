def add(a,b):
    if (type(a) is int) and (type(b) is int):
        return a+b
    raise TypeError('OOPs!! you are passing the wrong data type in function') 
print(add(2,3))
print(add('2','3'))

# Example 1
class Animal:
    def __init__(self,name):
        self.name=name

    def sound(self):
        raise NotImplementedError('you have to define this in subclass')

class Dog(Animal):
    def __init__(self,name,breed):
        super().__init__(name)
        self.breed=breed
    def sound(self):
        return 'bhow bhow'
class Cat(Animal):
    def __init__(self,name,breed):
        super().__init__(name)
        self.breed = breed
    def sound(self):
        return 'meow meow'
doggy=Dog('bonny','dog')
print(doggy.sound())

# Example 2
class Mobile:
    def __init__(self,name):
        self.name=name 

class MObileStore:
    def __init__(self):
        self.mobiles=[]

    def add_mobiles(self,new_mobile):
        if isinstance(new_mobile,Mobile):
            self.mobiles.append(new_mobile)
        else:
            raise TypeError('new mobile should be object of Mobile class')

mobile1=Mobile('one plus 6')
mobile2='samsung galaxy s10'
mobostore=MObileStore()
# print(mobostore.mobiles)
# mobostore.add_mobiles(mobile2)
mobostore.add_mobiles(mobile1)
mobo=mobostore.mobiles
print(mobo[0].name)

# Try , Except : exception handling, python
while True:
    try:
        age=int(input('enter your age: '))
        break
    except ValueError:
        print('maybe you entered string instead of number')
    except:
        print('unexpected error...')

if age<18:
    print('You can\'t play this game')
else:
    print('you can play this game')

#  Else finally with try except in Python
while True:
    try:
        number=int(input('enter a number : '))
    except ValueError:
        print("You didn\'t entered an integer")
    except:
        print('unexpected error...')
    else:
        print(f'user input= {number}')
        break
    finally:
        print('finally blocks.....')

# Excercise1
def div(a,b):
    try:
        return a/b       
    except ZeroDivisionError:
            print('Please don\'t divide by zero')
    except ValueError:
            print('Please input integers only')
    except TypeError as err:
        print(err)
    
# num1=int(input("Enter numerator: "))
# num2=int(input("Enter denominator: "))
print(div(4,'0'))

#custom exception
class NameTooShortError(ValueError):
    pass
def validate(name):
    if len(name)<8:
        raise NameTooShortError('name is short')
        # raise ValueError('name is short')

username=input("Enter your name:")
validate(username)
print(f'hello {username}')

# Python Debugger
import pdb
pdb.set_trace()
name=input('Please type your name:')
age=int(input('Please enter your age:'))
print(f"hello {name} your age is {age}")
age2=age+5
print(f"{name} you will be {age2} in next five years")
# l for line
# c for continue 
# n for next line 






