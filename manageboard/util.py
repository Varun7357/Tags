__author__ = 'nitinw'



def email_check(user):
    if user is not None and user.email.endswith('eroslabs.co'):
        return True
    else:
        return False