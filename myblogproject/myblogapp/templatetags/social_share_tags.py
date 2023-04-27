from django import template
register = template.Library()

@register.simple_tag
def my_facebook_share(url):
    return f'<a href="https://www.facebook.com/sharer/sharer.php?u={url}" target="_blank">Share on Facebook</a>'
