# pages/tests.py

from django.test import TestCase
from django.test import SimpleTestCase
from django.urls import reverse 

class HomepageTests(SimpleTestCase):
    # Test whether the URL exists at the correct location
    def test_url_exists_at_correct_location(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)

    # Test whether the URL is available by name
    def test_url_available_by_name(self):
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)

    # Test whether the correct template is used for the homepage
    def test_template_name_correct(self):  
        response = self.client.get(reverse("home"))
        self.assertTemplateUsed(response, "home.html")

    # Test whether the homepage template contains the expected content
    def test_template_content(self):  
        response = self.client.get(reverse("home"))
        self.assertContains(response, "<h1>Homepage</h1>")
       

        

class AboutpageTests(SimpleTestCase):
    # Test whether the URL exists at the correct location
    def test_url_exists_at_correct_location(self):
        response = self.client.get("/about/")
        self.assertEqual(response.status_code, 200)

    # Test whether the URL is available by name
    def test_url_available_by_name(self): 
        response = self.client.get(reverse("about"))
        self.assertEqual(response.status_code, 200)

    # Test whether the correct template is used for the about page
    def test_template_name_correct(self): # new
        response = self.client.get(reverse("about"))
        self.assertTemplateUsed(response, "about.html")

    # Test whether the about page template contains the expected content
    def test_template_content(self):
        response = self.client.get(reverse("about"))
        self.assertContains(response, "<h1>About page</h1>")       

        
