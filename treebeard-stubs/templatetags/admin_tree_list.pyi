from typing import Any

from django.template import Library
from django.utils.safestring import SafeString

register: Library
CHECKBOX_TMPL: str

def result_tree(context: dict[str, Any], cl: Any, request: Any) -> SafeString: ...
