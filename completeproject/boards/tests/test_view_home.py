from django.urls import reverse, resolve
from django.test import TestCase
from boards.views import home, board_topics, new_topic
from boards.models import Board, Topic, Post



class HomeTests(TestCase):
    def setUp(self) -> None:
        self.board = Board.objects.create(name='Django', description='Django board.')
        url = reverse('home')  # view name
        self.response = self.client.get(url)

    def test_home_view_status_code(self):
        """
        We are testing the status code of the response. The status code 200 means success.
        """
        self.assertEquals(self.response.status_code, 200)

    def test_home_url_resolves_home_view(self):
        """In the second test, we are making use of the resolve function.
        Django uses it to match a requested URL with a list of URLs listed in the urls.py.
        This test will make sure the URL /, which is the root URL, is returning the home view."""
        view = resolve('/')
        self.assertEquals(view.func, home)

    def test_home_view_contains_link_to_topics_page(self):
        board_topics_url = reverse('board_topics', kwargs={'pk': self.board.pk})
        self.assertContains(self.response, 'href="{0}"'.format(board_topics_url))
        """
        Here we are using the assertContains method to test if the response body contains a given text. The text we are using in the test, is the href part of an a tag. So basically we are testing if the response body has the text href="/boards/1/".
        The assertContains () function is a builtin function in PHPUnit and is used to assert an array having a value. This assertion will return true in the case if the array contains the provided value else return false and in case of true the asserted test case got passed else test case got failed.
        """

