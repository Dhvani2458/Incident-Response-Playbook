import json
import os

PLAYBOOK_DIR = "playbooks/"

def list_playbooks():
    return [f for f in os.listdir(PLAYBOOK_DIR) if f.endswith(".json")]

def load_playbook(name):
    with open(os.path.join(PLAYBOOK_DIR, name), "r") as f:
        return json.load(f)
