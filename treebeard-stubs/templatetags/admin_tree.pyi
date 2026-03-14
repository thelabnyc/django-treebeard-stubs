from typing import Any

from django.template import Library

register: Library

def result_tree(cl: Any) -> dict[str, Any]: ...
def tree_context(cl: Any) -> list[dict[str, Any]]: ...
