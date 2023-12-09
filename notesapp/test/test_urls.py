"""Unit Test for urls to check what view is called for a given url"""
from django.test import SimpleTestCase
from django.urls import reverse, resolve
from notesapp.views import index, new_note, note_detail, delete_note,  signup, about, profile, change_password

class TestUrls(SimpleTestCase):
    """Test for urls"""
    def test_index_url_is_resolved(self):
        """Test for urls"""
        url = reverse('index')
        print(resolve(url)) 
        self.assertEqual(resolve(url).func, index)

    def test_index_url_is_resolved(self):
        """Test for urls"""
        url = reverse('new')
        print(resolve(url)) 
        self.assertEqual(resolve(url).func, new_note)    

    def test_index_url_is_resolved(self):
        """Test for urls"""
        url = reverse('signup')
        print(resolve(url)) 
        self.assertEqual(resolve(url).func, signup)    

    def test_index_url_is_resolved(self):
        """Test for urls"""
        url = reverse('about')
        print(resolve(url)) 
        self.assertEqual(resolve(url).func, about)   

    def test_index_url_is_resolved(self):
        """Test for urls"""
        url = reverse('profile')
        print(resolve(url)) 
        self.assertEqual(resolve(url).func, profile) 

                           
