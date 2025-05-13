from langchain_openai import ChatOpenAI
from langchain_core.output_parsers.string import StrOutputParser
from .state import AgentState
from .prompts import classify_prompt, beautify_prompt
import os
from dotenv import load_dotenv
load_dotenv()
OPENAI_API_KEY=os.getenv("OPENAI_API_KEY")
os.environ["OPENAI_API_KEY"]=OPENAI_API_KEY

llm = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0.2)

classify_chain = classify_prompt | llm | StrOutputParser()
beautify_chain = beautify_prompt | llm | StrOutputParser()

def extract_content(state: AgentState):
    return {"text": state["payload"][0]["customer_remark"]}

def route_question_or_compliment(state: AgentState):
    response = classify_chain.invoke({"text": state["text"]})
    if "question" in response.lower():
        return "question"
    elif "compliment" in response.lower():
        return "compliment"

def run_question_code(state: AgentState):
    return {"answer": ["Will address your question and resolve it as soon as possible"]}

def run_compliment_code(state: AgentState):
    return {"answer": ["Thanks for the compliment"]}

def tag_query(state: AgentState):
    if "price" in state["text"]:
        return {"tag": "pricing"}
    elif "package" in state["text"]:
        return {"tag": "packaging"}
    else:
        return {"tag": "general"}

def beautify_answer(state: AgentState):
    response = beautify_chain.invoke({
        "answer": state["answer"][0],
        "tag": state["tag"]
    })
    return {"answer": [response]}
