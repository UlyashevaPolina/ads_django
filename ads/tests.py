from django.test import TestCase
import unittest
from .models import Ad, Category, User
from .views import add_ads
from django.utils import timezone


class AdModelTest(TestCase):
    def setUp(self):
        self.cat = Category.objects.create(Name='Категория 1')
        self.user = User.objects.create(username = 'admin')
        self.ad = Ad.objects.create(Title="Объявление 1", Description="Описание 1", Category = Category.objects.get(id=1), User = User.objects.get(id=1), Сondition = 'б/у',Сreated_at = '2025-05-10')
        self.ad1 = Ad.objects.create(Title="Объявление 11", Description="Описание 11", Category = Category.objects.get(id=1), User = User.objects.get(id=1), Сondition = 'б/у',Сreated_at = '2025-05-10')
        

    def test_add_ads(self):
        ad = Ad.objects.create(Title="Объявление 2", Description="Описание 2", Category = Category.objects.get(id=1), User = User.objects.get(id=1), Сondition = 'б/у', Сreated_at = '2025-05-10')
        self.assertIsNotNone(ad)
        self.assertEqual(ad.Title, "Объявление 2")

    def test_edit_ads(self):
        self.ad.Title = 'Обновленное объявление'
        self.ad.save()
        updated_ad = Ad.objects.get(id=self.ad.id)
        self.assertEqual(updated_ad.Title, "Обновленное объявление")

    def test_del_ads(self):
        self.ad1.delete()
        with self.assertRaises(Ad.DoesNotExist):
            Ad.objects.get(id=self.ad1.id)
    
    def tearDown(self):
        Ad.objects.all().delete()