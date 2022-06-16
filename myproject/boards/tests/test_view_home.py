from django.urls import reverse, resolve
from django.test import TestCase
from boards.views import home, board_topics, new_topic
from boards.models import Board, Topic, Post
from ..views import home, board_topics, new_topic
from ..models import Board, Topic, Post
from ..forms import NewTopicForm

class HomeTests(TestCase):
    def setUp(self) -> None:
        self.board = Board.objects.create(name='Django', description='Django board')
        url = reverse('home')
        self.response = self.client.get(url)

    """This is a very simple test case but extremely useful. We are testing the status code of the response. The status code 200 means success."""

    def test_home_view_status_code(self):
        self.assertEquals(self.response.status_code, 200)

    def test_home_url_resolves_home_view(self):
        view = resolve('/')
        self.assertEquals(view.func, home)

    def test_home_view_contains_link_to_topics_page(self):
        board_topics_url = reverse('board_topics', kwargs={'pk': self.board.pk})
        self.assertContains(self.response, 'href="{0}"'.format(board_topics_url))
