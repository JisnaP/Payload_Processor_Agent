from langgraph import State
from typing import TypedDict,List,Any,Annotated
import operator
class AgentState(TypedDict):
    text:str
    answer: Annotated[List[str],operator.add]
    payload:dict[str,List]
    tag:str
