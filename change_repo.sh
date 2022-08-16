
ghtoken=$(cat $HOME/gman/ghtoken)
echo $ghtoken
user=tik9
base=https://api.github.com
repo_api=$base/repos/$user
all_repos=$base/users/$user/repos
repo=fun

function all_repo { curl -s $all_repos ;}

function newname {
     res=fun
     res=$(jq -n --arg name $res '{name:$name}')
     echo $res
}

function get_description {
     res=$(curl -s $repo_api/$repo)
     echo $(echo "$res"|jq '.description' )
}

function ch_description {
     description='Serverless functions on node js'
     res=$(jq -n --arg name $repo --arg descr "$description" '{name:$name,description:$descr}')
     echo $res
}

function test { curl $repo_api/$repo ;}

# test
# all_repo
# res=$(ch_description)
get_description
# res=$(newname)
# curl -w '%{response_code}' 'https://api.github.com/users/tik9'

# descrip: curl -H "Authorization: token OAUTH-TOKEN" --request PATCH --data '{"name":"repo", "description":"a new description"}' https://api.github.com/repos/:owner/:repo
curl -s -u "$user:$ghtoken" --request PATCH --data "$res" $repo_api/$repo