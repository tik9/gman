import subprocess
# from pyfiglet import figlet_format
# from termcolor import cprint
from os import chdir, listdir, path, scandir, walk
import sys
home = path.dirname(path.dirname(__file__))
settingsDir = path.join(home, 'tesseractToMarkdown')
sys.path.append(settingsDir)
from settings import color, gitSpecialDirs
from helper import gitFirstLevel


def main():

    br = ''
    msg = 'commit from gitmanagerpy'
    # branch(br)
    # commit(msg=msg, br=br)

    # print(listdir(dir))
    # print(color.BOLD+dirpath+color.END)

    # run('status')
    # run('pull')
    gitSpecialDirs.extend(gitFirstLevel())
    for dir in gitSpecialDirs:
        print(color.BOLD + dir + color.END)
        chdir(dir)
        # run('pull')
        # run('status')
        # run ('remote','update')
        commit(msg=msg, br=br)
    print(f'{color.UNDERLINE}End')


def run(*args):
    # return subprocess.check_call(['git'] + list(args))
    return subprocess.Popen(['git'] + list(args))


def commit(br=None, msg=None):

    commit_message = msg
    branch = br
    if br == '':
        branch = 'master'
    if msg == '':
        commit_message = 'commit from gitmanager.py'

    run('add', '.')
    run("commit", "-am", commit_message)
    run('push')


def branch(br):

    run('checkout', '-b', br)


if __name__ == "__main__":
    main()
