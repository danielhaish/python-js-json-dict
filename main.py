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
