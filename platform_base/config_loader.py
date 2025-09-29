import os
from typing import Any, Dict
from dotenv import load_dotenv
import yaml

def load_env_file(env_path: str = ".env") -> None:
    cur = os.getcwd()
    while True:
        candidate = os.path.join(cur, env_path)
        if os.path.exists(candidate):
            load_dotenv(dotenv_path=candidate, override=True)
            return
        parent = os.path.dirname(cur)
        if parent == cur:
            break
        cur = parent


def load_yaml_config(yaml_path: str) -> Dict[str, Any]:
    if not os.path.exists(yaml_path):
        raise FileNotFoundError(f"YAML config file not found: {yaml_path}")

    with open(yaml_path, "r") as file:
        return yaml.safe_load(file)

def get_env_variable(key: str, default: Any = None) -> Any:
    return os.getenv(key, default)
