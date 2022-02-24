from os import makedirs
from settings import *
from os import chdir
import subprocess
from git import Repo
import git

def main():
    # pass
    # chdir(local_path)
    # new_localrepo()
    # str_ = new_ghrepo()
    # clone()

    # with open(workspace, 'w') as file_: file_.write(str_)
    # add_ignore()
    # str_ = new_ghrepo()
    # str_ = remote_addchange()
    push_new()


def new_ghrepo():
    new = g.get_user().create_repo(repo)
    return new

def clone():
    # print(url, local_path)
    # print(local_path)
    # subprocess.check_call(['git', 'clone', url, local_path])
    try:
        repo = Repo.clone_from(repo_url, local_path)
        # return repo
    except git.exc.InvalidGitRepositoryError:
        print('error')


def new_localrepo():
    makedirs(local_path, exist_ok=True)
    repo = git.Repo.init(local_path)


def remote_addchange():
    chdir(local_path)
    subprocess.check_call(['git', 'remote', 'add', 'origin', repo_url])
    # subprocess.check_call(['git', 'remote', 'set-url', 'origin', url])
    return subprocess.check_call(['git', 'remote', '-v'])

def add_ignore():
    exclude='node_modules\n.vscode\npackage-lock.json'
    gitignore=path.join(local_path,'.gitignore')
    with open(gitignore,'a+') as f:
        f.write(exclude)


def push_new():
    subprocess.check_call(
        ['git', 'push', '--set-upstream', 'origin', 'master'])


def ch_workspace():
    str_ = ''
    with open(workspace, 'r') as file_:
        # head = list(islice(file_, 8))
        for line in file_:
            # print(line)
            if 'folders' in line:
                str_ += f'{line}{{\n"path": "{local_path}"\n}},'
                continue
            str_ += line
    return str_


if __name__ == "__main__":
    main()
