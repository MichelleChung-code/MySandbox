dict1 = {1: 'a', 2: 'b', 3: 'c'}
dict2 = {3: 'dict2_c', 4: 'd', 5: 'e'}
dict3 = {5: 'dict3_e', 6: 'f', 7: 'g'}

final = {1: 'a', 2: 'b', 3: 'dict2_c', 4: 'd', 5: 'dict3_e', 6: 'f', 7: 'g'}

dict1.update(dict2)
dict1.update(dict3)

merged_dict = {**dict1, **dict2, **dict3}

assert final == dict1 == merged_dict
