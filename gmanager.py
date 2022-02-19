import subprocess
from os import path, walk
from settings import *
import shutil


class color:
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'


# 'custom'
# excludedirs = ['.oh-my-zsh','apps','cpython','fritzbox', 'game', 'ghtemplate','gman','tik9.github.io']
excludedirs = ['.oh-my-zsh', 'fritzbox', 'game', 'gman', ]


def main():

    # chdir(local_path)
    # delete_ghrepo(repo)
    # delete_localrepo(path.join(home,repo))
    # commit(msg='first')
    dlist = dwalk()
    dlist.extend(addlist)
    # result = testgpython()
    # result = commits()
    # repo = Repo(custom)
    # result = commit(repo)
    result = localrepos(dlist)
    # with open('test.txt', 'w') as file_:
        # file_.write(result)

    print(result)


def commit(repo):
    try:
        # print(commit_message)
        repo.git.add(update=True)
        repo.git.commit(m='commit from gmanager by ' + hostname)
        return repo.remote(name='origin').push()
    except:
        return('this is an error')
    # run('push')


def localrepos(dlist):
    # print(type(dlist))
    for repo in dlist:

        # chdir(repo)
        print(repo)
        # repo = Repo(repo).git
        # result = repo.status()
        # result = repo.pull()
        # result=repo.diff()
        # print(result)

        # run('diff', '--summary')
        # run('diff')
        # | grep --color "mode change 100644 => 100755"'
        # commit(repo)
    return 0


def ghrepos():
    repos = []
    for repo in pygh_user.get_repos():
        repos.append(repo.name)
    return list(enumerate(repos))


def dwalk():
    dlist = []
    for root, dirs, files in walklevel():
        if '.git' in dirs:
            if not(any(excl in root for excl in excludedirs)):
                dlist.append(root)

    return dlist


def walklevel():
    num_sep = base_folder.count(path.sep)
    # print('num sep', num_sep)
    for root, dirs, files in walk(base_folder):
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


def delete_ghrepo(repo):
    repo = pygh_user.get_repo(repo)
    repo.delete()


if __name__ == '__main__':
    main()
