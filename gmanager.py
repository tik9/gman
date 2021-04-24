import subprocess
from os import chdir, listdir, path, scandir, walk
import sys
from pathlib import Path
import git

home = str(Path.home())

jekyll = path.join(home, 'portable')
bewerbung = path.join(jekyll, 'bewerbung')


# home_w = path.dirname(path.dirname(path.abspath(__file__)))
# print(home)
# sys.exit()


class color:
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'


config = '.config'
powershell = path.join(home, config, 'powershell')

powershell = path.join(home, 'documents', 'windowspowershell')
user_code = 'Code/User'
user = path.join(home, config, user_code)
user = path.join(home, 'AppData/Roaming', user_code)
custom = path.join(home, '.oh-my-zsh', 'custom')

excludedirs = ['.oh-my-zsh', 'calculator',
               'cpython', 'doks', 'game', 'gman', 'ml']


def main():

    br = ''
    msg = 'commit from gitmanagerpy'

    # msg = 'python data cleaning !!NEW!!'
    # commit(msg=msg, br=br)
    dlist = dwalk()
    # dlist.append(walk())
    dlist.append(custom)
    dlist.append(powershell)
    all(dlist)


def all(dlist):
    for repo in dlist:
        # pass
        print(color.BOLD, repo, color.END)
        chdir(repo)
        # run('pull')
        run('status')
        # run ('remote','-v')
        # commit()
    print(color.BOLD, 'End', color.END)


def dwalk():
    dlist = []
    for root, dirs, files in walklevel():
        if '.git' in dirs:
            if not(any(excl in root for excl in excludedirs)):
                dlist.append(root)

    return dlist


def walklevel():
    num_sep = home.count(path.sep)
    # print('num sep', num_sep)
    for root, dirs, files in walk(home):
        yield root, dirs, files
        dirs.sort()
        num_sep_this = root.count(path.sep)
        # print('num sep this', num_sep_this)
        if num_sep + 1 <= num_sep_this:
            del dirs[:]
        # print(dirs)


def run(*args):
    return subprocess.check_call(['git'] + list(args))
    # return subprocess.Popen(['git'] + list(args))


def commit(br=None, msg=None):

    commit_message = msg
    branch = br
    if br == '':
        branch = 'master'
    if msg == None:
        commit_message = 'commit from gmanager'

    run('add', '.')
    run('commit', '-am', commit_message)
    run('push')


def branch(br):

    run('checkout', '-b', br)


if __name__ == '__main__':
    main()
