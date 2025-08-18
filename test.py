import streamlit as st
import random
import time

st.set_page_config(page_title="두뇌 훈련 미니게임", page_icon="🧠", layout="centered")

st.title("🧠 두뇌 훈련 미니게임 🎮")
st.write("재밌게 놀면서 집중력과 기억력을 키워보세요!")

# 세션 상태 초기화
if "score" not in st.session_state:
    st.session_state.score = 0
if "start_time" not in st.session_state:
    st.session_state.start_time = None
if "number_sequence" not in st.session_state:
    st.session_state.number_sequence = []

# 게임 선택
menu = st.sidebar.radio("게임 선택", ["계산 속도", "색깔 맞추기", "기억력 게임"])

# 1. 계산 속도 게임 🧮
if menu == "계산 속도":
    st.header("🧮 계산 속도 게임")
    a, b = random.randint(1, 20), random.randint(1, 20)
    op = random.choice(["+", "-", "*"])
    question = f"{a} {op} {b}"
    answer = eval(question)

    st.write(f"문제: **{question} = ?**")
    user_answer = st.number_input("정답을 입력하세요", step=1)
    if st.button("제출"):
        if user_answer == answer:
            st.success("정답입니다! ✅")
            st.session_state.score += 1
        else:
            st.error(f"틀렸습니다 ❌ 정답은 {answer}")
        st.write(f"현재 점수: {st.session_state.score}")

# 2. 색깔 맞추기 게임 🎨 (Stroop Test)
elif menu == "색깔 맞추기":
    st.header("🎨 색깔 맞추기 게임")
    colors = ["빨강", "파랑", "초록", "노랑"]
    color_map = {"빨강": "red", "파랑": "blue", "초록": "green", "노랑": "yellow"}

    text = random.choice(colors)
    font_color = random.choice(list(color_map.values()))

    st.markdown(f"<h2 style='color:{font_color};'>{text}</h2>", unsafe_allow_html=True)
    choice = st.radio("글자의 **색깔**은 무엇일까요?", colors)

    if st.button("제출"):
        if color_map[choice] == font_color:
            st.success("정답입니다! ✅")
            st.session_state.score += 1
        else:
            st.error("틀렸습니다 ❌")
        st.write(f"현재 점수: {st.session_state.score}")

# 3. 기억력 게임 🧠
elif menu == "기억력 게임":
    st.header("🧠 기억력 게임")

    if not st.session_state.number_sequence:
        st.session_state.number_sequence = [random.randint(0, 9) for _ in range(3)]
        st.session_state.start_time = time.time()

    # 숫자 보여주기 (3초간)
    if time.time() - st.session_state.start_time < 3:
        st.subheader("기억하세요!")
        st.write(" ".join(map(str, st.session_state.number_sequence)))
    else:
        user_input = st.text_input("숫자들을 순서대로 입력하세요 (예: 3 1 4)")
        if st.button("제출"):
            try:
                user_sequence = list(map(int, user_input.split()))
                if user_sequence == st.session_state.number_sequence:
                    st.success("정답입니다! ✅")
                    st.session_state.score += 1
                    st.session_state.number_sequence = []
                else:
                    st.error(f"틀렸습니다 ❌ 정답은 {st.session_state.number_sequence}")
                    st.session_state.number_sequence = []
            except:
                st.warning("입력이 올바르지 않아요!")

    st.write(f"현재 점수: {st.session_state.score}")

