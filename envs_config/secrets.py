import os

from dotenv import load_dotenv

RELATIVE_PATH = os.path.dirname(__file__)
GIT_API_KEY_PATH = os.path.abspath(
    os.path.join(RELATIVE_PATH, "..", "envs_config", "secrets.env")
)
print(GIT_API_KEY_PATH)
load_dotenv(dotenv_path=GIT_API_KEY_PATH)
GIT_API_KEY = os.getenv("GIT_API_KEY")
GIT_PASSWORD = os.getenv("GIT_PASSWORD")
