import sys
from github import Github

try:
    username = sys.argv[1]
    password = sys.argv[2]
except:
    print "usage: python conection.py username password"
    sys.exit(1)

try:
    g = Github(username, password)
    repos = g.get_user().get_repos()
    for repo in repos:
        pass
except:
    print "Login failed wrong user credentials"
    sys.exit(1)

# https://api.github.com/repos/kamranazmat/UCD-Big-Data-Programming/traffic/views

for repo in repos:
    print repo.name