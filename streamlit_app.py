import streamlit as st
import time

st.set_page_config()

with open("style.css") as css_style:
    st.markdown(f"<style>{css_style.read()}</style>", unsafe_allow_html=True)


button_1 = st.button("\n       PASSA        \n")

ph = st.empty()
N = 50
for secs in range(N, 0, -1):
    mm, ss = secs // 60, secs % 60
    ph.metric("PGP assistant", f"{mm:02d}:{ss:02d}")
    time.sleep(1)

    if button_1:
        n = 5 * 60