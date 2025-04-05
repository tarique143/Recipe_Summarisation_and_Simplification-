import streamlit as st
import google.generativeai as genai

# Configure Gemini API key
genai.configure(api_key="AIzaSyCc4B5Og2hOxnERFBSp95iQ9aT-urSCKM8")  # Replace with your Gemini API key

# Initialize the model
model = genai.GenerativeModel("gemini-1.5-pro-latest")

# Streamlit UI
st.set_page_config(page_title="🍳 Recipe Simplifier", page_icon="🥘")
st.title("🥘 Recipe Summarizer & Simplifier")
st.caption("Paste any long recipe and get a quick, simplified version powered by Gemini AI.")

# Input box for recipe
recipe_input = st.text_area("📄 Paste your recipe here:", height=300, placeholder="e.g. 1. Preheat oven to 350°F. 2. Mix flour and sugar...")

# Button to trigger summarization
if st.button("✨ Simplify Recipe"):
    if recipe_input.strip() == "":
        st.warning("Please enter a recipe to summarize.")
    else:
        with st.spinner("Summarizing..."):
            try:
                prompt = f"Summarize and simplify the following recipe for easy understanding:\n\n{recipe_input}"
                response = model.generate_content(prompt)
                summarized = response.text.strip()

                st.subheader("🧾 Simplified Recipe")
                st.success(summarized)

            except Exception as e:
                st.error(f"Error: {str(e)[:200]}")

# Footer
st.markdown("---")
st.caption("Made with ❤️ using Gemini API & Streamlit")