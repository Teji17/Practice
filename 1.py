Python 3.9.7 (tags/v3.9.7:1016ef3, Aug 30 2021, 20:19:38) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> a=5
>>> b=8
>>> print(a+b)
13
>>> a=5
>>> b=6
>>> print(str(a))
5
>>> print(type(a))
<class 'int'>
>>> a=47
>>> b=str(a)
>>> c=a+b
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    c=a+b
TypeError: unsupported operand type(s) for +: 'int' and 'str'
>>> ab='python class'
>>> len(ab)
12
>>> ab[0:13:2]
'pto ls'
>>> print(complex(a))
(47+0j)
>>> a=5
>>> b=4.6
>>> print(float(a))
5.0
>>> print(float(b))
4.6
>>> print(int(a))
5
>>> print(bool(a))
True
>>> a='50'
>>> b=int(a)
>>> print(b)
50
>>> c=a+b
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    c=a+b
TypeError: can only concatenate str (not "int") to str
\
>>> c=90
>>> print(b+c)
140
>>> print(b+c)
140
>>> 
>>> 
>>> a=int(input('enter a number':)
      
SyntaxError: invalid syntax
>>> a=int(input('enter a number:'))
enter a number:5
>>> b=int(input('enter a second number:'))
enter a second number:6
>>> print(a+b)
11
>>> 11
11
>>> 
>>> 
>>> cd=10+5j
>>> str(cd)
'(10+5j)'
>>> c=45
>>> str(c)
'45'
>>> bool(cd)
True
>>> int(cd)
Traceback (most recent call last):
  File "<pyshell#41>", line 1, in <module>
    int(cd)
TypeError: can't convert complex to int
>>> float(cd)
Traceback (most recent call last):
  File "<pyshell#42>", line 1, in <module>
    float(cd)
TypeError: can't convert complex to float
>>> a='Tejinderpal singh'
>>> print(a.casefold())
tejinderpal singh
>>> print(endswidth())
Traceback (most recent call last):
  File "<pyshell#45>", line 1, in <module>
    print(endswidth())
NameError: name 'endswidth' is not defined
>>> print(endswith())
Traceback (most recent call last):
  File "<pyshell#46>", line 1, in <module>
    print(endswith())
NameError: name 'endswith' is not defined
>>> print(endswith('h))
	       
SyntaxError: EOL while scanning string literal
>>> print(endswith('h'))
Traceback (most recent call last):
  File "<pyshell#48>", line 1, in <module>
    print(endswith('h'))
NameError: name 'endswith' is not defined
>>> print(a.endswith('t'))
False
>>> print(a.isdecimal())
False
>>> print(a.lower())
tejinderpal singh
>>> print(a.join())
Traceback (most recent call last):
  File "<pyshell#53>", line 1, in <module>
    print(a.join())
TypeError: str.join() takes exactly one argument (0 given)
>>> print(a.center())
Traceback (most recent call last):
  File "<pyshell#54>", line 1, in <module>
    print(a.center())
TypeError: center expected at least 1 argument, got 0
>>> print(a.center(25,"."))
....Tejinderpal singh....
>>> 