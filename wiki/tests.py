from django.test import TestCase
from django.contrib.auth.models import User
from wiki.models import Page
from wiki.forms import PageForm

# Create your tests here.
class WikiTestCase(TestCase):
    def test_true_is_true(self):
        self.assertEqual(True, True)

    def test_page_slugify_on_save(self):
        user = User()
        user.save()

        page = Page(title="My Test Page", content="test", author=user)
        page.save()

        self.assertEqual(page.slug, "my-test-page")

class TestPageModelAndViews(TestCase):
    def test_multiple_pages(self):
        user = User.objects.create()

        Page.objects.create(title="MY test page", content="test", author=user)
        Page.objects.create(title="Another test page", content="test", author=user)

        response = self.client.get('/')

        self.assertEqual(response.status_code, 200)

        responses = response.context['pages']
        self.assertEqual(len(responses), 2)

        self.assertQuerysetEqual(responses, ['<Page: MY test page>', '<Page: Another test page>'], ordered=False)

    def test_detail_view(self):
        user = User.objects.create()

        Page.objects.create(title="Test Page One", content="test", author=user)

        response = self.client.get('/test-page-one/')

        self.assertEqual(response.status_code, 200)

        response_page = response.context['page']
        self.assertEqual(response_page.title, 'Test Page One')

    def test_create_view(self):
        response = self.client.get("/newpage/")

        self.assertEqual(response.status_code, 200)

        self.assertIn('title', response.context['form'].as_p)
        self.assertIn('content', response.context['form'].as_p)

    def test_create_new_page(self):
        user = User.objects.create()

        sample_input = {
            'title': 'Test Page 1',
            'content': "test",
        }

        response = self.client.post('/newpage/', data=sample_input)

        self.assertEqual(response.status_code, 302)




# hello
