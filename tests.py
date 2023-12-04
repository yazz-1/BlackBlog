import unittest
import datetime
from application import app, db


class Test(unittest.TestCase):
	x = {'user': 'userTEST',
			'title': 'titleTEST',
			'article': 'This article is a test, ' + str(datetime.datetime.now(tz=datetime.timezone.utc))
	}

	def test_create_article(self):
		print("\nRunning CRUD test on database:\n")
		tests = db.tests
		article_id = tests.insert_one(self.x).inserted_id
		self.assertIsNotNone(article_id)
		print("-CREATE: done")

		query = {'user': 'userTEST'}
		article_test = tests.find(query).sort({'_id':-1}).limit(1)[0]
		self.assertEqual(self.x['article'], article_test['article'])
		print("-READ: done")

		modified = {'$set': {'article': 'This article has been modified'}}
		article_mod = tests.update_one(query, modified)
		self.assertNotEqual(self.x, tests.find_one(query))
		print("-UPDATE: done")

		db.tests.delete_one(query)
		self.assertIsNone(tests.find_one(query))
		print("-DELETE: done")


	"""
	def test_http_post():

	def test_register():

	def test_login():

	"""


if __name__ =='__main__':
	unittest.main()