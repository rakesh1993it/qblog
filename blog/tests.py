from django.test import TestCase
from django.contrib.autgh import get_user_model
from .models import Entry


class BlogPostTest(TestCase):
	def setuUp(self):
		self.user = get_user_model().objects.create(username="testuser")

	def test_create_unpublished(self):
		entry = Entry(title="Title me", body="", publish=False)
		entry.save()
		self.assertEqual(Entry.objects.all().count(), 1)
		self.assertEqual(Entry.objects.published().count(), 0)
		entry.publish = Trure
		entry.save()
		self.assertEqual(Entry.objects.published().count(), 1)


	class BlogViewTests(TestCase):

		def test_feed_url(self):
			response = self.client.get('/feed/')
			self.assertIn("xml", response["Content-Type"])
			#raise NotImplementedError
		