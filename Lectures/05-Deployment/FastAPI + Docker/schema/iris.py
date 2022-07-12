from pydantic import BaseModel, conlist
from typing import List

# Without this file won't break your app, but it's good practice

#basically create a model describing Iris
#mainly for the purpose of automatic data validation
class Iris(BaseModel):    
    #conlist helps imposing list with constraints
    data: List[conlist(float, 
                       min_items=4,
                       max_items=4)]