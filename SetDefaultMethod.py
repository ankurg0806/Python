# setDefault method for Python Dictionary

# setdefault() is a python standard library method used with dictionaries. Based on whether the key is present in dictionary or not, it either returns the value of a key (if the key is present) or, it inserts key with a value to the dictionary.

# Syntax: dict.setdefault(key, [defaultVal])

# Parameters: It takes two parameters:
# key – Key to be searched in the dictionary.
# defaultVal (optional) – If key is not there in dictionary, it will be inserted with a value defaultVal. If not provided, the default_value will be None.

# Returns:
# Value of the key if it is in the dictionary.
# None if key is not in the dictionary and default_value is not specified.
# defaultVal if key is not in the dictionary and default_value is specified.

# Write a function nested_dict which takes a dictionary where keys are 2-uples (city, property), and returns a new dictionary where keys are city and values are sub-dictionaries {property: values}.

# For exemple, if given dictionary is like the following

# {
    # ('paris', 'population'): 2500000,
    # ('paris', 'coordinates'): (48.51, 2.21),
    # ('paris', 'area'): 86.9,
    # ('paris', 'arrondissements'): 20,
    # ('besancon', 'population'): 120000,
    # ('besancon', 'coordinates'): (47.14, 6.01),
    # ('besancon', 'area'): 65,
# }
# #then nested_dict will return a dict like the following

# {
    # 'paris': {'population': 2500000, 'coordinates': (48.51, 2.21), 'area': 86.9, 'arrondissements': 20},
    # 'besancon': {'population': 120000, 'coordinates': (47.14, 6.01), 'area': 65}
# }
def nested_dict(dict):
    mydict = {}
    for (k1, k2), v in dict.items():
        if k1 in mydict:
            mydict[k1][k2] = v
        else:
            mydict[k1] = {}
            mydict[k1][k2] = v
    return mydict

Simple way using setdefault
# formation_solution
def nested_dict(d):
    dico = {}
    for (k1, k2), v in d.items():
        dico.setdefault(k1, {})[k2] = v
    return dico