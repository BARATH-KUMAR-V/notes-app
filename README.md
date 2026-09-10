# 📒 Python Notes App
**DevOps Lab Project 4 | Python Flask | Jenkins Pipeline**

## 🎯 Aim
Build a sticky notes web app using Flask where users can add/delete notes, deployed via Jenkins pipeline.

---

## 📋 Prerequisites
- Python 3.x, pip, Git, Jenkins

---

## 📁 Project Code

### `app.py`
```python
from flask import Flask, request, redirect, render_template_string
app = Flask(__name__)
notes = []

HTML = """
<!DOCTYPE html><html><body style="font-family:Arial;max-width:600px;margin:40px auto">
<h2>Sticky Notes</h2>
<form method="POST" action="/add">
  <textarea name="note" rows="3" cols="40" placeholder="Write a note..."></textarea><br>
  <button type="submit">Add Note</button>
</form>
<hr>
{% for i, n in notes %}
<div style="background:#fffacd;padding:12px;margin:10px;border-radius:6px">
  <p>{{ n }}</p>
  <form method="POST" action="/delete/{{ i }}">
    <button type="submit">Delete</button>
  </form>
</div>
{% endfor %}
</body></html>
"""

@app.route("/")
def index():
    return render_template_string(HTML, notes=enumerate(notes))

@app.route("/add", methods=["POST"])
def add():
    note = request.form.get("note","").strip()
    if note: notes.append(note)
    return redirect("/")

@app.route("/delete/<int:i>", methods=["POST"])
def delete(i):
    if 0 <= i < len(notes): notes.pop(i)
    return redirect("/")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
```

### `requirements.txt`
```
flask
```

### `Jenkinsfile`
```groovy
pipeline {
  agent any
  stages {
    stage('Checkout') {
      steps { git 'https://github.com/BARATH-KUMAR-V/notes-app.git' }
    }
    stage('Install') {
      steps { sh 'pip install -r requirements.txt' }
    }
    stage('Deploy') {
      steps {
        sh 'pkill -f "python app.py" || true'
        sh 'nohup python app.py > app.log 2>&1 &'
        sh 'echo "Notes App running on port 5000"'
      }
    }
  }
}
```

---

## 🚀 How to Run Locally
```bash
pip install flask
python app.py
# Open: http://localhost:5000
```

---

## 🐙 GitHub Setup Commands
```bash
git init
git add .
git commit -m "Add Notes App"
git remote add origin https://github.com/BARATH-KUMAR-V/notes-app.git
git push -u origin main
```

---

## 🔧 Jenkins Pipeline Setup
1. Jenkins → New Item → **Pipeline** → Name: `NotesApp`
2. Pipeline → SCM → Git → URL: `https://github.com/BARATH-KUMAR-V/notes-app.git`
3. Script Path: `Jenkinsfile`
4. Save → Build Now

---

## ✅ Expected Output
- Notes visible in browser at `http://localhost:5000`
- Add and delete sticky notes in real time
