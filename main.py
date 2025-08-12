import streamlit as st

# 페이지 설정
st.set_page_config(page_title="MBTI 직업 추천", page_icon="💼", layout="wide")

# CSS 스타일
st.markdown("""
    <style>
        body {
            background-color: #f0f4f8;
        }
        .big-title {
            font-size: 2.8em;
            font-weight: bold;
            color: #2E86C1;
            text-align: center;
            margin-bottom: 20px;
        }
        .job-card {
            background: linear-gradient(135deg, #ffffff, #f8f9fa);
            padding: 20px;
            border-radius: 20px;
            box-shadow: 0 6px 15px rgba(0,0,0,0.1);
            margin: 15px;
            text-align: center;
            transition: transform 0.3s ease;
        }
        .job-card:hover {
            transform: translateY(-5px);
        }
        .job-title {
            font-size: 1.4em;
            font-weight: bold;
            margin-top: 10px;
            color: #1B4F72;
        }
        .job-desc {
            font-size: 1em;
            color: #34495E;
            margin-top: 5px;
        }
        .job-major {
            font-size: 0.9em;
            color: #7D3C98;
            margin-top: 8px;
            font-style: italic;
        }
        img {
            border-radius: 15px;
        }
        .footer {
            text-align: center;
            font-size: 0.9em;
            color: gray;
            margin-top: 40px;
        }
    </style>
""", unsafe_allow_html=True)

# MBTI별 직업 데이터 (이미지 추가)
mbti_jobs = {
    "INTJ": [
        ("데이터 과학자", "복잡한 데이터를 분석해 의사결정을 돕는 전문가", "통계학, 컴퓨터공학", "https://images.unsplash.com/photo-1519389950473-47ba0277781c"),
        ("전략 컨설턴트", "기업의 장기 전략과 경쟁력 강화를 지원", "경영학, 경제학", "https://images.unsplash.com/photo-1551836022-deb4988cc6c4"),
        ("연구원", "새로운 지식을 탐구하고 기술을 개발", "자연과학, 공학", "https://images.unsplash.com/photo-1581091215367-59ab6b94d1a6")
    ],
    "ENTP": [
        ("마케팅 전문가", "창의적인 전략으로 제품과 브랜드 홍보", "광고홍보학, 경영학", "https://images.unsplash.com/photo-1557838923-2985c318be48"),
        ("기업가", "새로운 아이디어로 시장에 도전", "경영학, 창업학", "https://images.unsplash.com/photo-1542744173-8e7e53415bb0"),
        ("프로젝트 매니저", "팀을 이끌어 목표를 달성하는 책임자", "경영학, 산업공학", "https://images.unsplash.com/photo-1503387762-592deb58ef4e")
    ],
    "INFJ": [
        ("심리상담사", "개인의 심리적 어려움을 돕는 전문가", "심리학, 상담학", "https://images.unsplash.com/photo-1588072432836-e10032774350"),
        ("작가", "창의적인 이야기와 콘텐츠를 만드는 사람", "문예창작학, 국문학", "https://images.unsplash.com/photo-1529070538774-1843cb3265df"),
        ("교사", "지식과 가치관을 학생들에게 전달", "교육학, 전공 과목 관련 학문", "https://images.unsplash.com/photo-1588072432836-e10032774350")
    ],
    "ESFP": [
        ("배우", "연기와 표현으로 대중과 소통", "연극영화학, 공연예술학", "https://images.unsplash.com/photo-1485846234645-a62644f84728"),
        ("여행 가이드", "여행지를 안내하고 문화 전달", "관광학, 외국어", "https://images.unsplash.com/photo-1507525428034-b723cf961d3e"),
        ("이벤트 기획자", "행사와 축제를 기획·운영", "이벤트경영학, 마케팅학", "https://images.unsplash.com/photo-1503424886306-24b6f3e7d0ff")
    ]
}

# 제목
st.markdown('<div class="big-title">💼 MBTI 기반 직업 추천</div>', unsafe_allow_html=True)
st.write("당신의 MBTI를 선택하면 어울리는 직업과 관련 전공을 추천해드립니다! 🎯")

# MBTI 선택
selected_mbti = st.selectbox("MBTI를 선택하세요", list(mbti_jobs.keys()))

# 풍선 효과
if selected_mbti:
    st.balloons()

# 직업 카드 출력
if selected_mbti:
    st.subheader(f"📌 {selected_mbti} 유형 추천 직업")
    cols = st.columns(3)  # 3열 배치

    jobs = mbti_jobs[selected_mbti]
    for i, (job, desc, major, img_url) in enumerate(jobs):
        with cols[i % 3]:
            st.markdown(f"""
                <div class="job-card">
                    <img src="{img_url}" width="100%" height="auto">
                    <div class="job-title">✨ {job}</div>
                    <div class="job-desc">📖 {desc}</div>
                    <div class="job-major">🎓 관련 전공: {major}</div>
                </div>
            """, unsafe_allow_html=True)

# 하단 문구
st.markdown('<div class="footer">© 2025 MBTI Career Guide | Designed with ❤️ in Streamlit</div>', unsafe_allow_html=True)
