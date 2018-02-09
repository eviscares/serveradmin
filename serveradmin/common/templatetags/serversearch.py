import json

from django import template
from django.conf import settings

from adminapi.filters import filter_classes
from serveradmin.serverdb.models import Attribute

register = template.Library()


@register.inclusion_tag('serversearch.html')
def serversearch_js(search_id):
    attributes = {
        a.pk: {
            'multi': a.multi,
            'type': a.type,
        }
        for a in Attribute.objects.all()
    }

    return {
        'attributes_json': json.dumps(attributes),
        'filters_json': json.dumps([f.__name__ for f in filter_classes]),
        'search_id': search_id,
        'STATIC_URL': settings.STATIC_URL
    }
