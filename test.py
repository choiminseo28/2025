import streamlit as st
import random
import time

st.set_page_config(page_title="무드 기반 랜덤 음악 룰렛", page_icon="🎵", layout="wide")

# -----------------------------
# 무드별 배경 이미지
# -----------------------------
BACKGROUND_IMAGES = {
    "😀 신남/행복": "https://i.pinimg.com/originals/b8/6b/2f/b86b2f2fcf0d26cf7a356f5e40c30b57.jpg",
    "😊 차분/따뜻": "https://i.pinimg.com/originals/88/34/8b/88348bb2aa81f09b97b789d5026a756a.jpg",
    "😢 우울/위로": "https://i.pinimg.com/originals/6e/63/8c/6e638c6e9d2afc2c1e20a78a4f5bd24c.jpg",
    "😡 파워/분노해소": "https://i.pinimg.com/originals/d3/3e/9d/d33e9d65f0a050d8e21b8b2e87fbd4cf.jpg",
    "😴 힐링/휴식": "https://i.pinimg.com/originals/1c/1a/32/1c1a322ff9fce2f57d2f6eae8ed5b0e7.jpg",
    "😎 자신감/쿨": "https://i.pinimg.com/originals/50/f1/2a/50f12a0b9faecfdaed2f3f5b9285c1e5.jpg",
    "💔 이별/감성": "https://i.pinimg.com/originals/49/45/16/494516d6a020ba324deeeef01a52a7ad.jpg",
    "💃 신나는 댄스": "https://i.pinimg.com/originals/7a/6c/0f/7a6c0f82a92cb2c7e91821edff49c51f.jpg",
    "🧘 집중/공부": "https://i.pinimg.com/originals/cd/d3/49/cdd34927e0dcd6d9b4fbec6d38e25123.jpg",
    "🚀 운동/드라이브": "https://i.pinimg.com/originals/1f/24/d6/1f24d6b7d905ddf6f1183d12c3ebeaeb.jpg",
}

# 기본 배경 설정
current_bg = BACKGROUND_IMAGES["😀 신남/행복"]

# 세션 상태
if "selected_mood" in st.session_state:
    current_bg = BACKGROUND_IMAGES.get(st.session_state.selected_mood, current_bg)

# 동적 배경 스타일 적용
def set_background(image_url):
    page_bg = f"""
    <style>
    [data-testid="stAppViewContainer"] {{
        background-image: url("{image_url}");
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
    }}
    [data-testid="stHeader"] {{
        background: rgba(0,0,0,0);
    }}
    [data-testid="stSidebar"] {{
        background: rgba(255, 255, 255, 0.8);
        backdrop-filter: blur(10px);
        border-radius: 12px;
    }}
    </style>
    """
    st.markdown(page_bg, unsafe_allow_html=True)

set_background(current_bg)

# -----------------------------
# 앱 제목 영역
# -----------------------------
st.markdown("""
<div style="text-align:center; padding:20px; background:rgba(255,192,203,0.7); border-radius:15px;">
    <h1 style="color:#FF69B4; font-size:3em; text-shadow: 2px 2px 5px white;">🎵 무드 기반 랜덤 음악 룰렛 🎰</h1>
    <p style="color:#fff; font-size:1.2em;">얼굴 이모지로 <b>오늘의 무드</b>를 고르면,<br> 그 분위기에 맞는 노래를 랜덤 추천해드려요! 🎶<br>유튜브 영상까지 바로 감상 가능!</p>
</div>
""", unsafe_allow_html=True)

