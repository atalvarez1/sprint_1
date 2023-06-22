# import pandas as pd

# df = pd.DataFrame({'a': [1, 2, 3], 'b': [4, 5, 6]})

# print(df.head())


import random

adjectives = ['blue', 'large', 'grainy', 'substantial', 'potent', 'thermonuclear']
nouns = ['food', 'house', 'tree', 'bicycle', 'toupee', 'phone']


def random_phrase(list1, list2):

    item1 = random.choice(list1)
    item2 = random.choice(list2)

    return str(item1) + ' ' + str(item2)


if __name__ == '__main__':
    pass
    #print(random_phrase(adjectives, nouns))