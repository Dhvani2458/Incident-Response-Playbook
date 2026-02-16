import datetime

def create_incident(event):
    incident = {
        "id": event.get("id", "INC-" + datetime.datetime.now().strftime("%H%M%S")),
        "type": event.get("type", "Unknown"),
        "severity": event.get("severity", "Medium"),
        "timestamp": datetime.datetime.now().isoformat(),
        "details": event,
    }
    return incident
