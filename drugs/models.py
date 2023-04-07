from arango_orm import Collection
from arango_orm.fields import String, List

class Drug(Collection):
    __collection__ = 'drug-label'

    description = List(String(required=True, allow_none=False))
    adverse_reactions_table = List(String(required=True, allow_none=False))
    dosage_and_administration_table = List(String(required=True, allow_none=False))
    drug_interactions_table = List(String(required=True, allow_none=False))
    warnings_and_cautions_table = List(String(required=True, allow_none=False))
    precautions_table = List(String(required=True, allow_none=False))

