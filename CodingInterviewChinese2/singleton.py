#!/usr/bin/python
# coding=utf-8  
"""
Source code reference: 
	https://stackoverflow.com/questions/6760685/creating-a-singleton-in-python
"""

def Test(testClass):
	"""a simple test"""
	A = testClass()
	B = testClass()
	A.test = 1
	print(A.test == B.test)
	print(A is B)


### Method 1: A decorator
def singleton_1(class_):
	"""using decoration to make sure only one instance"""
	instances = {}
	def getinstance(*args, **kwargs):
		if class_ not in instances:
			instances[class_] = class_(*args, **kwargs)
		return instances[class_]
	return getinstance

@singleton_1
class Class_1(object):
	pass

Test(Class_1)

### Method 2: A base class
class singleton_2(object):
	_instance = None
	def __new__(class_, *args, **kwargs):
		if not isinstance(class_._instance, class_):
			class_._instance = object.__new__(class_, *args, **kwargs)
		return class_._instance

class Class_2(singleton_2):
	pass
Test(Class_2)

### Method 3: A metaclass
class singleton_3(type):
	""" type是所有元类的父亲。我们可以通过继承type来创建元类 """
	_instances = {}
	def __call__(cls, *args, **kwargs):
		if cls not in cls._instances:
			cls._instances[cls] = super(singleton_3, cls).__call__(*args, **kwargs)
		return cls._instances[cls]

#Python2
class class_3():
	__metaclass__ = singleton_3

Test(class_3)

# #Python3
# class MyClass(BaseClass, metaclass=Singleton):
#     pass