# -----------------------------
# 데이터: 무드별 추천 곡 리스트 (모두 재생 가능한 영상만 포함)
# -----------------------------
SONGS = {
    "😀 신남/행복": [
        {"title": "NewJeans - Super Shy", "url": "https://www.youtube.com/watch?v=ArmDp-zijuc"},
        {"title": "IVE - IAM", "url": "https://www.youtube.com/watch?v=6ZUIwj3FgUY"},
        {"title": "Pharrell Williams - Happy", "url": "https://www.youtube.com/watch?v=ZbZSe6N_BXs"},
        {"title": "BTS - Dynamite", "url": "https://www.youtube.com/watch?v=gdZLi9oWNZg"}
    ],
    "😊 차분/따뜻": [
        {"title": "Paul Kim - 모든 날, 모든 순간", "url": "https://www.youtube.com/watch?v=JwFqkZMW9p8"},
        {"title": "Lauv - I Like Me Better", "url": "https://www.youtube.com/watch?v=3tUh-x-fp8Q"},
        {"title": "IU - 밤편지", "url": "https://www.youtube.com/watch?v=BzYnNdJhZQw"}
    ],
    "😢 우울/위로": [
        {"title": "Adele - Someone Like You", "url": "https://www.youtube.com/watch?v=hLQl3WQQoQ0"},
        {"title": "윤하 - 사건의 지평선", "url": "https://www.youtube.com/watch?v=g3B2rYI5E1E"},
        {"title": "Sam Smith - Too Good At Goodbyes", "url": "https://www.youtube.com/watch?v=J_ub7Etch2U"},
        {"title": "백예린 - Square", "url": "https://www.youtube.com/watch?v=tDukIfFzX18"}
    ],
    "😡 파워/분노해소": [
        {"title": "Imagine Dragons - Believer", "url": "https://www.youtube.com/watch?v=7wtfhZwyrcc"},
        {"title": "Linkin Park - Numb", "url": "https://www.youtube.com/watch?v=kXYiU_JCYtU"},
        {"title": "Stray Kids - Thunderous", "url": "https://www.youtube.com/watch?v=EaswWiwMVs8"}
    ],
    "😴 힐링/휴식": [
        {"title": "LOFI Girl - lofi hip hop radio", "url": "https://www.youtube.com/watch?v=jfKfPfyJRdk"},
        {"title": "BTS - Spring Day (봄날)", "url": "https://www.youtube.com/watch?v=xEeFrLSkMm8"},
        {"title": "Crush - 가끔", "url": "https://www.youtube.com/watch?v=2Gm_PfUq9w8"}
    ],
    "😎 자신감/쿨": [
        {"title": "BLACKPINK - DDU-DU DDU-DU", "url": "https://www.youtube.com/watch?v=IHNzOHi8sJs"},
        {"title": "Dua Lipa - Don't Start Now", "url": "https://www.youtube.com/watch?v=oygrmJFKYZY"},
        {"title": "LE SSERAFIM - ANTIFRAGILE", "url": "https://www.youtube.com/watch?v=pyf8cbqyfPs"}
    ],
    "💔 이별/감성": [
        {"title": "태연 - 그대라는 시", "url": "https://www.youtube.com/watch?v=Cg8sDCf-3MM"},
        {"title": "Anne-Marie - 2002", "url": "https://www.youtube.com/watch?v=Il-an3K9pjg"},
        {"title": "정승환 - 눈사람", "url": "https://www.youtube.com/watch?v=EPWv1V1w0n8"}
    ],
    "💃 신나는 댄스": [
        {"title": "SEVENTEEN - Super", "url": "https://www.youtube.com/watch?v=-GQg25oP0S4"},
        {"title": "TWICE - The Feels", "url": "https://www.youtube.com/watch?v=f5_wn8mexmM"},
        {"title": "PSY - DADDY", "url": "https://www.youtube.com/watch?v=FrG4TEcSuRg"}
    ],
    "🧘 집중/공부": [
        {"title": "Nujabes - Feather", "url": "https://www.youtube.com/watch?v=1st8a4QZQzM"},
        {"title": "(playlist) 노르웨이 숲으로 가자, 가사없는 노래", "url": "https://youtu.be/m876TGnxFxQ?si=zE0G6vCKjGsEDjWD"},
        {"title": "윤한 - Serenade", "url": "https://youtu.be/D4678C2QV50?si=i0ZbyNdyslaYafts"}
    ],
    "🚀 운동/드라이브": [
        {"title": "The Weeknd - Blinding Lights", "url": "https://www.youtube.com/watch?v=fHI8X4OXluQ"},
        {"title": "ITZY - WANNABE", "url": "https://www.youtube.com/watch?v=fE2h3lGlOsk"},
        {"title": "Calvin Harris - Summer", "url": "https://www.youtube.com/watch?v=ebXbLfLACGM"}
    ],
}

