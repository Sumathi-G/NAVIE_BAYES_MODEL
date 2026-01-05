import streamlit as st
import pickle

# Load model
with open("spam_classifier.pkl", "rb") as file:
    model = pickle.load(file)

# App config
st.set_page_config(page_title="Spam Classifier", layout="centered")

st.title("📩 Email / SMS Spam Classifier")
st.write("Enter a message to check whether it is **Spam** or **Not Spam**")

# Text input
message = st.text_area("Enter your message here")

# Predict button
if st.button("Predict"):
    if message.strip() == "":
        st.warning("Please enter a message")
    else:
        prediction = model.predict([message])[0]

        if prediction == 1:
            st.error("🚨 This message is **SPAM**")
        else:
            st.success("✅ This message is **NOT SPAM**")

st.markdown("---")
st.caption("Built using Streamlit & Machine Learning")
