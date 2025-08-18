import streamlit as st
import random
import time

st.set_page_config(page_title="무드 기반 랜덤 음악 룰렛", page_icon="🎵", layout="wide")

# 배경 이미지 및 스타일
page_bg = """
<style>
[data-testid="stAppViewContainer"] {
    background-image: url("https://images.unsplash.com/photo-1507874457470-272b3c8d8ee2");
    background-size: cover;
    background-position: center;
    background-attachment: fixed;
}
[data-testid="stHeader"] {
    background: rgba(0,0,0,0);
}
[data-testid="stSidebar"] {
    background: rgba(255, 255, 255, 0.8);
    backdrop-filter: blur(10px);
    border-radius: 12px;
}
</style>
"""

st.markdown(page_bg, unsafe_allow_html=True)

st.markdown("""
<div style="text-align:center; padding:20px; background:rgba(0,0,0,0.5); border-radius:15px;">
    <h1 style="color:#FFD700; font-size:3em;">🎵 무드 기반 랜덤 음악 룰렛 🎰</h1>
    <p style="color:white; font-size:1.2em;">얼굴 이모지로 <b>오늘의 무드</b>를 고르면,<br> 그 분위기에 맞는 노래를 랜덤 추천해드려요! 🎶<br>유튜브 영상까지 바로 감상 가능!</p>
</div>
""", unsafe_allow_html=True)

