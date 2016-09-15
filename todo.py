from flask import Flask
from flask import render_template
from flask import request
import psycopg2

app = Flask(__name__)
todos = []

#Here we are going open a connection to postgres
conn = psycopg2.connect("dbname=alex user=alex")
cur = conn.cursor()

@app.route("/", methods=['POST','GET'])
def todo_home():
    global todos
    if request.method == 'POST' and  'todo' in request.form:
        cur.execute("INSERT INTO todoitems (item,list_id) VALUES (%s, 1);", (request.form['todo'],))
        #todos.append(request.form['todo'])
        return render_template("todo.html", todos=todos)
    elif request.method == 'POST':
        print request.form['item']
        del todos[int(request.form['item'])]
        #todos.remove(request.form['item'])
        return render_template("todo.html", todos=todos)
    else:
        cur.execute("SELECT item FROM todoitems WHERE list_id = 1;")
        data=cur.fetchall()
        print data
        return render_template("todo.html", todos=data) 
  
@app.route("/cats")
def meow():
    return "Whatever you want"

if __name__ == "__main__":
    app.run('0.0.0.0', debug=True)
