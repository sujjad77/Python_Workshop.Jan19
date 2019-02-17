dict={ 'd1':{'a':1, 'b':2, 'c': 3}, 'd2':{'a':1, 'b':2, 'c': 3}, 'd4':{'d':5, 'r':5, 'u': 6}}
result = {}

for key,value in dict.items():
    if value not in result.values():
        result[key] = value

print(result)