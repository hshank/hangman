from termcolor import colored
import os

def introduction():
	print '\n\n\nWelcome to Hangman - Soccer Edition!!'
	print '\n\n\nThis is a two player game. First Player 1 will suggest a word for Player 2 to guess.'
	print 'Note that the word must be lowercase and cannot contain numbers, special characters, or spaces.'


def clearScreen():
    os.system("clear")
    print colored(""",------.          ,--.  ,--.          ,--.    ,--.  ,--.                                                  \n|  .---',--.,--.,-'  '-.|  |-.  ,---. |  |    |  '--'  | ,--,--.,--,--,  ,---. ,--,--,--. ,--,--.,--,--,  \n|  `--, |  ||  |'-.  .-'| .-. '| .-. ||  |    |  .--.  |' ,-.  ||      \| .-. ||        |' ,-.  ||      \ \n|  |`   '  ''  '  |  |  | `-' |' '-' '|  |    |  |  |  |\ '-'  ||  ||  |' '-' '|  |  |  |\ '-'  ||  ||  | \n`--'     `----'   `--'   `---'  `---' `--'    `--'  `--' `--`--'`--''--'.`-  / `--`--`--' `--`--'`--''--' \n                                                                        `---'          """ , "magenta")

def green(string):
    return colored(string, 'green')

def yellow(string):
    return colored(string, 'yellow')

def red(string):
    return colored(string, 'red')


hangman = {}
hangman[0] = '           ________________\n          |################|\n          |################|\n          |################|\n\n\n    o\n  -()-\n   |\_'+ green('o') + '\n\n'
hangman[1] = '           ________________\n          |################|\n          |################|\n          |################|\n\n\n\n    o     \n  -()-    '+ green('o') + '\n   |\_\n'
hangman[2] = '           ________________\n          |################|\n          |################|\n          |################|\n\n\n           '+ green('o') + '\n    o     \n  -()-  \n   |\_\n'
hangman[3] = '           ________________\n          |################|\n          |################|\n          |################|\n\n                      '+ green('o') + '\n\n    o     \n  -()-  \n   |\_\n'
hangman[4] = '           ________________\n          |################|\n          |################|\n          |################|\n                      '+ green('o') + '\n\n\n    o     \n  -()-  \n   |\_\n'
hangman[5] = '           ________________\n          |      '+ red('GOAL') + '      |\n          |      '+ yellow('GOAL') + '    '+ green('o') + ' |\n          |      '+ green('GOAL') + '      |\n\n\n\n    o     \n  -()-  \n   |\_\n'
endMessage = colored('\n\n_________                                     __           ._.\n\_   ___ \  ____   ____    ________________ _/  |_  ______ | |\n/    \  \/ /  _ \ /    \  / ___\_  __ \__  \\   __\/  ___/  | |\n\     \___(  <_> )   |  \/ /_/  >  | \// __ \|  |  \___ \   \|\n \______  /\____/|___|  /\___  /|__|  (____  /__| /____  >  __\n        \/            \//_____/            \/          \/   \/\n\n', 'cyan')
