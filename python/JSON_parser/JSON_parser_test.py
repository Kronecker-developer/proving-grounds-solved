import unittest
from JSON_parser import getToDoList

class JsonParserTest(unittest.TestCase):

    def test_jsonparser_1(self):
        link = 'https://jsonplaceholder.typicode.com/todos'
        userId = 2
        completed = 1
        completedlist = [
        {'userId': 2, 'id': 22, 'title': 'distinctio vitae autem nihil ut molestias quo', 'completed': True},
        {'userId': 2, 'id': 25, 'title': 'voluptas quo tenetur perspiciatis explicabo natus', 'completed': True},
        {'userId': 2, 'id': 26, 'title': 'aliquam aut quasi', 'completed': True},
        {'userId': 2, 'id': 27, 'title': 'veritatis pariatur delectus', 'completed': True},
        {'userId': 2, 'id': 30, 'title': 'nemo perspiciatis repellat ut dolor libero commodi blanditiis omnis', 'completed': True},
        {'userId': 2, 'id': 35, 'title': 'repellendus veritatis molestias dicta incidunt', 'completed': True},
        {'userId': 2, 'id': 36, 'title': 'excepturi deleniti adipisci voluptatem et neque optio illum ad', 'completed': True},
        {'userId': 2, 'id': 40, 'title': 'totam atque quo nesciunt', 'completed': True}
        ]

        self.assertEqual(getToDoList(link,userId,completed), completedlist)

    def test_jsonparser_2(self):
        userId = 7
        link = 'https://jsonplaceholder.typicode.com/todos'
        completed = 0
        notcompletedlist = [
        {'userId': 7, 'id': 123, 'title': 'esse et quis iste est earum aut impedit', 'completed': False},
        {'userId': 7, 'id': 124, 'title': 'qui consectetur id', 'completed': False},
        {'userId': 7, 'id': 125, 'title': 'aut quasi autem iste tempore illum possimus', 'completed': False},
        {'userId': 7, 'id': 128, 'title': 'eius omnis est qui voluptatem autem', 'completed': False},
        {'userId': 7, 'id': 129, 'title': 'rerum culpa quis harum', 'completed': False},
        {'userId': 7, 'id': 131, 'title': 'qui ea incidunt quis', 'completed': False},
        {'userId': 7, 'id': 134, 'title': 'molestiae doloribus et laborum quod ea', 'completed': False},
        {'userId': 7, 'id': 135, 'title': 'facere ipsa nam eum voluptates reiciendis vero qui', 'completed': False},
        {'userId': 7, 'id': 136, 'title': 'asperiores illo tempora fuga sed ut quasi adipisci', 'completed': False},
        {'userId': 7, 'id': 137, 'title': 'qui sit non', 'completed': False},
        {'userId': 7, 'id': 139, 'title': 'consequatur doloribus id possimus voluptas a voluptatem', 'completed': False}
        ]

        self.assertEqual(getToDoList(link,userId,completed), notcompletedlist)

if __name__ == "__main__":
    unittest.main()