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
            prompt = f"""DO NOT review, critique, or analyze the text. DO NOT write "Strengths" or "Areas for Improvement". 
            Your ONLY job is to extract facts from the text and fill in this exact template:

            Summary:
            [Write a 1-paragraph summary of the facts]

            Key Ideas:
            [List 3-5 bullet points]

            Quiz:
            [Write 3 multiple-choice questions based on the text, with answers at the end]

            Text to process:
            {notes_input}"""

            # Send the prompt to the local Gemma model
            response = ollama.chat(model='gemma:2b', messages=[
                {'role': 'user', 'content': prompt}
            ])

            # Display the AI's response on the screen
            st.write(response['message']['content'])
    else:
        st.warning("Please paste some notes first!")