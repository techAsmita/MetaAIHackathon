# app.py
import streamlit as st
from inference import CustomerSupportEnv

# Initialize environment
if "env" not in st.session_state:
    st.session_state.env = CustomerSupportEnv()
    obs = st.session_state.env.reset()
    st.session_state.messages = [("Customer", obs.current_customer_query)]

st.title("🤖 AI Customer Support Simulator")

# Show chat messages
for role, msg in st.session_state.messages:
    if role == "Customer":
        st.markdown(f"**🧑 Customer:** {msg}")
    else:
        st.markdown(f"**🤖 Agent:** {msg}")

# Input
user_input = st.text_input("Enter customer message")

if st.button("Send") and user_input:
    st.session_state.messages.append(("Customer", user_input))

    # Simple fallback logic
    if "refund" in user_input.lower():
        reply = "Sorry, we will refund your order"
    elif "frustrated" in user_input.lower():
        reply = "We understand, and we apologize for the trouble"
    elif "escalate" in user_input.lower():
        reply = "We will escalate this to our manager"
    else:
        reply = "Sorry, we are looking into your issue."

    st.session_state.messages.append(("Agent", reply))

    # Step environment
    obs, reward, done = st.session_state.env.step(reply)
    st.success(f"Reward Score: {reward}")