#this program will take the amount you paid and return how much it's worth in grams
#so it's easier to buy in bulk with friends and split
## ex: $40/$110 && oz==$110

#CONSTANTS
EIGHTH = 3.5
QUARTER = 7
HALF = 14
OZ = 28

def main():
    doWork()

#define math
#to find how much it's worth, we multiply the amount paid by total number of grams and divide by the amount you paid
def maths(amount, price, paid):
    result = (paid * amount) / price
    return result

#collect data
def intro():
    print('\nwelcome to the weed calculator\n')
    print('how much are you buying?\nleave blank to default to an OZ')
    amount = input('>> ')
    if amount == '' or ' ':
        amount = OZ
    else:
        amount = int(amount)
    print('how much is it selling for?')
    price = int(input('$'))
    print('how much are you throwing in?')
    paid = int(input('$'))
    print('alrighty, so you\'re buying %s grams, it costs $%s, and you threw $%s on it' % (amount, price, paid))
    return amount, price, paid

def doWork():
    data = intro()
    print(data)
    amount = data[0]
    price = data[1]
    paid = data[2]
    result = maths(amount, price, paid)
    print('congratulations, you get %s grams!!' % (result))
    return result

if __name__ == '__main__':
    main()
