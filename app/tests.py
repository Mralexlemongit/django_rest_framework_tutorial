from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status

from app.views import snippet_detail, snippet_list, SnippetsList


class SnippetsTestCase(TestCase):
    fixtures = ['snippets.json', ]

    def setUp(self):
        self.client = APIClient()

    def test_get_snippets(self):
        response = self.client.get('/snippets/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_post_snippets(self):
        data = {"code": "Agregado en test_post_snippet"}
        response = self.client.post('/snippets/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_post_snippets_400_bad_request(self):
        data = {}
        response = self.client.post('/snippets/', data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_get_snippet(self):
        response = self.client.get('/snippets/1')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_snippet_404_not_found(self):
        response = self.client.get('/snippets/4')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_put_snippet(self):
        data = {"code": "modificado en test_post_snippet"}
        response = self.client.put('/snippets/1', data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_put_snippet_400_bad_request(self):
        data = {"code": ""}
        response = self.client.put('/snippets/1', data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
    
    def test_delete_snippet(self):
        response = self.client.delete('/snippets/1')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
    
