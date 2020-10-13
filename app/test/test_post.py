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

if __name__ == '__main__':
    unittest.main()
