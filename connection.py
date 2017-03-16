from github import Github

# First create a Github instance:
g = Github("kamranazmat", "")

# Then play with your Github objects:
for repo in g.get_user().get_repos():
    print repo.name