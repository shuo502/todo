from app import  app
from app.models import Todo ,TodoForm
from flask_script import Manager

# from flask_script  import Manager
manager=Manager(app)

@manager.command
def save():
    todo=Todo(content="study flask")
    todo.save()

@manager.command
def f():
    todos=Todo.objects.all()
    for i in todos:
        print(i.content)

@manager.command
def k():
    form=TodoForm()
    todo=Todo.objects.get_or_404(id='5b5ac64fd8aea31ef0723278')
    todo.status=222
    todos = Todo.objects.all()
    print(todo.status)

if __name__ =="__main__":
    manager.run()
