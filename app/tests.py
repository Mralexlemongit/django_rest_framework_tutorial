from django.test import TestCase
from rest_framework.test import APIRequestFactory
from rest_framework import status

from app.views import snippet_detail, snippet_list


class SnippetsTestCase(TestCase):
    fixtures = ['snippets.json', ]

    def setUp(self):
        self.factory = APIRequestFactory()

    def test_get_snippets(self):
        request = self.factory.get('/snippets/')
        response = snippet_list(request)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_post_snippets(self):
        data = {"code": "Agregado en test_post_snippet"}
        request = self.factory.post('/snippets/', data)
        response = snippet_list(request)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_post_snippets_400_bad_request(self):
        data = {}
        request = self.factory.post('/snippets/', data)
        response = snippet_list(request)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_get_snippet(self):
        request = self.factory.get('/snippets/')
        response = snippet_detail(request, 1)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_snippet_404_not_found(self):
        request = self.factory.get('/snippets/')
        response = snippet_detail(request, 4)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_post_snippet(self):
        data = {"code": "modificado en test_post_snippet"}
        request = self.factory.get('/snippets/', data)
        response = snippet_detail(request, 1)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_post_snippet_400_bad_request(self):
        data = {"code": ""}
        request = self.factory.post('/snippets/', data)
        response = snippet_detail(request, 1)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
    
    def test_delete_snippet(self):
        data = {"code": ""}
        request = self.factory.delete('/snippets/', data)
        response = snippet_detail(request, 1)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
    
