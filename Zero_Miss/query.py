from main import zeroMiss

#program initializer
def query():
    inquery = str(input('Query? (y/n): '))

    while inquery == 'y':
        zeroMiss()
        print('')
        inquery = str(input('Query? (y/n): '))

    print('Goodbye!')

query()
