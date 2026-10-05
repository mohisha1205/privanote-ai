import streamlit as st
import ollama

# Set up the web page
st.set_page_config(page_title="PrivaNote AI")
st.title("Private Notes to Quiz Generator")
st.write("Turn your messy notes into clean summaries and quizzes. 100% private, running locally on Gemma.")

# Create the text input box
notes_input = st.text_area("Paste your class notes here:", height=200)

# What happens when the button is clicked
if st.button("Generate Study Material"):
    if notes_input:
        with st.spinner("Gemma is reading your notes..."):
            # Our specific instructions for the AI
            prompt = f"Read these notes and output exactly three sections:\n1. A brief summary.\n2. A bulleted list of key ideas.\n3. A 3-question multiple-choice quiz with the correct answers at the bottom.\n\nHere are the notes:\n{notes_input}"

            # Send the prompt to the local Gemma model
            response = ollama.chat(model='gemma:2b', messages=[
                {'role': 'user', 'content': prompt}
            ])

            # Display the AI's response on the screen
            st.write(response['message']['content'])
    else:
        st.warning("Please paste some notes first!")