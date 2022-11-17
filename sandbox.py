import requests


def delete_repo(repo_name: str) -> None:
    r = requests.delete(
        url=f"https://api.github.com/repos/pnowakowski-gl/{repo_name}",
        headers={
            "accept": "application/vnd.github+json",
            "authorization": "bearer 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",
        },
    )
    r.raise_for_status()

    return r.status_code


def create_repo() -> int:
    r = requests.post(
        url=f"https://api.github.com/user/repos",
        headers={"authorization": "bearer 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"},
        json={"name": "new_repo", "description": "new repo created via api call"},
    )
    r.raise_for_status()

    return r.status_code


# print(create_repo())
print(delete_repo("new_repo"))
