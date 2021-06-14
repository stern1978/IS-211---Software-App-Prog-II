from flask import Flask, render_template, request, redirect

todo_list = []

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html', todo_list = todo_list)

@app.route('/submit', methods = ['GET', 'POST'])
def submit():
    task = request.form['task']
    email = request.form['email']
    priority = request.form['priority']
    pl = ['High', 'Medium', 'Low']

    if len(email.split('@')) != 2:
        print 'email'
        return redirect('/')
    if priority not in pl:
        print 'priority'
        return redirect('/')

    task_list = (priority, task, email, priority)
    todo_list.append(task_list)
    return redirect('/')
    
@app.route('/clear', methods = ['GET', 'POST'])
def clear():
    del todo_list[:]
    return redirect('/')
    
if __name__ == '__main__':
    app.run(debug=True)
