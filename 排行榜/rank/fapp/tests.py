from django.test import TestCase,Client,SimpleTestCase
from django.urls import reverse
import json,redis
from rank import settings
import unittest


pool = redis.ConnectionPool(host=settings.REDIS_HOST, port=settings.REDIS_PORT,
                            db=settings.REDIS_DATA_DB,decode_responses=True)
# Create your tests here.
r = redis.Redis(connection_pool=pool)

class RankTests(TestCase):

    def setUp(self):
        self.client = Client()
        self.list_url = reverse('rank',kwargs={'user':'客户端1','start':1,'end':10})
        self.list_url_2 = reverse('rank',kwargs={'name':'客户端1','score':10000})

    def test_rank_GET(self):

        response = self.client.get(self.list_url)

        self.assertEquals(response.status_code,200)

    def test_rank_POST(self):

        response = self.client.post(self.list_url_2)
        self.assertEquals(response.status_code,200)
        self.assertEquals(r.zscore('rank','客户端1'),10000)


# if __name__ == '__main__':
#     unittest.main()