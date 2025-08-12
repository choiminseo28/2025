import streamlit as st

# MBTI별 직업 추천 데이터
mbti_jobs = {
    "INTJ": ["데이터 과학자", "전략 컨설턴트", "연구원", "시스템 분석가"],
    "INTP": ["연구원", "소프트웨어 엔지니어", "AI 개발자", "이론 물리학자"],
    "ENTJ": ["경영 컨설턴트", "프로젝트 매니저", "기업 임원", "벤처 창업가"],
    "ENTP": ["마케팅 전문가", "기업가", "기획자", "혁신 컨설턴트"],
    "INFJ": ["심리상담사", "작가", "교사", "사회복지사"],
    "INFP": ["소설가", "심리상담사", "예술가", "교육자"],
    "ENFJ": ["HR 매니저", "강사", "커뮤니티 매니저", "홍보 전문가"],
    "ENFP": ["광고 기획자", "콘텐츠 크리에이터", "이벤트 기획자", "여행 작가"],
    "ISTJ": ["회계사", "행정 공무원", "변호사", "품질 관리 전문가"],
    "ISFJ": ["간호사", "교사", "도서관 사서", "사회복지사"],
    "ESTJ": ["군 장교", "프로젝트 매니저", "경영 관리자", "은행원"],
    "ESFJ": ["간호사", "영양사", "고객 서비스 매니저", "학교 교사"],
    "ISTP": ["기계 엔지니어", "파일럿", "응급 구조사", "수리 기술자"],
    "ISFP": ["그래픽 디자이너", "사진작가", "플로리스트", "음악가"],
    "ESTP": ["세일즈 매니저", "이벤트 플래너", "운동선수", "응급 구조사"],
    "ESFP": ["배우", "여행 가이드", "이벤트 기획자", "방송 진행자"],
}

st.set_page_config(page_title="MBTI 직업 추천", page_icon="💼", layout="centered")

st.title("💼 MBTI 기반 직업 추천")
st.write("당신의 MBTI를 선택하면 어울리는 직업을 추천해드립니다.")

# MBTI 선택
mbti_list = list(mbti_jobs.keys())
selected_mbti = st.selectbox("MBTI를 선택하세요", mbti_list)

# 추천 결과 출력
if selected_mbti:
    st.subheader(f"📌 {selected_mbti} 유형 추천 직업")
    for job in mbti_jobs[selected_mbti]:
        st.write(f"- {job}")

