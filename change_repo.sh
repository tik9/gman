
ghtoken=$(cat $HOME/gman/.env|cut -d= -f2)
echo $ghtoken

user=tik9
base=https://api.github.com
repo_api=$base/repos/$user
all_repos=$base/users/$user/repos
repo=tire

all_repo() { curl -s $all_repos |jq '.[].name' ;}
# |jq [].name;}

name_js() {
     res=re
     res=$(jq -n --arg name $res '{name:$name}')
     echo $res
}

ch_name(){
     res=$(name_js)
     curl -s -u "$user:$ghtoken" --request PATCH --data "$(name_js)" $repo_api/$repo
}

get_description() {
     res=$(curl -s $repo_api/$repo)
     echo $(echo "$res"|jq '.description' )
}

ch_description() {
     description='node js'
     res=$(jq -n --arg name $repo --arg descr "$description" '{name:$name,description:$descr}')
     echo $res
}

get_repo() { curl -s $repo_api/$repo|jq .name ;}

# ch_name
# get_repo
# all_repo
# newname
# res=$(ch_description)
# get_description
