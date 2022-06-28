
ghtoken=$(cat $HOME/gman/ghtoken)
user=tik9
repo_api=https://api.github.com/repos/$user
repo=apps

function newname {
     new_repo=test
     res=$(jq -n --arg name "$new_repo" '{name:$name}')
     echo $res
}

function description {
     description='A jekyll static site for applications with help of javascript'
     res=$(jq -n --arg name $repo --arg descr "$description" '{name:$name,description:$descr}')
     echo $res
}

function test {
     curl -i -u $user:$ghtoken https://api.github.com/users/octocat
     # curl $repo_api/$repo
}

test
res=$(description)
# newname
# echo $res
# curl -u "$user:$ghtoken" --request PATCH --data "$res" $repo_api/$repo