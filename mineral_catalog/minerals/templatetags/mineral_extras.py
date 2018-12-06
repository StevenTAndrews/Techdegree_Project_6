from minerals.models import Mineral

from django import template

register = template.Library()


@register.filter
def getattribute(obj, value):
	return getattr(obj, value)