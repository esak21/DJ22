from django.contrib.auth.models import User
## Create REceiver
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import Profile

# @receiver(post_save, sender=Profile)
# def profileUpdated(sender, instance,created,  **kwargs):
#     print('profile Saved')
#     print('Instance:'+ str(instance))
#     print('sender:'+ str(sender))
#     print('Created::', created)

# # post_save.connect(profileUpdated, sender=Profile)
# @receiver(post_delete, sender=Profile)
# def DeleteUser(sender, instance, **kwargs):
#     print("deleting user")


# post_delete.connect(DeleteUser, sender=Profile)

# if a user is created Profile will be created automatically 
def createProfile(sender, instance, created, **kwargs):
    if created :
        user = instance 
        profile = Profile.objects.create(
            user = user , 
            username = user.username, 
            email = user.email, 
            name = user.first_name,
        )

post_save.connect(createProfile, sender=User)


def deleteUser(sender, instance, **kwargs):
    user = instance.user
    user.delete()
    print("User Deleted")


post_delete.connect(deleteUser, sender=Profile)