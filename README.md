import streamlit as st
import random
from datetime import datetime

# -----------------------------
# 페이지 설정
# -----------------------------
st.set_page_config(
    page_title="오늘의 운세",
    page_icon="🔮",
    layout="centered"
)

# -----------------------------
# 운세 데이터
# -----------------------------
fortune_list = [
    {
        "title": "🌞 최고의 하루",
        "fortune": "오늘은 새로운 도전을 시작하기 좋은 날입니다.",
        "love": "좋은 인연이 다가올 수 있습니다.",
        "money": "뜻밖의 행운이 찾아올 수 있습니다.",
        "study": "집중력이 높아져 공부가 잘 됩니다.",
        "lucky_color": "파란색",
        "lucky_number": "7"
    },
    {
        "title": "🍀 행운 가득",
        "fortune": "평소보다 운이 좋은 하루입니다.",
        "love": "주변 사람들과 즐거운 시간을 보내세요.",
        "money": "계획적인 소비가 도움이 됩니다.",
        "study": "복습하면 좋은 결과가 있습니다.",
        "lucky_color": "초록색",
        "lucky_number": "3"
    },
    {
        "title": "⭐ 차분한 하루",
        "fortune": "무리하지 않으면 좋은 결과가 있습니다.",
        "love": "배려가 좋은 관계를 만듭니다.",
        "money": "큰 지출은 미루는 것이 좋습니다.",
        "study": "기초를 다시 점검해 보세요.",
        "lucky_color": "하늘색",
        "lucky_number": "9"
    },
    {
        "title": "🌈 희망의 하루",
        "fortune": "작은 기회가 큰 행운으로 이어질 수 있습니다.",
        "love": "웃는 얼굴이 좋은 인상을 줍니다.",
        "money": "예상치 못한 좋은 소식이 있습니다.",
        "study": "새로운 것을 배우기 좋은 날입니다.",
        "lucky_color": "노란색",
        "lucky_number": "5"
    },
    {
        "title": "💎 성장하는 하루",
        "fortune": "노력이 좋은 결실을 맺습니다.",
        "love": "진심을 전하면 좋은 일이 생깁니다.",
        "money": "절약이 미래의 행운을 가져옵니다.",
        "study": "꾸준함이 최고의 무기입니다.",
        "lucky_color": "보라색",
        "lucky_number": "1"
    }
]

# -----------------------------
# 제목
# -----------------------------
st.title("🔮 오늘의 운세")

today = datetime.now().strftime("%Y-%m-%d")
st.write(f"오늘 날짜 : **{today}**")

st.markdown("---")

name = st.text_input("이름을 입력하세요")

if st.button("✨ 운세 보기"):

    if name == "":
        st.warning("이름을 입력해주세요.")
    else:
        # 이름마다 같은 운세가 나오도록 설정
        random.seed(name + today)
        result = random.choice(fortune_list)

        st.success(f"{name}님의 오늘의 운세")

        st.subheader(result["title"])

        st.write("### 🌟 종합 운세")
        st.write(result["fortune"])

        st.write("### ❤️ 연애운")
        st.write(result["love"])

        st.write("### 💰 금전운")
        st.write(result["money"])

        st.write("### 📚 학업운")
        st.write(result["study"])

        col1, col2 = st.columns(2)

        with col1:
            st.metric("행운의 숫자", result["lucky_number"])

        with col2:
            st.metric("행운의 색", result["lucky_color"])

st.markdown("---")
st.caption("오늘의 운세는 재미를 위한 콘텐츠입니다 😊")
