import streamlit as st

# 페이지 설정
st.set_page_config(
    page_title="첫 웹페이지",
    page_icon="👋",
    layout="centered"
)

# 배경색 및 글자색 스타일
st.markdown("""
<style>
.stApp {
    background-color: #001f5b;
    color: white;
}

h1, h2, h3, h4, h5, h6, p, div, span, label {
    color: white !important;
}

.stButton > button {
    background-color: white;
    font-weight: bold;
    border-radius: 10px;
    padding: 0.5rem 1rem;
}

.stButton > button p,
.stButton > button span {
    color: black !important;
}
</style>
""", unsafe_allow_html=True)

# 화면 상태 초기화
if "page" not in st.session_state:
    st.session_state.page = "main"

# 메인 화면
if st.session_state.page == "main":
    st.markdown(
        "<h1 style='text-align:center;'>안녕하세요 👋</h1>",
        unsafe_allow_html=True
    )

    st.write("")

    if st.button("나도 인사하기"):
        st.session_state.page = "greet"
        st.rerun()

# 축하 화면
elif st.session_state.page == "greet":
    st.balloons()

    st.markdown(
        "<h2 style='text-align:center;'>🎉 첫 웹페이지 제작을 축하해요! 🎉</h2>",
        unsafe_allow_html=True
    )

    st.write("")

    if st.button("돌아가기"):
        st.session_state.page = "main"
        st.rerun()
