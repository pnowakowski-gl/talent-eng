from urllib.parse import urljoin

import requests

from envs_config.api_key import API_KEY
from src.config.config import config


class GitHubApi:
    API_KEY = API_KEY()
    DEFAULT_HEADER = {"accept": "application/vnd.github+json"}
    DEFAULT_AUTH_HEADER = {"authorization": f"bearer {API_KEY}"}
    REPOSITORY = "pnowakowski-gl"

    def __init__(self) -> None:
        pass

    def search_repo(self, repo_name: str) -> dict:
        r = requests.get(
            url=f"https://{config.GITHUB_URL}/search/repositories",
            headers=self.DEFAULT_HEADER,
            params={"q": repo_name},
        )
        r.raise_for_status()

        return r.json()

    def create_repo(self, repo_name: str, desc: str) -> int:
        r = requests.post(
            url=f"http://{config.GITHUB_URL}/user/repos",
            headers=self.DEFAULT_AUTH_HEADER,
            json={"name": repo_name, "description": desc},
        )
        r.raise_for_status()

        return r.status_code

    def delete_repo(self, repo_name: str) -> int:
        r = requests.delete(
            url=f"http://{config.GITHUB_URL}/repos/{self.REPOSITORY}/{repo_name}",
            headers=self.DEFAULT_AUTH_HEADER,
        )
        r.raise_for_status()

        return r.status_code
