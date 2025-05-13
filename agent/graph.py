from langgraph.graph import StateGraph, START, END
from .state import AgentState
from .nodes import (
    extract_content,
    route_question_or_compliment,
    run_question_code,
    run_compliment_code,
    tag_query,
    beautify_answer
)

def build_graph():
    graph_builder = StateGraph(AgentState)

    graph_builder.add_node("extract_content", extract_content)
    graph_builder.add_node("run_question_code", run_question_code)
    graph_builder.add_node("run_compliment_code", run_compliment_code)
    graph_builder.add_node("tag_query", tag_query)
    graph_builder.add_node("beautify_answer", beautify_answer)

    graph_builder.add_edge(START, "extract_content")
    graph_builder.add_conditional_edges("extract_content",
                                        route_question_or_compliment,
                                        {
                                            "question": "run_question_code",
                                            "compliment": "run_compliment_code"
                                        })
    graph_builder.add_edge("extract_content", "tag_query")
    graph_builder.add_edge("tag_query", "beautify_answer")
    graph_builder.add_edge("run_question_code", "beautify_answer")
    graph_builder.add_edge("run_compliment_code", "beautify_answer")
    graph_builder.add_edge("beautify_answer", END)

    return graph_builder.compile()



    