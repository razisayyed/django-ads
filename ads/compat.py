"""Compatibility helpers for supporting multiple Django versions."""
import django

if django.VERSION < (4, 0):
    from django.utils.translation import ugettext_lazy as gettext_lazy  # type: ignore
    from django.utils.translation import ugettext as gettext  # type: ignore
else:
    from django.utils.translation import gettext_lazy  # type: ignore
    from django.utils.translation import gettext  # type: ignore

try:  # pragma: no cover - depends on Django version
    from django.utils.encoding import force_str
except ImportError:  # Django < 3.0
    from django.utils.encoding import force_text as force_str  # type: ignore

__all__ = ["gettext", "gettext_lazy", "force_str"]
