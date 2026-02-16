from flask import Flask, render_template, jsonify
from modules.siem_handler import get_siem_logs
from modules.playbook_manager import list_playbooks, load_playbook

app = Flask(__name__)

@app.route("/")
def dashboard():
    return render_template("dashboard.html")

@app.route("/logs")
def logs():
    logs = get_siem_logs()
    return render_template("logs_view.html", logs=logs)

@app.route("/playbooks")
def playbook_list():
    playbooks = list_playbooks()
    return render_template("playbook_list.html", playbooks=playbooks)

@app.route("/playbook/<name>")
def playbook_view(name):
    pb = load_playbook(name)
    return render_template("playbook_view.html", playbook=pb)

if __name__ == "__main__":
    app.run(debug=True)
