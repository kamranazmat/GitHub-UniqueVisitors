import sys
import requests

try:
    username = sys.argv[1]
    password = sys.argv[2]
except:
    print "usage: python conection.py username password"
    sys.exit(1)

url_repos = "https://api.github.com/users/" + username + "/repos"
r = requests.get(url_repos, auth=(username, password))


if(r.status_code != 200):
    print "Login failed wrong user credentials"
    sys.exit(1)
    
repos = r.json()
for repo in repos:
    if not repo['fork']:
        url_traffic = repo['url'] + "/traffic/popular/referrers"
        response_repo = requests.get(url_traffic, auth=(username, password))
        json_repo = response_repo.json()
        json_len = len(json_repo)
        count = 0
        if json_len == 0:
            print repo['url'], " - ", count
        else:        
            for val in json_repo:
                count = val['uniques']
                print repo['url'], " - ", count