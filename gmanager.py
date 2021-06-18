import subprocess
from os import chdir,getcwd, path, walk
from settings import *


class color:
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'


excludedirs = ['.oh-my-zsh', 'game', 'gman','tik9.github.io']


def main():

    chdir(local_path)
    # delete_repository(repo)

    # commit(msg='first')
    # dlist = []
    dlist = dwalk()
    # print(type(dlist),type(addlist))
    dlist.extend(addlist)
    all(dlist)
    # print(local_path)
    print(repos())

def repos():
    repos=[]
    for repo in pygh_user.get_repos():
        repos.append(repo.name)
    return list(enumerate(repos))

def all(dlist):
    # print(type(dlist))
    for repo in dlist:
        print(color.BOLD,repo,color.END)
        chdir(repo)
        # print(getcwd())
        # run('pull','origin','master')
        # run('status')
        # run('diff', '--summary')
        # | grep --color "mode change 100644 => 100755"'

        # run ('remote','-v')
        # commit()
    # print(color.BOLD, 'End', color.END)


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



def delete_repository(repo):
    repo = pygh_user.get_repo(repo)
    repo.delete()

if __name__ == '__main__':
    main()
