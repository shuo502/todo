import unittest
from app import app
from app.models import Todo


class TodoTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        print("set up")

    def tearDown(self):
        todos = Todo.objects.all()
        for todo in todos:
            todo.delete()
        print("down")

    def test_index(self):
        rv = self.app.get('/')
        assert b'Todo' in rv.data
        print("hello test")

    def test_todo(self):
        self.app.post('/add',data=dict(content=b'testtodo'))
        todo=Todo.objects.get_or_404(content="testtodo")
        # todo=Todo.objects.get_or_404(content="abc")
        # todo=Todo.objects.get(content=b"testtodo")
        print(todo)
        assert todo is not None

        #coverage report
        #coverage run -m unittest discover
        #python -m unittest discove


