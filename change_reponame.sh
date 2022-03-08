
ghtoken=$(cat ghtoken)
oldName=-new_repo-
new_repo=php
user=tik9
newName=$(jq -n --arg name "$new_repo" '{name:$name}')
echo $newName

curl -u "$user:$ghtoken" -X PATCH -d "$newName" https://api.github.com/repos/$user/$oldName

