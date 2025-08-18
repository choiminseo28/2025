import streamlit as st
import random

st.set_page_config(page_title="오늘 뭐 먹지?", page_icon="🍜", layout="centered")

st.title("🍽️ 오늘 뭐 먹지? 메뉴 룰렛 🎰")
st.write("메뉴 정하기 어려울 때 룰렛을 돌려보세요!")

# 메뉴 후보 리스트
menus = [
    "🍣 초밥",
    "🍜 라면",
    "🍕 피자",
    "🍔 햄버거",
    "🥩 스테이크",
    "🍛 카레",
    "🥗 샐러드",
    "🍗 치킨",
    "🌮 타코",
    "🍱 도시락",
    "🍙 삼각김밥",
    "🥟 만두",
    "🍤 새우튀김",
    "🍦 아이스크림",
    "🥪 샌드위치"
]

if st.button("룰렛 돌리기 🎰"):
    choice = random.choice(menus)
    st.success(f"오늘의 추천 메뉴는... {choice} 입니다! 🎉")

st.sidebar.header("설정 ⚙️")
add_menu = st.sidebar.text_input("메뉴 직접 추가")
if st.sidebar.button("추가하기"):
    if add_menu:
        menus.append(add_menu)
        st.sidebar.success(f"{add_menu} 추가 완료!")

st.sidebar.write("현재 메뉴 후보:")
st.sidebar.write(", ".join(menus))

