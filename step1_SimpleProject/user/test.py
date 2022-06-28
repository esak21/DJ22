from django.test import TestCase
from django.contrib.auth import get_user_model



class userAccountTests(TestCase):
    
    
    def test_new_superuser(self):
        db = get_user_model()
        super_user = db.objects.create_superuser(
            'testuser@super.com', 
            'password',
            'testuser',
            '458789561',
            'lastname',
        )

        self.assertEqual(super_user.email, 'testuser@super.com')
        self.assertEqual(super_user.lastname, 'lastname')
        self.assertEqual(super_user.name, 'testuser')
        self.assertTrue(super_user.is_superuser)
        self.assertTrue(super_user.is_staff)
        self.assertTrue(super_user.is_active)
        self.assertEqual(str(super_user), "testuser")

        with self.assertRaises(ValueError):
            db.objects.create_superuser(
            email ='testuser@super.com', 
            password ='password',
            name = 'testuser',
            mobileno='458789561',
            lastname='lastname',
            is_superuser=False
        )

        with self.assertRaises(ValueError):
            db.objects.create_superuser(
            email ='testuser@super.com', 
            password ='password',
            name = 'testuser',
            mobileno='458789561',
            lastname='lastname',
            is_staff=False
        )

        with self.assertRaises(ValueError):
            db.objects.create_superuser(
            email ='', 
            password ='password',
            name = 'testuser',
            mobileno='458789561',
            lastname='lastname',
            is_staff=False
        )
            

    def test_new_user(self):
        db = get_user_model()
        user = db.objects.create_user(
            email= "sampleuser@gmail.com",
            password='password',
            name= "sample", 
            mobileno = "987854598",
            lastname="pillai"
        )
        self.assertEqual(user.email, 'sampleuser@gmail.com')
        self.assertEqual(user.lastname, 'pillai')

        self.assertFalse(user.is_superuser)

        with self.assertRaises(ValueError):
            db.objects.create_user(
            email ='', 
            password ='password',
            name = 'testuser',
            mobileno='458789561',
            lastname='lastname',
            is_staff=False
        )
        self.assertEqual(user.get_full_name(), 'samplepillai')
        self.assertEqual(user.get_mobile_number(), '987854598')
        user.lastname=''
        self.assertEqual(user.get_full_name(), 'sample')
