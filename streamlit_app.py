import streamlit as st
import time

st.set_page_config()



# Styled HTML form button
st.markdown("""
    <style>
        .custom-button {
            width: 100vw;
            height: 50vh;
            font-size: 72px;
            background-color: #6200EE;
            color: white;
            border: none;
            cursor: pointer;
        }

        body, html {
            margin: 0;
            padding: 0;
        }

        @media (min-width: 768px) {
            .custom-button {
                width: 50vw;
            }
        }
    </style>

    <form action="" method="get">
        <input type="hidden" name="custom_button" value="1">
        <button class="custom-button" type="submit">PASSA</button>
    </form>
""", unsafe_allow_html=True)

ph = st.empty()
n = 50
for secs in range(n, 0, -1):
    secs -= 1
    mm, ss = secs // 60, secs % 60
    ph.metric("PGP assistant", f"{mm:02d}:{ss:02d}")
    time.sleep(1)

    # Get current query params
    params = st.query_params
    # Check if button was clicked
    clicked = params.get("custom_button") == "1"
    # Trigger Python logic
    if clicked:
        n = 50
        # Optional: Clear the query params to reset the state
        #st.query_params.clear()



