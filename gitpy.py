import subprocess
from pyfiglet import figlet_format
from termcolor import cprint

class color:
    NOTICE = '\033[91m'
    END = '\033[0m'


info = color.NOTICE + '''Automate process commands such as clone,..\n''' + color.END


def run(*args):
    return subprocess.check_call(['git'] + list(args))


def clone():

    __user__ = 'tik9'
    __repo__ = ''

    local_path = ''

    subprocess.Popen(['git', 'clone', "https://github.com/" +
                      __user__ + "/" + __repo__ + ".git", local_path])


def commit():
    commit_message = 'commit from gitpy.py'

    run("commit", "-am", commit_message)
    run("push", "-u", "origin", "master")

def branch():
    branch = input("\nType in the name of the branch you want to make: ")
    br = f'{branch}'

    run("checkout", "-b", br)

    choice = input("\nDo you want to push the branch right now to GitHub? (y/n): ")
    choice = choice.lower()

    if choice == "y":
        run("push", "-u", "origin", br)

    elif choice == "n":
        print("\nOkay, goodbye!\n")

    else:
        print("\nInvalid command! Use y or n.\n")


def pull():
    print("\nPulls changes from the current folder if *.git is initialized.")

    choice = input("\nDo you want to pull the changes from GitHub? (y/n): ")
    choice = choice.lower()

    if choice == "y":
        run("pull")

    elif choice == "n":
        print("\nOkay, goodbye!\n")

    else:
        print("\nInvalid command! Use y or n.\n")

cprint(figlet_format('Git-Commands', font='slant'), 'green')
print(info + "\n")
commit()