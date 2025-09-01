import streamlit as st
import time

st.set_page_config()

#with open("style.css") as css_style:
#    st.markdown(f"<style>{css_style.read()}</style>", unsafe_allow_html=True)


st.markdown("""
    <style>
        button {
            width: 100vw;
            height: 50vh;
            font-size: 48px;
            background-color: #4CAF50;
            color: white;
            border: none;
            cursor: pointer;
        }

        /* Make sure body doesn't add padding */
        .main, body, html {
            margin: 0;
            padding: 0;
        }

        @media (min-width: 768px) {
            .full-width-half-height-button {
                width: 50vw;  /* Optional: Adjust for tablets/desktops */
            }
        }
    </style>

""", unsafe_allow_html=True)


button_1 = st.button("PASSA")

ph = st.empty()
N = 50
for secs in range(N, 0, -1):
    mm, ss = secs // 60, secs % 60
    ph.metric("PGP assistant", f"{mm:02d}:{ss:02d}")
    time.sleep(1)

    if button_1:
        n = 5 * 60