
class JsJson:
    def __init__(self, json_data, first_json=None):

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

    def __setattr__(self, name, value):
        pointer = self.first_json.json_data
        for i in self.first_json.atrs:
            pointer = pointer[i]
        pointer[name] = value
        return self

    def __str__(self):
     return str(self.json_data)

bob = JsJson({"x": {'d':{'c': 20}}})
bob.x.d.c = 30
print(bob.x)
print(bob)
