dcmap = {
    'DC10': 'Sydney',
    'DC12': 'ROT',
    'DC13': 'ROT',
    'DC15': 'Shanghai',
    'DC16': 'Biere',
    'DC17': 'Toronto',
    'DC18': 'Moscow',
    'DC19': 'Sao Paulo',
    'DC2': 'Amsterdam',
    'DC4': 'Chandler1',
    'DC8': 'Ashburn',
    'DC21': 'Santa Clara',
    'DC22': 'Dubai',
    'DC23': 'Riyadh',
}

def match(dc):
    if dc in dcmap:
        return dcmap[dc]
    else:
        return None

