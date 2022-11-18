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
    r = requests.get(
        url=f"https://api.github.com/users/pnowakowski-gl/repos",
        headers={"authorization": "bearer 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"},
        json={"name": "new_repo", "description": "new repo created via api call"},
    )
    r.raise_for_status()

    for i in r.json():
        print(i['name'])


#print(create_repo())
#print(delete_repo("new_repo"))
def create_repo():
    r = requests.get(        url="https://api.github.com/search/repositories?q=talent-eng",
        headers={
        "accept": "application/vnd.github+json",
        "authorization": f"bearer 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",})
    r.raise_for_status()

    return r.json()["items"][0]["name"]
print(create_repo())