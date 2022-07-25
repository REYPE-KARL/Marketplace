from django.contrib.auth import get_user_model

from django.test import TestCase


# Create your tests here.
from django.urls import reverse


class UsersManagersTests(TestCase):

    def test_create_user(self):
        User = get_user_model()
        user = User.objects.create_user(email='normal@user.com', user_name='normal', password='foo')

        self.assertEqual(user.email, 'normal@user.com')
        self.assertEqual(user.user_name, 'normal')
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)
        self.assertTrue(user.has_perms(['app_name.permission_code_name']))
        self.assertTrue(user.has_module_perms('myModule'))
        self.assertEqual(str(user), f'{user.user_name}')

        url = reverse("profile", kwargs={"slug": user.slug})
        self.assertEqual(user.get_absolute_url(), url)

        try:
            # username is None for the AbstractUser option
            # username does not exist for the AbstractBaseUser option
            self.assertIsNone(user.username)
        except AttributeError:
            pass

        with self.assertRaises(TypeError):
            User.objects.create_user()
        with self.assertRaises(TypeError):
            User.objects.create_user(email='')
        with self.assertRaises(TypeError):
            User.objects.create_user(user_name='')
        with self.assertRaises(ValueError):
            User.objects.create_user(email='', user_name='normal', password='foo')
        with self.assertRaises(ValueError):
            User.objects.create_user(email='normal@user.com', user_name='', password='foo')

    def test_create_user_2(self):
        User = get_user_model()
        user2 = User.objects.create_user(email='walter@white.com', user_name='heisenberg', password='foo',
                                        first_name='walter', last_name='white')

        self.assertEqual(user2.first_name, 'walter')
        self.assertEqual(user2.last_name, 'white')
        self.assertTrue(user2.is_active)
        self.assertFalse(user2.is_staff)
        self.assertFalse(user2.is_superuser)

        try:
            # username is None for the AbstractUser option
            # username does not exist for the AbstractBaseUser option
            self.assertIsNone(user2.username)
        except AttributeError:
            pass

        with self.assertRaises(TypeError):
            User.objects.create_user(first_name='')
        with self.assertRaises(TypeError):
            User.objects.create_user(last_name='')

    def test_create_superuser(self):
        User = get_user_model()
        admin_user = User.objects.create_superuser(email='super@user.com', user_name='superuserman', password='foo')
        self.assertEqual(admin_user.email, 'super@user.com')
        self.assertEqual(admin_user.user_name, 'superuserman')
        self.assertTrue(admin_user.is_active)
        self.assertTrue(admin_user.is_staff)
        self.assertTrue(admin_user.is_superuser)

        try:
            # username is None for the AbstractUser option
            # username does not exist for the AbstractBaseUser option
            self.assertIsNone(admin_user.username)
        except AttributeError:
            pass

        with self.assertRaises(ValueError):
            User.objects.create_superuser(email='super@user.com', user_name='superuserman',
                                          password='foo', is_superuser= False )
        with self.assertRaises(ValueError):
            User.objects.create_superuser(email='super@user.com', user_name='superuserman',
                                          password='foo', is_staff= False )