from os import makedirs
from settings import *


def main():
    repo = Repo(custom)
    # str_ = remote_addchange()

    # print(str_)

def clone():
    # print(url, local_path)
    # print(local_path)
    # subprocess.check_call(['git', 'clone', url, local_path])
    try:
        repo = Repo.clone_from(url, local_path)
        # return repo
    except git.exc.InvalidGitRepositoryError:
        print('error')


def new_localrepo():
    makedirs(local_path, exist_ok=True)
    # subprocess.check_call(['git', 'init'])
    repo = git.Repo.init(local_path)


def new_ghrepo():
    new = g.get_user().create_repo(repo)
    return new

if __name__ == "__main__":
    main()
