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


def commit(br=None, msg=None):

    commit_message = msg
    branch = br
    if br == '':
        branch = 'master'
    if msg == '':
        commit_message = 'commit from gitpy.py'

    run('add', '.')
    # run("commit", "-am", commit_message)
    # run('push')
    run("push", "-u", 'origin', branch)
    # run("push", "-u", 'origin', branch, '--porcelain>>git.txt')


def branch(br):

    run("checkout", "-b", br)


def pull():
    run("pull")


br = ''
msg = 'shortcut zwischen linkem rechten Tab springen'
# branch(br)
commit(msg=msg, br=br)

# cprint(figlet_format('Git-Commands', font='slant'), 'green')
# print(f'\n{info}')
