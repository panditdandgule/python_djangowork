from django.urls import reverse, resolve
from django.test import TestCase
from boards.views import home, board_topics, new_topic
from boards.models import Board, Topic, Post
from ..views import home, board_topics, new_topic
from ..models import Board, Topic, Post
from ..forms import NewTopicForm

class BoardTopicsTests(TestCase):
    def setUp(self) -> None:
        Board.objects.create(name='Django', description='Django Board.')

    def test_board_topics_view_success_status_code(self):
        """The test_board_topics_view_success_status_code method:
        is testing if Django is returning a status code 200 (success) for an existing Board."""
        url = reverse('board_topics', kwargs={'pk': 1})
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)

    def test_board_topics_view_not_found_status_code(self):
        """The test_board_topics_view_not_found_status_code method: is testing if Django is returning
        a status code 404 (page not found) for a Board that doesn’t exist in the database."""
        url = reverse('board_topics', kwargs={'pk': 99})
        response = self.client.get(url)
        self.assertEquals(response.status_code, 404)

    def test_board_topics_url_resolves_board_topics_view(self):
        """The test_board_topics_url_resolves_board_topics_view method:
        is testing if Django is using the correct view function to render the topics."""
        view = resolve('/boards/1/')
        self.assertEquals(view.func, board_topics)

    def test_board_topics_view_contains_link_back_to_homepage(self):
        board_topics_url = reverse('board_topics', kwargs={'pk': 1})
        response = self.client.get(board_topics_url)
        homepage_url = reverse('home')
        self.assertContains(response, 'href="{0}"'.format(homepage_url))

    def test_board_topics_view_contains_navigation_links(self):
        board_topics_url = reverse('board_topics', kwargs={'pk': 1})
        homepage_url = reverse('home')
        new_topic_url = reverse('new_topic', kwargs={'pk': 1})

        response = self.client.get(board_topics_url)

        self.assertContains(response, 'href="{0}"'.format(homepage_url))
        self.assertContains(response, 'href="{0}"'.format(new_topic_url))

