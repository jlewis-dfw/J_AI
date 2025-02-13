import streamlit as st

def main():                 
    st.title("J AI Chatbot")
    chat_container = st.container()

    user_input = st.text_input("Type your message here", key="user_input")

    send_button = st.button("Send", key="send_button")

    if send_button:
         llm_reposnse = "This is a response from the LLM model!"   
    with chat_container:
        st.chat_message("user").write(user_input)
        st.chat_message("llm").write("here is a response from the LLM model")

if __name__ == "__main__":
    main()

