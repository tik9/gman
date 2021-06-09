import subprocess
from os import chdir, path, walk
from pathlib import Path
import requests

home = str(Path.home())

bewerbung = path.join(home, 'bewerbung')

url_api = 'https://api.github.com/user/repos'
repo='react-app'
repo='repo'

class color:
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'


config = '.config'
powershell = path.join(home, config, 'powershell')

# powershell = path.join(home, 'documents', 'windowspowershell')
user_code = 'Code/User'
user = path.join(home, config, user_code)
# user = path.join(home, 'AppData/Roaming', user_code)
custom = path.join(home, '.oh-my-zsh', 'custom')

excludedirs = ['.oh-my-zsh', 'cpython', 'doks', 'game', 'gman', 'ml']


def main():

    br = ''
    msg = 'commit from gitmanagerpy'

    # msg = 'python data cleaning !!NEW!!'
    # commit(msg=msg, br=br)
    dlist = dwalk()
    dlist.append(custom)
    dlist.append(powershell)
    # all(dlist)
    print(delete_repository())

def delete_repository():
    response = requests.delete(url_api+'/tik9/'+repo)
    print(response.json())

def all(dlist):
    for repo in dlist:
        # pass
        print(color.BOLD, repo, color.END)
        chdir(repo)
        # run('pull','origin','master')
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


def commit(msg=None):

    commit_message = msg

    if msg == None:
        commit_message = 'commit from gmanager'

    run('add', '.')
    run('commit', '-am', commit_message)
    run('push')


def branch(br):

    run('checkout', '-b', br)


if __name__ == '__main__':
    main()
