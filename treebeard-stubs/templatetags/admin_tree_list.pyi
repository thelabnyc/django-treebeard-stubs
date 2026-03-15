from typing import Any

from django.contrib.admin.views.main import ChangeList
from django.http import HttpRequest
from django.template import Library
from django.utils.safestring import SafeString

register: Library
CHECKBOX_TMPL: str

def result_tree(context: dict[str, Any], cl: ChangeList, request: HttpRequest) -> SafeString: ...
