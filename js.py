
class JsJson(dict):
    def __init__(self, json_data, first_json=None):
        if isinstance(json_data, dict):
            super(JsJson, self).__init__(json_data)
        dict.__setattr__(self, 'json_data', json_data)
        dict.__setattr__(self, 'first_json', first_json)
        dict.__setattr__(self, 'atrs', [])


    def __getattr__(self, item):
        if self.first_json == None:
            dict.__setattr__(self, 'first_json', self)
            self.first_json.atrs.append(item)
        else:
            self.first_json.atrs.append(item)

        return type(self)(self.json_data[item], self.first_json)

    def __eq__(self, js_json_object):
        if isinstance(js_json_object, JsJson):
            return js_json_object.json_data == self.json_data
        return self.json_data == js_json_object

    def __getitem__(self, item):
        if item == None:
            return self.json_data
        return type(self)(self.json_data[item], self.first_json)

    def __setattr__(self, name, value):
        pointer = self.first_json.json_data
        for i in self.first_json.atrs:
            pointer = pointer[i]
        pointer[name] = value
        return self

    def __str__(self):
     return str(self.json_data)

bob = JsJson({"x": {'d':{'c': 20}}})
boby = JsJson({"x": {'d':{'c': 20}}})
bob.x.d.c = 30
print(bob.x)
print(boby)
print(boby == bob)
print(bob.x.d.c == 30)
x = boby['x']['d']['c']
print(bob.items())
