from django import template
from connectercise.models import Sport

register = template.Library()

@register.inclusion_tag('connectercise/sports.html')
def get_sport_list(current_sport=None):
    return {'sports': Sport.objects.all(), 'current_sport': current_sport}