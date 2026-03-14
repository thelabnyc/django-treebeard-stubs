from typing import Any

from django.template import Variable

action_form_var: Variable

def needs_checkboxes(context: dict[str, Any]) -> bool: ...
