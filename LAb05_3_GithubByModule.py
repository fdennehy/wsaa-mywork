# to use this install package
# pip install PyGithub

from github import Github
from config import config as cfg

# apikey = cfg["githubkey"]
# use your own key
g = Github(apikey)

for repo in g.get_user("https://github.com/fdennehy").get_repos():
    print(repo.name)