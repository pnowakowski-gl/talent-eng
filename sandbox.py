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
