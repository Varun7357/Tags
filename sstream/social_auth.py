__author__ = 'nitinw'


from django.contrib.auth import logout
from social.apps.django_app.views import _do_login



def social_user(backend, uid, user=None, *args, **kwargs):
    '''OVERRIDED: It will logout the current user
    instead of raise an exception '''

    provider = backend.name
    social = backend.strategy.storage.user.get_social_auth(provider, uid)
    if social:
        if user and social.user != user:
            logout(backend.strategy.request)
        elif not user:
            user = social.user
    return {'social': social,
            'user': user,
            'is_new': user is None,
            'switch_user': True,
            'new_association': False}


def switch_user(backend, switch_user=False, user=None, social=None, *args, **kwargs):

    if switch_user and social:
        #
        # social.actions.do_complete will not login second user because of prior user, so we'll do it here.
        #
        #user.social_user = social
        #user.backend = "%s.%s" % (strategy.backend.__module__, strategy.backend.__class__.__name__)
        _do_login(backend, user, social)
        # store last login backend name in session
        backend.strategy.session_set('social_auth_last_login_backend', social.provider)
