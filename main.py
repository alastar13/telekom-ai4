import openai
from openai import AsyncOpenAI
import streamlit as st


def main():
    with st.sidebar:
        openai_api_key = "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"

    st.title("Chatbot")
    if "messages" not in st.session_state:
        st.session_state["messages"] = [{"role": "assistant", "content": "How can I help you?"}]

    for msg in st.session_state.messages:
        st.chat_message(msg["role"]).write(msg["content"])

    if prompt := st.chat_input():
        if not openai_api_key:
            st.info("Please add your OpenAI API key to continue.")
            st.stop()

        openai.api_key = "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"
        st.session_state.messages.append({"role": "user", "content": prompt})
        st.chat_message("user").write(prompt)
        response = openai.chat.completions.create(
            model="gpt-4",
            messages=[
                {
                    "role": "user",
                    "content": st.session_state.messages,
                },
            ],
        )
        msg = response.choices[0].message
        st.session_state.messages.append(msg)
        st.chat_message("assistant").write(msg.content)


if __name__ == "__main__":
    main()
