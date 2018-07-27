import unittest
from app import app
from app.models import Todo


class TodoTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        # print("set up")

    def tearDown(self):
        todos = Todo.objects.all()
        for todo in todos:
            todo.delete()
        # print("down")

    def test_index(self):
        rv = self.app.get('/')
        assert "Todo" in rv.data
        # print("hello test")
