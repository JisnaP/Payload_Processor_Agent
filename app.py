from agent.graph import build_graph
import streamlit as st
import json
def process_payload(payload):
    graph=build_graph()
    response=graph.invoke(payload)
    return response

st.title("Langgraph Payload Processor")
sample_payload={
    
    "payload":[
    {
        "customer_remarks":"I really appreciate your service"
    }
]

}
st.subheader("Sample Payload Format")
st.json(sample_payload,expanded=True)

st.subheader("Enter your payload here")
user_input=st.text_area(
    "Paste your json payload here",value=json.dumps(sample_payload,indent=4),height=200)
if st.button("Submit"):
    try:
        payload=json.loads(user_input)
        st.success("Payload successfully parsed")
        response=process_payload(payload)
        st.write("Answer",response["answer"][-1])
        st.write("Tag",response["tag"])
    except json.JSONDecodeError as e:
        st.error(f"Invalid json format: {e}")
