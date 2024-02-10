from ninja import Schema


class StudentSchemaOut(Schema):
    id: int
    name: str
    email: str


class StudentSchemaIn(Schema):
    name: str = None
    email: str = None
