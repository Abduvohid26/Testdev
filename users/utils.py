from django.template.defaultfilters import filesizeformat
from rest_framework.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

def validate_file_size(value):
    limit = 10 * 1024 * 1024
    if value.size > limit:
        raise ValidationError(_('File size should not exceed %s. Current size is %s.') % (filesizeformat(limit), filesizeformat(value.size)))