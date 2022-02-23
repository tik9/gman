from os import makedirs
from settings import *


def main():
    # pass
    # chdir(local_path)
    new_localrepo()
    # str_ = new_ghrepo()
    # clone()

    # str_ = ch_workspace()
    # with open(workspace, 'w') as file_:
    # file_.write(str_)

    # str_ = new_ghrepo()
    # push_new()
    # str_ = remote_addchange()


def new_localrepo():
    makedirs(local_path, exist_ok=True)
    subprocess.check_call(['git', 'init'])

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


def remote_addchange():
    # print(local_path, url)
    subprocess.check_call(['git', 'remote', 'add', 'origin', repo_url])
    # subprocess.check_call(['git', 'remote', 'set-url', 'origin', url])
    return subprocess.check_call(['git', 'remote', '-v'])


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


def fork():
    # print(gith, user, repo)
    chdir(home)
    clone()

    # subprocess.check_call(['git','remote','add','upstream',url])
    # subprocess.check_call(['git', 'pull', 'upstream', 'master'])


def aliase():
    repoShort = 'gh'
    cap = path.join(custom, 'plugins/common-aliases/common-aliases.plugin.zsh')
    cf = path.join(custom, 'common_functions.zsh')
    # pro = path.join(home, 'Documents/WindowsPowerShell/Microsoft.Powershell_profile.ps1')
    # with open(cap, 'a',) as f:f.write(f'\n{repoShort}=$HOME/{repoShort')

    with open(cf, 'a', encoding='utf8') as f:
        f.write(f'\nfunction {repoShort} {{ cd ${repoShort} }}')

    with open(cf, 'r') as f:
        print(f.read())

    # with open(pro, 'a', encoding='utf8') as f:f.write(f'\n${repoShort}="$hw/{repo}"')


if __name__ == "__main__":
    main()
