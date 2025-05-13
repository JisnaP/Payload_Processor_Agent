from agent.graph import build_graph

if __name__=='__main__':

    graph=build_graph()
    #example input
    input_state = {
        "payload": [{"customer_remark": "I love your service!"}],
        "answer": [],
        "text": "",
        "tag": ""
    }
    result=graph.invoke(input_state)
    print(result)