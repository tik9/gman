
ghtoken=$(cat $HOME/gman/ghtoken)
user=tik9
repo_api=https://api.github.com/repos/$user

function newname {
     old_repo=
     new_repo=test
     new_name=$(jq -n --arg name "$new_repo" '{name:$name}')
     echo $new_name
     # curl -u "$user:$ghtoken" -X PATCH -d "$new_name" $repo_api/$old_repo
}

function description {
     descript='a test repo for a node express app'
     repo=node-test
     jq_desc=$(jq -n --arg name $repo --arg descr "$descript" '{name:$name,description:$descr}')
     echo $jq_desc
     curl -u "$user:$ghtoken" --request PATCH --data "$jq_desc" $repo_api/$repo
}

function test {
     # curl -i -u $user:$ghtoken https://api.github.com/users/octocat
     curl $repo_api/node-test
}

# test
# description
# newname