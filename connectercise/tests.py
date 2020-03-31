import os, re, inspect, tempfile
from django.test import TestCase
import connectercise.models
from django.contrib.auth.models import User
from connectercise import forms
from django.urls import reverse, resolve
from django.conf import settings
from populate_connectercise import populate
from django.db import models
from django.forms import fields as django_fields

# Create your tests here.
def create_user_object():
    user = User.objects.get_or_create(username='testuser', first_name='Test', last_name='User', email='test@test.com')[0]
    user.set_password('testabc123')
    user.save()
    return user

def create_super_user_object():
    return User.objects.create_superuser('admin', 'admin@test.com', 'testpassword')

def get_template(path_to_template):
    f = open(path_to_template, 'r')
    template_str = ""
    for line in f:
        template_str = f"{template_str}{line}"
    f.close()
    return template_str

class ModelTests(TestCase):

    def setUp(self):
        sport_sp = connectercise.models.Sport.objects.get_or_create(name='Random Sport')
        connectercise.models.Sport.objects.get_or_create(name='Another Random Sport')
        connectercise.models.SportRequest.objects.get_or_create(sport=sport_sp[0], title='Random Request', location='University of Glasgow', desc='Lorem Ipsum?', views=422, creator=create_user_object())

    def test_userprofile_class(self):
        self.assertTrue('UserProfile' in dir(connectercise.models))
        user_profile = connectercise.models.UserProfile()
        expected_attributes = {
            'picture': tempfile.NamedTemporaryFile(suffix=".jpg").name,
            'user': create_user_object(),
        }
        expected_types = {
            'picture': models.fields.files.ImageField,
            'user': models.fields.related.OneToOneField,
        }
        found_count = 0
        for attr in user_profile._meta.fields:
            attr_name = attr.name
            for expected_attr_name in expected_attributes.keys():
                if expected_attr_name == attr_name:
                    found_count+=1
                    self.assertEqual(type(attr), expected_types[attr_name], f"The type of attribute for {attr_name} was {type(attr)}; (expected {expected_types[attr_name]})")
                    setattr(user_profile, attr_name, expected_attributes[attr_name])

        self.assertEqual(found_count, len(expected_attributes.keys()), f"In the UserProfile model, there are {found_count} attributes; (expected {len(expected_attributes.keys())})")
        user_profile.save()

    def test_sport_class(self):
        sport_sp = connectercise.models.Sport.objects.get(name='Random Sport')
        self.assertEqual(sport_sp.name, 'Random Sport', "Test of Sport model failed; (expected name attribute)")
        sport_asp = connectercise.models.Sport.objects.get(name='Another Random Sport')
        self.assertEqual(sport_asp.name, 'Another Random Sport', "Test of Sport model failed; (expected name attribute)")

    def test_request_class(self):
        sport_sp = connectercise.models.Sport.objects.get(name='Random Sport')
        req = connectercise.models.SportRequest.objects.get(title='Random Request')
        self.assertEqual(req.location, 'University of Glasgow', "Test of SportRequest model failed; (expected location attribute)")
        self.assertEqual(req.views, 422, "Test of SportRequest model failed; (expected views attribute)")
        self.assertEqual(req.title, 'Random Request', "Test of SportRequest model failed; (expected title attribute)")
        self.assertEqual(req.sport, sport_sp, "Test of SportRequest model failed; (expected sport attribute)")

    def test_str_method(self):
        sport_sp = connectercise.models.Sport.objects.get(name='Random Sport')
        req = connectercise.models.SportRequest.objects.get(title='Random Request')
        self.assertEqual(str(sport_sp), 'Random Sport', "__str__() method of Sport model failed.")
        self.assertEqual(str(req), 'Random Request', "__str__() method of SportRequest model failed.")