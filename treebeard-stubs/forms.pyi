from typing import Any

from django import forms
from django.forms.utils import ErrorList
from django.utils.safestring import SafeString
from treebeard.models import Node

class MoveNodeForm(forms.ModelForm):
    _position: forms.ChoiceField
    _ref_node_id: forms.ChoiceField
    is_sorted: bool | list[str] | None
    def __init__(
        self,
        data: Any | None = ...,
        files: Any | None = ...,
        auto_id: str = ...,
        prefix: str | None = ...,
        initial: dict[str, Any] | None = ...,
        error_class: type[ErrorList] = ...,
        label_suffix: str = ...,
        empty_permitted: bool = ...,
        instance: Node | None = ...,
        **kwargs: Any,
    ) -> None: ...
    def save(self, commit: bool = ...) -> Node: ...
    @staticmethod
    def is_loop_safe(for_node: Node | None, possible_parent: Node) -> bool: ...
    @staticmethod
    def mk_indent(level: int) -> str: ...
    @classmethod
    def add_subtree(cls, for_node: Node | None, node: Node, options: list[tuple[Any, SafeString]]) -> None: ...
    @classmethod
    def mk_dropdown_tree(cls, model: type[Node], for_node: Node | None = ...) -> list[tuple[Any, str]]: ...

def movenodeform_factory(
    model: type[Node],
    form: type[MoveNodeForm] = ...,
    fields: Any | None = ...,
    exclude: tuple[str, ...] | None = ...,
    formfield_callback: Any | None = ...,
    widgets: Any | None = ...,
) -> type[MoveNodeForm]: ...
