class Product(BaseModel):
    id: int
    name: str
    labelid: int
    category: str
    gender: str
    currentlyactive: bool
    created: datetime
    updated: Optional[datetime]

class Color(BaseModel):
    id: int
    name: str
    rgb: str