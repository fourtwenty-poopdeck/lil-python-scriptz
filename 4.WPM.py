#find wpm 

import time, random
TESTS = ['copy this text and hit enter to find your typing speed fgt',
         'type me to find out how many words per minute you can type',
         'premade religions are for plebs. if you really want to do the religion thing, you have to make your own. personally, i practice penguinistic idolatry. i worship a giant gilded penguin statue and pray to it four times a day. i abide by a very strict, very confusing moral/ethical system whereby i strive to foster as much penguiness as possible in myself. i believe that when we die, those of us who have achieved sufficient penguiness will ascend and reincarnate as penguins in the next life. everyone else is doomed to a cycle of birth and rebirth as a human being. as far as i can tell, it is the only true religion.',
]
TEST = random.choice(TESTS)

def main():
    WPM()

def WPM():
    print(TEST)
    input('(press enter to begin)')
    ORIG_TIME = time.time()
    ANSWER = input('>> ')
    FINAL_TIME = time.time()

    if ANSWER != TEST:
        fail()
    else:
        calculate(FINAL_TIME - ORIG_TIME)

def calculate(TIME):
    WORDS = (len(TEST.split(' ')))
    WPM = (WORDS * 60) / TIME
    print('you can type %s words per minute!' % (WPM))

def fail():
    print('you tard, the string you entered was not the same as the one given.\ntry again')


if __name__ == '__main__':
    main()
