
from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
from .models import TicketModel


from django.core.mail import EmailMessage
from django.conf import Settings, settings
from django.template.loader import render_to_string
def send_email_user(instance):
    # Sending Email Logic 
    context = {
        "name": instance.assigned_to,
        "ticketid": instance.ticketId,
        "attachment": '/home/esak/esak_2022/2022_dj/step1_SimpleProject/'+str(instance.attachment.url),
    }
    my_template = render_to_string('ticket/email_template.html', context=context)
    email = EmailMessage(
        'Ticket Created',
        my_template,
        settings.EMAIL_HOST_USER,
        ['esakki2021@gmail.com'],

    )
    email.fail_silently = False
    email.attach_file('/home/esak/esak_2022/2022_dj/step1_SimpleProject/'+str(instance.attachment.url))
    email.send()
    print("Email Send to Assigned User")
    
@receiver(post_save, sender=TicketModel)
def create_ticket_post(sender, instance, created, **kwargs):
    print(instance )
    print("---------" )
    if created: 
        print(" A New Ticket is Generated")
        # send Email 
        send_email_user(instance)
        
        
# Instead of the Below Method we can use the decorators as well 
# post_save.connect(create_ticket_post, sender=TicketModel)