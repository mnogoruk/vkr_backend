from app.schemas.rwschema import RWSchema


class SpecializationCategoryInResponse(RWSchema):
    id: str
    name: str


class SpecializationInResponseBase(RWSchema):
    id: str
    label: str
    laboring: bool


class SpecializationInResponse(SpecializationInResponseBase):
    specialization_category: SpecializationCategoryInResponse
