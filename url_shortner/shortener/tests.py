from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from shortener.models import Url


class AccountTests(APITestCase):
    def test_create_url(self):
        """
        Ensure we can create a new shortened url.
        """
        url = reverse("create")

        data = {"link": "ht://www.tier.app"}
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(
            response.json(), {"success": False, "error": "URL is not valid"}
        )
        self.assertEqual(Url.objects.count(), 0)

        data = {"link": "https://www.tier.app"}
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Url.objects.count(), 1)
