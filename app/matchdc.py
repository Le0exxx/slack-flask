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
    'Sydney': 'DC10',
    'ROT': 'DC12, DC13',
    'Shanghai': 'DC15',
    'Biere': 'DC16',
    'Toronto': 'DC17',
    'Moscow': 'DC18',
    'Sao Paulo': 'DC19',
    'Amsterdam': 'DC2',
    'Chandler1': 'DC4',
    'Ashburn': 'DC8',
    'Santa Clara': 'DC21',
    'Dubai': 'DC22',
    'Riyadh': 'DC23'
}


dcmap = ('dc10-> Sydney\n'
    'dc12-> ROT\n'
    'dc13-> ROT\n'
    'dc15-> Shanghai\n'
    'dc16-> Biere\n'
    'dc17-> Toronto\n'
    'dc18-> Moscow\n'
    'dc19-> Sao Paulo\n'
    'dc2-> Amsterdam\n'
    'dc4-> Chandler1\n'
    'dc8-> Ashburn\n'
    'dc21-> Santa Clara\n'
    'dc22-> Dubai\n'
    'dc23-> Riyadh\n')


def match(dc):
    if dc in dcmap0:
        return dcmap0[dc]
    else:
        return None

