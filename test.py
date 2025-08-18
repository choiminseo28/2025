import streamlit as st
import random
import requests
from io import BytesIO
from PIL import Image

st.set_page_config(page_title="AI 그림 맞추기 게임", page_icon="🎨", layout="centered")

st.title("🎨 AI 그림 맞추기 게임 🐶🐱")
st.write("랜덤 이미지를 보고 **고양이인지 강아지인지** 맞혀보세요!")

# 점수 관리
if "score" not in st.session_state:
    st.session_state.score = 0
if "round" not in st.session_state:
    st.session_state.round = 1

# 랜덤으로 정답 고르기
true_label = random.choice(["고양이", "강아지"])

# 랜덤 이미지 불러오기 (임시로 picsum 사용)
url = f"https://picsum.photos/400/300?random={random.randint(1,10000)}"
response = requests.get(url)
img = Image.open(BytesIO(response.content))

st.image(img, caption=f"문제 {st.session_state.round}", use_column_width=True)

choice = st.radio("이 이미지는 무엇일까요?", ["고양이", "강아지"])

if st.button("제출"):
    if choice == true_label:
        st.success("정답입니다! ✅")
        st.session_state.score += 1
    else:
        st.error(f"틀렸습니다 ❌ 정답은 {true_label}")
    st.session_state.round += 1
    st.write(f"현재 점수: {st.session_state.score}")

st.sidebar.write("📊 게임 현황")
st.sidebar.write(f"라운드: {st.session_state.round}")
st.sidebar.write(f"점수: {st.session_state.score}")
