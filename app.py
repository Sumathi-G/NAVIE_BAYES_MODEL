import streamlit as st
import joblib

# Load the trained model
model = joblib.load("spam_classifier.pkl")

# Page config
st.set_page_config(page_title="Spam Classifier", layout="centered")

st.title("📩 Email / SMS Spam Classifier")
st.write("Enter a message to check whether it is **Spam** or **Not Spam**")

# User input
message = st.text_area("Enter your message")

# Prediction
if st.button("Predict"):
    if message.strip() == "":
        st.warning("⚠️ Please enter a message")
    else:
        prediction = model.predict([message])[0]

        if prediction == 1:
            st.error("🚨 This message is SPAM")
        else:
            st.success("✅ This message is NOT SPAM")

st.markdown("---")
st.caption("Built with Streamlit & Joblib")
