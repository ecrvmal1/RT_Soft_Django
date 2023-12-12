from django.test import TestCase
from http import HTTPStatus
from django.urls import reverse


class TestMainPage(TestCase):
    fixtures = ("fixtures/009_all.json",)

    def test_page_open(self):
        path = reverse("mainapp:index")
        result = self.client.get(path)
        self.assertEqual(result.status_code, HTTPStatus.OK)