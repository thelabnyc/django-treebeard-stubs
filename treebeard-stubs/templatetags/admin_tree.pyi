from django.contrib.admin.views.main import ChangeList
from django.template import Library

register: Library

def result_tree(cl: ChangeList) -> dict[str, list[dict[str, int | str | None]] | list | ChangeList | int]: ...
def tree_context(cl: ChangeList) -> list[dict[str, str | int]]: ...
