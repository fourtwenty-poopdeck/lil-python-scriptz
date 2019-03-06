#this script automatically calculates the range of ip addresses available on your network
##when given an ip address and a subnet mask

#intro
print('Welcome to my network address range calculation program!')
print('WARNING: this will only work with subnet masks beginning with 255.255.255!')
print()

#get constants
print('Give me your IP address')
IP = input('>> ')
print('Now lemme get dat subnet mask right quickie')
SUBNET = input('>> ')
print('Thanks, calculating IP range...')

def main():
    extraStep(IP)
    stepFour()

    #outro
    print('Your IP range is the range between your network address and your \nbroadcast address! :D \n\nthanks for using my program, goodbye.')

# subtract the last octet of the subnet mask from 256
## gets number of ip addresses in subnet
def stepOne(SUBNET):
    lastOctet = int(SUBNET.split('.')[-1])
    result = 256 - lastOctet
    return result

# divide the last octet of the IP address by the result of step 1 (no remainder)
## gets theoretical number of subnets below this IP address
def stepTwo(IP):
    firstResult = stepOne(SUBNET)
    IP = int(IP.split('.')[-1])
    result = IP // firstResult
    return result

# multiply the result of step 2 by the result of step one
## this gives us the network address
def stepThree():
    initIP = extraStep(IP)
    one = stepOne(SUBNET)
    two = stepTwo(IP)
    result = one * two 
    print('Your network address is %s.%s!' % (initIP, result))
    return result

# add the result of step 3 and step 1 then subtract 1
## this gives the broadcast address
def stepFour():
    initIP = extraStep(IP)
    one = stepOne(SUBNET)
    three = stepThree()
    result = (one + three) - 1 
    print('Your subnet mask is %s.%s!' % (initIP, result))
    return result

#this function just gets the first three octets of your ip address for printing at the end of program
def extraStep(IP):
    IP = IP.split('.')[0:3]
    IP = '.'.join(IP)
    return IP

if __name__ == '__main__':
    main()
