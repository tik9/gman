
$repo = ''

$repo_dir = "$hw/$repo"
chdir $repo_dir
# get-childitem .

# $ti = (Get-Culture).TextInfo
# $repogro = $ti.totitlecase($repo)

git init
git add -A
git commit -m 'first commit'
git remote add origin https://github.com/tik9/$repo.git
git push -u origin master