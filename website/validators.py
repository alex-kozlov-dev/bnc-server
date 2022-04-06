import os
from django.core.exceptions import ValidationError


def is_svg(file):
    ext = os.path.splitext(file.name)[1]
    if ext.lower() != '.svg':
        raise ValidationError('File should have .svg extension')
