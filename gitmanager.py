import subprocess
from pyfiglet import figlet_format
from termcolor import cprint
from os import chdir, listdir, path, scandir, walk

homew = path.dirname(path.dirname(__file__))
ohzsh = '.oh-my-zsh'
setjson = 'C:/Users/User/AppData/Roaming/Code/User'
# setjson='/home/tk/.config/code/User'


def main():

    br = ''
    msg = 'commit from gitmanagerpy'
    # branch(br)
    commit(msg=msg, br=br)

    gitdirs = [f'{homew}/{ohzsh}/custom', setjson]

    for dir in gitdirs:
        # print(listdir(dir))
        print(color.BOLD+dir+color.END)

        chdir(dir)
        # run('status')

    excludedirs = [ohzsh, 'cv', 'doks', 'lt']
    for root, dirs, files in walklevel():

        if '.git' in dirs:
            if not(any(excl in root for excl in excludedirs)):
                print(color.BOLD+root+color.END)
                # chdir(root)
                run('pull')


def walklevel():
    num_sep = homew.count(path.sep)
    for root, dirs, files in walk(homew):
        yield root, dirs, files
        dirs.sort()
        num_sep_this = root.count(path.sep)
        if num_sep + 1 <= num_sep_this:
            del dirs[:]


class color:
    NOTICE = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
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
        commit_message = 'commit from gitmanager.py'

    run('add', '.')
    run("commit", "-am", commit_message)
    run('push')


def branch(br):

    run('checkout', '-b', br)


def pull():
    run('pull')


if __name__ == "__main__":
    main()
