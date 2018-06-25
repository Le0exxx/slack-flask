#
dcmap0 = {
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
    'sydney': 'DC10',
    'rot': 'DC12, DC13',
    'shanghai': 'DC15',
    'biere': 'DC16',
    'toronto': 'DC17',
    'moscow': 'DC18',
    'sao paulo': 'DC19',
    'amsterdam': 'DC2',
    'chandler1': 'DC4',
    'ashburn': 'DC8',
    'santa clara': 'DC21',
    'dubai': 'DC22',
    'riyadh': 'DC23'
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
    dct = dc.translate(str.maketrans('', '', 'DCdc'))  #(None, "DCdc")
    if dct in dcmap0:
        return dcmap0[dct]
    if dc.lower() in dcmap0:
        return dcmap0[dc.lower()]
    else:
        return None