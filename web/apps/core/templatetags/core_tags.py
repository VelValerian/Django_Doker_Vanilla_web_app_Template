from django import template
from django.utils.safestring import mark_safe
from django.urls import reverse, NoReverseMatch

register = template.Library()


@register.simple_tag(takes_context=True)
def svg_icon(context, name, css_class=""):
    """
    Renders an SVG icon from the project's sprite.
    Usage: {% svg_icon 'burger' 'icon--large' %}
    """
    svg_html = f'''
    <svg class="icon icon--{name} {css_class}" aria-hidden="true" focusable="false">
        <use xlink:href="#icon-{name}"></use>
    </svg>
    '''
    return mark_safe(svg_html)


@register.simple_tag(takes_context=True)
def is_active(context, url_name, css_class="is-active"):
    """
    Checks if the current URL matches the given url_name.
    Usage: <a href="{% url 'home' %}" class="{% is_active 'home' %}">Home</a>
    """
    try:
        current_path = context['request'].path
        target_url = reverse(url_name)
        if current_path == target_url:
            return css_class
    except (NoReverseMatch, KeyError):
        pass
    return ""
