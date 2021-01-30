import subprocess
# from pyfiglet import figlet_format
# from termcolor import cprint
from os import chdir, listdir, path, scandir, walk
import sys
from pathlib import Path


home_w = str(Path.home())
home_script = path.dirname(path.dirname(__file__))


class color:
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'


def main():

    br = ''
    msg = 'commit from gitmanagerpy'
    # msg = 'python data cleaning !!NEW!!'
    # commit(msg=msg, br=br)
    sev_repos()


def sev_repos():
    config = '.config'
    powershell = path.join(home_script, config, 'powershell')
    powershell = path.join(home_w, 'documents', 'windowspowershell')
    user_code = 'Code/User'
    user = path.join(home_script, config, user_code)
    user = path.join(home_w, 'AppData/Roaming', user_code)
    custom = path.join(home_script, '.oh-my-zsh', 'custom')

    git_special_dirs = [powershell]
    git_special_dirs = []
    git_special_dirs.extend(git_first_level())
    for dir in git_special_dirs:
        # pass
        print(color.BOLD + dir + color.END)
        chdir(dir)
        # run('pull')
        # run('status')
        # run ('remote','update')
        commit()
    print(f'{color.BOLD}End{color.END}')


def walklevel():
    num_sep = home_script.count(path.sep)
    for root, dirs, files in walk(home_script):
        yield root, dirs, files
        dirs.sort()
        num_sep_this = root.count(path.sep)
        if num_sep + 1 <= num_sep_this:
            del dirs[:]


def gitFirstLevel():
    slist = []
    excludedirs = ['.oh-my-zsh', 'doks', 'git']
    excludedirs = ['.oh-my-zsh', 'doks', 'cv', 'further-skill-tests',
                   'ghpage', 'my-github-projects', 'ml', 'pluralsight-skill-tests', 'in-quiz-questions']

    for root, dirs, files in walklevel():

        if '.git' in dirs:
            if not(any(excl in root for excl in excludedirs)):
                # print(color.BOLD+root+color.END)
                slist.append(root)
    return slist


def run(*args):
    return subprocess.check_call(['git'] + list(args))
    # return subprocess.Popen(['git'] + list(args))


def commit(br=None, msg=None):

    commit_message = msg
    branch = br
    if br == '':
        branch = 'master'
    if msg == None:
        commit_message = 'commit from gitmanager.py'

    print(commit_message)

    run('add', '.')
    run("commit", "-am", commit_message)
    run('push')


def branch(br):

    run('checkout', '-b', br)


if __name__ == "__main__":
    main()
