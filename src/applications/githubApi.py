import os

import requests
from dotenv import load_dotenv

from src.config.config import config


class GitHubApi:
    RELATIVE_PATH = os.path.dirname(__file__)
    GIT_API_KEY_PATH = os.path.abspath(
        os.path.join(RELATIVE_PATH, "..", "..", "envs_config", "api_key.env")
    )
    load_dotenv(dotenv_path=GIT_API_KEY_PATH)
    GIT_API_KEY = os.getenv("GIT_API_KEY")
    DEFAULT_HEADER = {"accept": "application/vnd.github+json"}
    DEFAULT_AUTH_HEADER = {
        "accept": "application/vnd.github+json",
        "authorization": f"bearer {GIT_API_KEY}",
    }
    GIT_USER_NAME = "pnowakowski-gl"

    def get_list_of_public_repos(self, repo_name: str) -> dict:
        """
        Search public repositories and returns repos who have repo_name as part of text.
        """
        r = requests.get(
            url=f"{config.GITHUB_URL}/search/repositories",
            headers=self.DEFAULT_AUTH_HEADER,
            params={"q": repo_name},
        )
        r.raise_for_status()

        return r.json()

    def find_users_repos(self, user="pnowakowski-gl") -> str:
        """
        Find repo name of a given user and return generator of them.
        """
        r = requests.get(
            url=f"{config.GITHUB_URL}/users/{user}/repos",
            headers=self.DEFAULT_AUTH_HEADER,
        )
        r.raise_for_status()

        for repo_name in r.json():
            yield repo_name["name"]

    def create_new_repository(self, repo_name: str, desc: str) -> int:
        """
        Create new repository with given name and description if it doesn't currently exist.
        Raise error for status.
        Returns status code.
        """
        if repo_name not in self.find_users_repos():
            r = requests.post(
                url=f"{config.GITHUB_URL}/user/repos",
                headers=self.DEFAULT_AUTH_HEADER,
                json={"name": repo_name, "description": desc},
            )
            r.raise_for_status()

            return r.status_code

        raise Exception(f"{repo_name} already exists and cannot be created.")

    def delete_existing_repository(self, repo_name: str) -> int:
        """
        Delete existing repository with given name if it does exist.
        Raise error for status.
        Returns status code.
        """
        if repo_name in self.find_users_repos():
            r = requests.delete(
                url=f"{config.GITHUB_URL}/repos/{self.GIT_USER_NAME}/{repo_name}",
                headers=self.DEFAULT_AUTH_HEADER,
            )
            r.raise_for_status()

            return r.status_code

        raise Exception(f"{repo_name} does not exist and cannot be deleted.")
