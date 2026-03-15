from typing import Any

from django import forms
from django.utils.safestring import SafeString
from treebeard.models import Node

class TreeNodeChoiceField(forms.ModelChoiceField):
    DEPTH_SEPARATOR: SafeString
    def label_from_instance(self, obj: Node) -> SafeString: ...

class MoveNodeForm(forms.ModelForm):
    treebeard_position: forms.ChoiceField
    treebeard_ref_node: TreeNodeChoiceField
    is_sorted: bool | list[str] | None
    def __init__(
        self, *args: Any, initial: dict[str, Any] | None = ..., instance: Node | None = ..., **kwargs: Any
    ) -> None: ...
    def save(self, commit: bool = ...) -> Node: ...

def movenodeform_factory(
    model: type[Node],
    form: type[MoveNodeForm] = ...,
    exclude: tuple[str, ...] | None = ...,
    **kwargs: Any,
) -> type[MoveNodeForm]: ...
