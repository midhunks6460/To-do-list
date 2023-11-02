from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

todo_list = []

@app.route('/')
def index():
    return render_template('index.html', todos=todo_list)

@app.route('/add', methods=['POST'])
def add():
    task = request.form.get('task')
    if task:
        todo_list.append(task)
    return redirect(url_for('index'))

@app.route('/remove/<int:index>')
def remove(index):
    if 0 <= index < len(todo_list):
        todo_list.pop(index)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
