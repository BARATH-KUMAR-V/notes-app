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
