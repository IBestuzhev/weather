from django.template import Library
from django.core.signing import TimestampSigner


register = Library()


@register.simple_tag
def user_token(user):
    signer = TimestampSigner()
    return signer.sign(user.pk)
