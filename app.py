import streamlit as st

st.set_page_config(page_title="TECHLAH", page_icon="🚀")
st.title("🚀 TECHLAH")
st.write("Launch Your Tech Future - LIFE HUB TECH")

st.write("Ask me any coding question!")
q = st.text_area("Your question")
if st.button("Ask TECHLAH"):
    st.success(f"Great question! TECHLAH would answer: {q} - Your full AI will be connected after deploy!")

st.caption("Made by Pretty Mumbere - Kampala")