# -----------------------------
# 데이터: 무드별 추천 곡 리스트
# -----------------------------
SONGS = {
    "😀 신남/행복": [
        {"title": "NewJeans - Super Shy", "url": "https://www.youtube.com/watch?v=ArmDp-zijuc"},
        {"title": "IVE - IAM", "url": "https://www.youtube.com/watch?v=6ZUIwj3FgUY"},
        {"title": "Pharrell Williams - Happy", "url": "https://www.youtube.com/watch?v=ZbZSe6N_BXs"},
        {"title": "BTS - Dynamite", "url": "https://www.youtube.com/watch?v=gdZLi9oWNZg"},
        {"title": "Kirinji - Almond Eye (Remaster)", "url": "https://www.youtube.com/watch?v=3CqkYt2_9dU"}
    ],
    "😊 차분/따뜻": [
        {"title": "AKMU - 어떻게 이별까지 사랑하겠어, 널 사랑하는 거지", "url": "https://www.youtube.com/watch?v=ZKAmmaQ9iQk"},
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
        {"title": "(G)I-DLE - QUEENCARD", "url": "https://www.youtube.com/watch?v=6fT7Kx9G4b0"},
        {"title": "Stray Kids - Thunderous", "url": "https://www.youtube.com/watch?v=EaswWiwMVs8"}
    ],
    "😴 힐링/휴식": [
        {"title": "LOFI Girl - lofi hip hop radio", "url": "https://www.youtube.com/watch?v=jfKfPfyJRdk"},
        {"title": "BTS - Spring Day (봄날)", "url": "https://www.youtube.com/watch?v=xEeFrLSkMm8"},
        {"title": "Crush - 가끔", "url": "https://www.youtube.com/watch?v=2Gm_PfUq9w8"},
        {"title": "Sigur Rós - Hoppípolla", "url": "https://www.youtube.com/watch?v=hnAwPeqrdAk"}
    ],
    "😎 자신감/쿨": [
        {"title": "BLACKPINK - DDU-DU DDU-DU", "url": "https://www.youtube.com/watch?v=IHNzOHi8sJs"},
        {"title": "Dua Lipa - Don't Start Now", "url": "https://www.youtube.com/watch?v=oygrmJFKYZY"},
        {"title": "LE SSERAFIM - ANTIFRAGILE", "url": "https://www.youtube.com/watch?v=pyf8cbqyfPs"},
        {"title": "Charlie Puth - Attention", "url": "https://www.youtube.com/watch?v=nfs8NYg7yQM"}
    ],
    "💔 이별/감성": [
        {"title": "태연 - 그대라는 시", "url": "https://www.youtube.com/watch?v=Cg8sDCf-3MM"},
        {"title": "10CM - 사랑은 은하수 다방에서", "url": "https://www.youtube.com/watch?v=K8P8M2wsE1g"},
        {"title": "Anne-Marie - 2002", "url": "https://www.youtube.com/watch?v=Il-an3K9pjg"},
        {"title": "정승환 - 눈사람", "url": "https://www.youtube.com/watch?v=EPWv1V1w0n8"}
    ],
    "💃 신나는 댄스": [
        {"title": "SEVENTEEN - Super", "url": "https://www.youtube.com/watch?v=-GQg25oP0S4"},
        {"title": "TWICE - The Feels", "url": "https://www.youtube.com/watch?v=f5_wn8mexmM"},
        {"title": "PSY - DADDY", "url": "https://www.youtube.com/watch?v=FrG4TEcSuRg"},
        {"title": "ZEDD, Maren Morris - The Middle", "url": "https://www.youtube.com/watch?v=M3mJkSqZbX4"}
    ],
    "🧘 집중/공부": [
        {"title": "Monstercat Silk - Focus Playlist", "url": "https://www.youtube.com/watch?v=i7U7s3P9Gk8"},
        {"title": "Nujabes - Feather", "url": "https://www.youtube.com/watch?v=1st8a4QZQzM"},
        {"title": "Lo-fi beats to study", "url": "https://www.youtube.com/watch?v=5qap5aO4i9A"},
        {"title": "윤한 - Serenade", "url": "https://www.youtube.com/watch?v=0kKQfX0A9yM"}
    ],
    "🚀 운동/드라이브": [
        {"title": "The Weeknd - Blinding Lights", "url": "https://www.youtube.com/watch?v=fHI8X4OXluQ"},
        {"title": "ITZY - WANNABE", "url": "https://www.youtube.com/watch?v=fE2h3lGlOsk"},
        {"title": "Calvin Harris - Summer", "url": "https://www.youtube.com/watch?v=ebXbLfLACGM"},
        {"title": "Jvke - golden hour", "url": "https://www.youtube.com/watch?v=PEM0Vs8jf1w"}
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

# 세션 상태
if "history" not in st.session_state:
    st.session_state.history = []  # (mood_key, song)

st.markdown("""
<h2 style="color:#FFD700; text-shadow: 2px 2px 5px black;">1) 오늘의 무드를 선택하세요 ✨</h2>
""", unsafe_allow_html=True)

# 이모지 선택 그리드
mood_keys = list(EMOJIS.keys())
cols = st.columns(5)
selected_mood = st.session_state.get("selected_mood", mood_keys[0])

for i, key in enumerate(mood_keys):
    with cols[i % 5]:
        if st.button(f"{EMOJIS[key]} {key.split()[1]}", key=f"mood_{i}"):
            selected_mood = key
            st.session_state.selected_mood = key

st.markdown(f"<h4 style='color:white;'>선택된 무드: {EMOJIS[selected_mood]} {selected_mood}</h4>", unsafe_allow_html=True)

st.markdown("""
<hr style="border:2px solid #FFD700;">
<h2 style="color:#FFD700; text-shadow: 2px 2px 5px black;">2) 룰렛 돌리기 🎰</h2>
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

# 히스토리 표시
if st.session_state.history:
    st.markdown("""
    <hr style="border:1px solid white;">
    <h3 style="color:#FFD700;">📜 오늘의 추천 히스토리</h3>
    """, unsafe_allow_html=True)
    for mood, song in reversed(st.session_state.history[-10:]):
        st.markdown(f"<p style='color:white;'>{EMOJIS[mood]} <b>{mood}</b> → {song['title']}</p>", unsafe_allow_html=True)

# 사이드바: 사용자 커스텀 곡 추가
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
