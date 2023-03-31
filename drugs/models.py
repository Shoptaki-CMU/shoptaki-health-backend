from arango_orm import Collection
from arango_orm.fields import String

class Drug(Collection):
    __collection__ = 'drugs'

    name = String(required=True, allow_none=False)
    description = String(required=True, allow_none=False)
