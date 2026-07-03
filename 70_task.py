import json

def invert_dict(d):
    result = {}
    for k, v in d.items():
        result[v] = k
    return result

# d = json.loads(input())
d = {"a": 1, "b": 2, "c": 3}
result = invert_dict(d)
print(json.dumps(result, sort_keys=True))
