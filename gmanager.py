import subprocess
from os import chdir, path, walk
from settings import *
import shutil

class color:
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'


excludedirs = ['.oh-my-zsh', 'game', 'gman', 'tik9.github.io']


def main():

    # chdir(local_path)
    repo = 'further-skill-tests'
    delete_ghrepo(repo)
    # delete_localrepo(path.join(home,'rest_git',repo))
    # commit(msg='first')
    # dlist = []
    dlist = dwalk()
    dlist.extend(addlist)
    rlist = localrepos(dlist)
    # print(rlist)
    print(ghrepos())


def delete_localrepo(folder):
    shutil.rmtree(folder)
    print('delete', repo)


def ghrepos():
    repos = []
    for repo in pygh_user.get_repos():
        repos.append(repo.name)
    return list(enumerate(repos))


def localrepos(dlist):
    # print(type(dlist))
    rlist = []
    for repo in dlist:
        rlist.append(repo)
    return rlist

    # chdir(repo)
    # print(getcwd())
    # run('pull','origin','master')
    # run('status')
    # run('diff', '--summary')
    # | grep --color "mode change 100644 => 100755"'

    # run ('remote','-v')
    # commit()


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


def delete_ghrepo(repo):
    repo = pygh_user.get_repo(repo)
    repo.delete()


if __name__ == '__main__':
    main()
