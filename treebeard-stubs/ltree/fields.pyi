from collections import UserList
from collections.abc import Iterable
from typing import Any

from django import forms
from django.core.validators import RegexValidator
from django.db.backends.base.base import BaseDatabaseWrapper
from django.db.models import IntegerField, Model
from django.db.models.expressions import BaseExpression, Combinable, Func
from django.db.models.fields import CharField, TextField
from django.db.models.lookups import PostgresOperatorLookup, Transform

path_label_validator: RegexValidator

class PathValue(UserList[str]):
    def __init__(self, value: str | Iterable[str]) -> None: ...

class PathValueProxy:
    field_name: str
    def __init__(self, field_name: str) -> None: ...
    def __get__(self, instance: Model | None, owner: type[Model]) -> PathValue | None: ...
    def __set__(self, instance: Model | None, value: str | PathValue | Iterable[str] | None) -> None: ...

class PathFormField(forms.CharField): ...

class PathField(TextField):
    def db_type(self, connection: BaseDatabaseWrapper) -> str: ...
    def contribute_to_class(self, cls: type[Model], name: str, private_only: bool = ...) -> None: ...
    def from_db_value(
        self, value: str | None, expression: BaseExpression, connection: BaseDatabaseWrapper, *args: Any
    ) -> PathValue | None: ...
    def get_prep_value(self, value: str | PathValue | None) -> str | None: ...
    def to_python(self, value: str | PathValue | None) -> PathValue | None: ...
    def get_db_prep_value(
        self, value: str | PathValue | list[str] | None, connection: BaseDatabaseWrapper, prepared: bool = ...
    ) -> str | None: ...

class AncestorLookup(PostgresOperatorLookup):
    lookup_name: str
    postgres_operator: str

class DescendantLookup(PostgresOperatorLookup):
    lookup_name: str
    postgres_operator: str

class Subpath(Func):
    function: str
    output_field: PathField
    def __init__(
        self, expression: Combinable | str, pos: int | Combinable, length: int | Combinable | None = ..., **extra: Any
    ) -> None: ...

class Ltree2Text(Transform):
    function: str
    lookup_name: str
    output_field: CharField  # type: ignore[assignment]

class Text2LTree(Transform):
    function: str
    lookup_name: str
    output_field: PathField  # type: ignore[assignment]

class NLevel(Transform):
    lookup_name: str
    function: str
    output_field: IntegerField  # type: ignore[assignment]
