#pip install pydantic #data validation for typing
from pydantic import BaseModel, conlist
from typing import List

#typing is a common library for enforcing the type
#similar to TypeScript -> enforcing typing in Javascript
#conlist => constraining how a list behaves

#Data Entity
#in MVC (Model-View-Controller), Model describes the data entity
class Iris(BaseModel):
    data: List[conlist(float, min_items=4, max_items=4)]