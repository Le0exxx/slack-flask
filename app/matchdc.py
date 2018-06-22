#
dcmap0 = {
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
    '10': 'Sydney',
    '12': 'ROT',
    '13': 'ROT',
    '15': 'Shanghai',
    '16': 'Biere',
    '17': 'Toronto',
    '18': 'Moscow',
    '19': 'Sao Paulo',
    '2': 'Amsterdam',
    '4': 'Chandler1',
    '8': 'Ashburn',
    '21': 'Santa Clara',
    '22': 'Dubai',
    '23': 'Riyadh',
    'dc10': 'Sydney',
    'dc12': 'ROT',
    'dc13': 'ROT',
    'dc15': 'Shanghai',
    'dc16': 'Biere',
    'dc17': 'Toronto',
    'dc18': 'Moscow',
    'dc19': 'Sao Paulo',
    'dc2': 'Amsterdam',
    'dc4': 'Chandler1',
    'dc8': 'Ashburn',
    'dc21': 'Santa Clara',
    'dc22': 'Dubai',
    'dc23': 'Riyadh',
}


dcmap = {
    'dc10': 'Sydney',
    'dc12': 'ROT',
    'dc13': 'ROT',
    'dc15': 'Shanghai',
    'dc16': 'Biere',
    'dc17': 'Toronto',
    'dc18': 'Moscow',
    'dc19': 'Sao Paulo',
    'dc2': 'Amsterdam',
    'dc4': 'Chandler1',
    'dc8': 'Ashburn',
    'dc21': 'Santa Clara',
    'dc22': 'Dubai',
    'dc23': 'Riyadh',
}

def match(dc):
    if dc in dcmap0:
        return dcmap0[dc]
    else:
        return None

