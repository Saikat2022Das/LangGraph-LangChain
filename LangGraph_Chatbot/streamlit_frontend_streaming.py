import streamlit as st
from langgraph_backend import chatbot
from langchain_core.messages import HumanMessage

from langchain_ollama import ChatOllama
from langchain_core.messages import HumanMessage

# st.session_state -> dict -> 
CONFIG = {'configurable': {'thread_id': 'thread-1'}}

if 'message_history' not in st.session_state:
    st.session_state['message_history'] = []

# loading the conversation history
for message in st.session_state['message_history']:
    with st.chat_message(message['role']):
        st.text(message['content'])

#{'role': 'user', 'content': 'Hi'}
#{'role': 'assistant', 'content': 'Hi=ello'}

user_input = st.chat_input('Type here')

if user_input:

    # first add the message to message_history
    st.session_state['message_history'].append({'role': 'user', 'content': user_input})
    with st.chat_message('user'):
        st.text(user_input)

    # first add the message to message_history
    with st.chat_message("assistant"):
        placeholder = st.empty()
        full_response = ""

        # stream directly from the model
        for chunk in chatbot.graph.nodes["chat_node"].func.__self__.llm.stream(
            [HumanMessage(content=user_input)]
        ):
            if not chunk.content:
                continue

            full_response += chunk.content
            placeholder.markdown(full_response)

    # after streaming, commit final message to graph
    chatbot.invoke(
        {"messages": [HumanMessage(content=user_input)]},
        config=CONFIG
    )

    st.session_state["message_history"].append(
        {"role": "assistant", "content": full_response}
    )

