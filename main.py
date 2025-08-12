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

# MBTI별 직업 데이터 (직업, 설명, 전공, 이미지)
mbti_jobs = {
    "INTJ": [
        ("데이터 과학자", "복잡한 데이터를 분석해 의사결정을 돕는 전문가", "통계학, 컴퓨터공학", "https://images.unsplash.com/photo-1519389950473-47ba0277781c"),
        ("전략 컨설턴트", "기업의 장기 전략과 경쟁력 강화를 지원", "경영학, 경제학", "https://images.unsplash.com/photo-1551836022-deb4988cc6c4"),
        ("연구원", "새로운 지식을 탐구하고 기술을 개발", "자연과학, 공학", "https://images.unsplash.com/photo-1581091215367-59ab6b94d1a6")
    ],
    "INTP": [
        ("연구원", "이론과 실험을 통해 새로운 지식을 창출", "물리학, 컴퓨터공학", "https://images.unsplash.com/photo-1505664063603-28e48ca204eb"),
        ("AI 개발자", "인공지능 알고리즘과 시스템을 개발", "인공지능, 컴퓨터공학", "https://images.unsplash.com/photo-1581090700227-4c4f50b56c7d"),
        ("이론 물리학자", "자연 현상의 근본 원리를 연구", "물리학, 수학", "https://images.unsplash.com/photo-1554475901-4538ddfbccc2")
    ],
    "ENTJ": [
        ("경영 컨설턴트", "기업 운영 전략을 설계·개선", "경영학, 경제학", "https://images.unsplash.com/photo-1551836022-deb4988cc6c4"),
        ("기업 임원", "조직을 이끌어 성과 창출", "경영학, 리더십학", "https://images.unsplash.com/photo-1520607162513-77705c0f0d4a"),
        ("벤처 창업가", "혁신적인 아이디어로 사업 창출", "창업학, 마케팅학", "https://images.unsplash.com/photo-1542744173-8e7e53415bb0")
    ],
    "ENTP": [
        ("마케팅 전문가", "창의적인 전략으로 제품과 브랜드 홍보", "광고홍보학, 경영학", "https://images.unsplash.com/photo-1557838923-2985c318be48"),
        ("기업가", "새로운 아이디어로 시장에 도전", "경영학, 창업학", "https://images.unsplash.com/photo-1542744173-8e7e53415bb0"),
        ("프로젝트 매니저", "팀을 이끌어 목표를 달성하는 책임자", "경영학, 산업공학", "https://images.unsplash.com/photo-1503387762-592deb58ef4e")
    ],
    "INFJ": [
        ("심리상담사", "개인의 심리적 어려움을 돕는 전문가", "심리학, 상담학", "https://images.unsplash.com/photo-1588072432836-e10032774350"),
        ("작가", "창의적인 이야기와 콘텐츠를 만드는 사람", "문예창작학, 국문학", "https://images.unsplash.com/photo-1529070538774-1843cb3265df"),
        ("교사", "지식과 가치관을 학생들에게 전달", "교육학, 전공 과목", "https://images.unsplash.com/photo-1596495577886-d920f1fb7238")
    ],
    "INFP": [
        ("소설가", "창의적인 이야기와 캐릭터를 창조", "문예창작학, 국문학", "https://images.unsplash.com/photo-1507842217343-583bb7270b66"),
        ("예술가", "감정과 아이디어를 시각적·청각적으로 표현", "미술학, 음악학", "https://images.unsplash.com/photo-1504198453319-5ce911bafcde"),
        ("심리상담사", "마음을 이해하고 치유를 돕는 전문가", "심리학, 상담학", "https://images.unsplash.com/photo-1588072432836-e10032774350")
    ],
    "ENFJ": [
        ("HR 매니저", "조직의 인재 채용과 육성을 담당", "인사관리학, 경영학", "https://images.unsplash.com/photo-1581092334808-898d9f46c9c9"),
        ("강사", "전문 지식을 강의하고 지도", "교육학, 전공 분야", "https://images.unsplash.com/photo-1596495577886-d920f1fb7238"),
        ("홍보 전문가", "브랜드와 기업 이미지를 관리·향상", "홍보학, 커뮤니케이션학", "https://images.unsplash.com/photo-1557838923-2985c318be48")
    ],
    "ENFP": [
        ("광고 기획자", "창의적인 광고 캠페인을 설계", "광고홍보학, 마케팅학", "https://images.unsplash.com/photo-1522199710521-72d69614c702"),
        ("콘텐츠 크리에이터", "온라인 콘텐츠를 제작·배포", "미디어학, 디자인학", "https://images.unsplash.com/photo-1522202176988-66273c2fd55f"),
        ("여행 작가", "세계 각지를 여행하며 글과 사진 기록", "문예창작학, 관광학", "https://images.unsplash.com/photo-1507525428034-b723cf961d3e")
    ],
    "ISTJ": [
        ("회계사", "재무 기록을 관리하고 분석", "회계학, 경영학", "https://images.unsplash.com/photo-1554224155-8d04cb21cd6c"),
        ("행정 공무원", "정부 조직 운영과 정책 집행", "행정학, 법학", "https://images.unsplash.com/photo-1538688423619-a81d3f23454b"),
        ("품질 관리 전문가", "제품과 서비스 품질 유지·개선", "산업공학, 품질경영학", "https://images.unsplash.com/photo-1581090700227-4c4f50b56c7d")
    ],
    "ISFJ": [
        ("간호사", "환자의 건강과 회복을 돕는 전문가", "간호학", "https://images.unsplash.com/photo-1580281657521-13b06c5f7b6b"),
        ("교사", "학생들에게 지식과 인성을 교육", "교육학, 전공 과목", "https://images.unsplash.com/photo-1596495577886-d920f1fb7238"),
        ("도서관 사서", "도서와 자료를 관리하고 안내", "문헌정보학", "https://images.unsplash.com/photo-1588072432836-e10032774350")
    ],
    "ESTJ": [
        ("군 장교", "군의 전략과 부대를 지휘", "군사학, 경영학", "https://images.unsplash.com/photo-1607013251379-e6eecfffe234"),
        ("프로젝트 매니저", "팀과 자원을 효율적으로 관리", "산업공학, 경영학", "https://images.unsplash.com/photo-1503387762-592deb58ef4e"),
        ("은행원", "금융 서비스 제공과 고객 상담", "경제학, 금융학", "https://images.unsplash.com/photo-1563013544-824ae1b704d3")
    ],
    "ESFJ": [
        ("영양사", "식단을 설계하고 영양 관리", "영양학, 식품학", "https://images.unsplash.com/photo-1600891964599-f61ba0e24092"),
        ("고객 서비스 매니저", "고객 만족과 서비스 품질 관리", "경영학, 마케팅학", "https://images.unsplash.com/photo-1563013544-824ae1b704d3"),
        ("학교 교사", "교육과 학급 운영 담당", "교육학, 전공 과목", "https://images.unsplash.com/photo-1596495577886-d920f1fb7238")
    ],
    "ISTP": [
        ("기계 엔지니어", "기계 설계와 제작", "기계공학", "https://images.unsplash.com/photo-1581091215367-59ab6b94d1a6"),
        ("파일럿", "항공기를 안전하게 운항", "항공운항학", "https://images.unsplash.com/photo-1529070538774-1843cb3265df"),
        ("응급 구조사", "응급 상황에서 생명을 구하는 전문가", "응급구조학", "https://images.unsplash.com/photo-1580281657521-13b06c5f7b6b")
    ],
    "ISFP": [
        ("그래픽 디자이너", "시각적 콘텐츠 제작", "디자인학, 시각디자인", "https://images.unsplash.com/photo-1505691938895-1758d7feb511"),
        ("사진작가", "사진 촬영과 편집", "사진학, 시각예술", "https://images.unsplash.com/photo-1504198453319-5ce911bafcde"),
        ("음악가", "음악 창작과 공연", "음악학", "https://images.unsplash.com/photo-1511671782779-c97d3d27a1d4")
    ],
    "ESTP": [
        ("세일즈 매니저", "제품·서비스 판매 전략 수립", "마케팅학, 경영학", "https://images.unsplash.com/photo-1503387762-592deb58ef4e"),
        ("운동선수", "경기에 참여하고 팀을 대표", "체육학", "https://images.unsplash.com/photo-1517649763962-0c623066013b"),
        ("이벤트 플래너", "행사와 이벤트 기획", "이벤트경영학", "https://images.unsplash.com/photo-1503424886306-24b6f3e7d0ff")
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
