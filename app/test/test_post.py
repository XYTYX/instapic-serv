import unittest
import json
import tempfile

from app.main import db
from test_auth import login_user, register_user
from app.test.base import BaseTestCase
from moto import mock_s3

def new_post(self):
    with tempfile.NamedTemporaryFile('w+b', suffix='.png') as f:
        register_user(self)
        resp_login = login_user(self)
        content = b'foo'
        f.name = "filename.png"
        f.write(content)
        f.seek(0)
        return self.client.post(
            '/api/v1/post',
            data=dict(
                file=f,
                text="text"            
            ),
            headers=dict(
                Authorization='Bearer ' + json.loads(
                    resp_login.data.decode()
                )['authorization']
            )
        )

class TestPostBlueprint(BaseTestCase):
    def test_new_post(self):
        """ Test for new post """
        with self.client:
            response = new_post(self)
            data = json.loads(response.data.decode())
            self.assertTrue(data['text'] == 'text')
            self.assertTrue(response.content_type == 'application/json')
            self.assertEqual(response.status_code, 200)

def new_like(self):
    """ tests that a like is created if one doesn't exist already """
    register_user(self)
    resp_login = login_user(self)
    post = new_post(self)
    post_public_id = post['public_id']
    data = self.client.post(
        '/api/v1/post/like/' + post_public_id,
        headers=dict(
            Authorization='Bearer ' + json.loads(
                resp_login.data.decode()
            )['authorization']
        )
    )
    self.assetTrue(get_like(data['like_public_id']))
    self.assertEqual(response.status_code, 200)

def new_like(self):
    """ tests that a like is not created if one already exists """
    register_user(self)
    resp_login = login_user(self)
    post = new_post(self)
    post_public_id = post['public_id']
    data = self.client.post(
        '/api/v1/post/like/' + post_public_id,
        headers=dict(
            Authorization='Bearer ' + json.loads(
                resp_login.data.decode()
            )['authorization']
        )
    )
    self.assetTrue(get_like(data['like_public_id']))
    data_2 = self.client.post(
        '/api/v1/post/like/' + post_public_id,
        headers=dict(
            Authorization='Bearer ' + json.loads(
                resp_login.data.decode()
            )['authorization']
        )
    )
    self.assertEqual(data_2['status'], 400)

def new_unlike(self):
    register_user(self)
    resp_login = login_user(self)
    post = new_post(self)
    like = new_like(self)
    post_public_id = post['public_id']
    data = self.client.post(
        '/api/v1/post/unlike/' + post_public_id,
        headers=dict(
            Authorization='Bearer ' + json.loads(
                resp_login.data.decode()
            )['authorization']
        )
    )
    self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()
