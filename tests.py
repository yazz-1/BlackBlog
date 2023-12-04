import unittest
import datetime

from application import app, db


class Test(unittest.TestCase):

	x = {'user': 'userTEST',
			'title': 'titleTEST',
			'article': 'This article is a test, ' + str(datetime.datetime.now(tz=datetime.timezone.utc))
		}

	client = app.test_client()

	def test_create_article(self):
		print('--> Testing create_article() endpoint')
		response = self.client.post('/post', data=self.x)
		self.assertEqual(response.status_code, 200)
	
	def test_edit_article(self):
		print('--> Testing edit_article() endpoint')
		data = {'title': 'newTitleTEST', 'article': 'This article has been modified'}
		response = self.client.post('/edit/userTEST/1', data=data)
		self.assertIn('modified', response.text)


"""

	def test_register():

	def test_login():

	"""


if __name__ =='__main__':
	unittest.main()