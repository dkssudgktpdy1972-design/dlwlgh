import streamlit as st

# 페이지 설정
st.set_page_config(
    page_title="방배중학교 소개",
    page_icon="🏫",
    layout="wide"
)

# 제목
st.title("🏫 방배중학교 소개")
st.markdown("---")

# 학교 소개
st.header("학교 소개")

st.write("""
방배중학교는 서울특별시 서초구에 위치한 중학교입니다.

학생들이 자신의 꿈과 끼를 키울 수 있도록 다양한 교육활동을 운영하고 있으며,
창의적이고 바른 인성을 갖춘 인재를 육성하기 위해 노력하고 있습니다.
""")

st.markdown("---")

# 교육 목표
st.header("🎯 교육 목표")

col1, col2 = st.columns(2)

with col1:
    st.success("""
    ✔ 바른 인성을 갖춘 학생

    ✔ 창의적으로 생각하는 학생

    ✔ 함께 성장하는 학생
    """)

with col2:
    st.info("""
    📚 배움이 즐거운 학교

    🤝 서로 존중하는 학교

    🌱 미래를 준비하는 학교
    """)

st.markdown("---")

# 학교 정보
st.header("🏫 학교 정보")

st.table({
    "항목": [
        "학교명",
        "지역",
        "학교급",
        "설립"
    ],
    "내용": [
        "방배중학교",
        "서울특별시 서초구",
        "중학교",
        "공립"
    ]
})

st.markdown("---")

# 학교 시설
st.header("🏢 학교 시설")

st.write("""
- 일반 교실
- 과학실
- 컴퓨터실
- 도서관
- 체육관
- 운동장
- 급식실
""")

st.markdown("---")

# 학교 생활
st.header("🎈 학교 생활")

tab1, tab2, tab3 = st.tabs(["동아리", "행사", "진로"])

with tab1:
    st.write("""
    다양한 동아리 활동을 통해 학생들의 재능을 키웁니다.
    """)

with tab2:
    st.write("""
    체육대회, 축제, 봉사활동 등 다양한 학교 행사가 있습니다.
    """)

with tab3:
    st.write("""
    진로체험과 진학상담을 통해 학생들의 미래를 지원합니다.
    """)

st.markdown("---")

# 학교 위치
st.header("📍 학교 위치")

st.write("서울특별시 서초구 방배동")

st.map({
    "lat":[37.481],
    "lon":[126.995]
})

st.markdown("---")

# 푸터
st.caption("© 2026 방배중학교 소개 사이트 (Streamlit)")
