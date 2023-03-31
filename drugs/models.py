from arango_orm import Collection
from arango_orm.fields import String, List

class Drug(Collection):
    __collection__ = 'drug-label'

    description = List(String(required=True, allow_none=False))

