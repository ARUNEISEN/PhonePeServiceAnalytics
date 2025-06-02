from git import Repo

repo_url = "https://github.com/PhonePe/pulse.git"

local_dest = "./data"

Repo.clone_from(repo_url,local_dest)