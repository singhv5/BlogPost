from django import template
from social_share.templatetags.social_share import share_url

register = template.Library()

@register.simple_tag
def facebook_share(url):
    return share_url('facebook', url)
