import json

def get_siem_logs():
    try:
        with open("data/sample_logs.json", "r") as f:
            return json.load(f)
    except:
        return [{"timestamp": "N/A", "event": "No logs found"}]
