# python-js-json-dict
It simple python class that allows you to load python dict and access it like js object so you can set value and access value using dotsq
So you could enjoy the nice sntax of js and the pyhton syntax 
I would write alot of tests to make sure it work proparly to avoid bugs
plese fill free to send pull requests and ask for more features 

usment example:
```
bob = JsJson({"x": {'d':{'c': 20}}})
boby = JsJson({"x": {'d':{'c': 20}}, 'y':2})
bob.x.d.c = 30
print(bob.x)
print(boby)
print(boby == bob)
print(bob.x.d.c == 30)
x = boby['x']['d']['c']
for i in boby:
    print(i)
```
output
```
{'d': {'c': 30}}
{'x': {'d': {'c': 20}}, 'y': 2}
False
True
x
y

```
