#find ascii numbers for char

import sys 

def main():
    print('encode or decode?')
    print('Y or E for encode, N or D for decode')
    answer = input('>> ')
    if answer.upper().strip().startswith('Y') or answer.upper().strip().startswith('E'):
        mode = 'encode'
    elif answer.upper().strip().startswith('N') or answer.strip().upper().startswith('D'):
            mode = 'decode'
    else:
        sys.exit('try again')
   
    if mode == 'encode':
        ascii()
    elif mode == 'decode':
        plain()
    else:
        sys.exit('try again')

def ascii():
    char = (input('gimme char:\n>>'))
    char = str(char)
    value = ord(char)
    print('%s translates to %s in ascii encoding!' % (char, value))

def plain():
    char = (input('gimme code:\n>>'))
    char = int(char)
    value = chr(char)
    print('ascii code: %s\ntranslates to: %s' % (char, value))  

if __name__ == '__main__':
    main()
