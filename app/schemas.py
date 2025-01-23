from pydantic import BaseModel

class PostBase(BaseModel):
    titile: str
    content: str
    published: bool=True

class PostCreate(PostBase):
    pass

class PostUpdate(PostBase):
    pass