EMOJIS = {
    "😀 신남/행복": "😀",
    "😊 차분/따뜻": "😊",
    "😢 우울/위로": "😢",
    "😡 파워/분노해소": "😡",
    "😴 힐링/휴식": "😴",
    "😎 자신감/쿨": "😎",
    "💔 이별/감성": "💔",
    "💃 신나는 댄스": "💃",
    "🧘 집중/공부": "🧘",
    "🚀 운동/드라이브": "🚀",
}

if "history" not in st.session_state:
    st.session_state.history = []  # (mood_key, song)

# -----------------------------
# 무드 선택
# -----------------------------
st.markdown("""
<h2 style="color:#FF69B4; text-shadow: 2px 2px 5px white;">1) 오늘의 무드를 선택하세요 ✨</h2>
""", unsafe_allow_html=True)

mood_keys = list(EMOJIS.keys())
cols = st.columns(5)
selected_mood = st.session_state.get("selected_mood", mood_keys[0])

for i, key in enumerate(mood_keys):
    with cols[i % 5]:
        if st.button(f"{EMOJIS[key]} {key.split()[1]}", key=f"mood_{i}"):
            selected_mood = key
            st.session_state.selected_mood = key
            set_background(BACKGROUND_IMAGES[key])

st.markdown(f"<h4 style='color:white;'>선택된 무드: {EMOJIS[selected_mood]} {selected_mood}</h4>", unsafe_allow_html=True)

# -----------------------------
# 룰렛 돌리기
# -----------------------------
st.markdown("""
<hr style="border:2px solid #FF69B4;">
<h2 style="color:#FF69B4; text-shadow: 2px 2px 5px white;">2) 룰렛 돌리기 🎰</h2>
""", unsafe_allow_html=True)

placeholder = st.empty()

if st.button("룰렛 돌리기! 🎶"):
    pool = SONGS[selected_mood]
    for _ in range(15):
        s = random.choice(pool)
        placeholder.info(f"🎯 후보: **{s['title']}**")
        time.sleep(0.08)
    choice = random.choice(pool)
    st.session_state.history.append((selected_mood, choice))
    st.balloons()
    st.success(f"오늘의 추천곡은 ✨ **{choice['title']}** ✨")
    st.video(choice["url"])
    st.markdown(f"[👉 유튜브에서 듣기]({choice['url']})")

# -----------------------------
# 히스토리
# -----------------------------
if st.session_state.history:
    st.markdown("""
    <hr style="border:1px solid white;">
    <h3 style="color:#FF69B4;">📜 오늘의 추천 히스토리</h3>
    """, unsafe_allow_html=True)
    for mood, song in reversed(st.session_state.history[-10:]):
        st.markdown(f"<p style='color:white;'>{EMOJIS[mood]} <b>{mood}</b> → {song['title']}</p>", unsafe_allow_html=True)

# -----------------------------
# 사이드바: 사용자 커스텀 곡 추가
# -----------------------------
with st.sidebar:
    st.header("⚙️ 내 노래 추가")
    mood_for_add = st.selectbox("무드 선택", options=mood_keys)
    title_add = st.text_input("곡 제목 + 아티스트")
    url_add = st.text_input("유튜브 URL")
    if st.button("추가하기", key="add_song"):
        if mood_for_add and title_add and url_add:
            SONGS[mood_for_add].append({"title": title_add, "url": url_add})
            st.success("추가 완료! 이제 룰렛에 포함됩니다 🎉")
        else:
            st.warning("무드/제목/URL을 모두 입력해주세요.")
