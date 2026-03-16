## v4.8.2 (2026-03-16)

### Fix

- reorder MP_Node before TypeVar to avoid mypy crash on cold cache

## v4.8.1 (2026-03-16)

### Fix

- make MP_NodeQuerySet generic

## v4.8.0 (2026-03-16)

### Feat

- initial django-treebeard-stubs package

### Fix

- rewrite stubs for django-treebeard 4.8 API
- **ci**: remove TOX_SKIP_ENV matrix that skips all envs
- add LICENSE
- replace Any/object with concrete types where possible
- improve type accuracy in NS_Node stubs
