import streamlit as st

# ─────────────────────────────────────────────
# 페이지 기본 설정
# ─────────────────────────────────────────────
st.set_page_config(
    page_title="MBTI 철학자 매칭소",
    page_icon="🏛️",
    layout="centered",
)

# ─────────────────────────────────────────────
# 커스텀 CSS (현학적이고 세련된 분위기)
# ─────────────────────────────────────────────
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@400;600;700&family=Noto+Serif+KR:wght@400;600&display=swap');
    
    .stApp {
        background: linear-gradient(135deg, #1a1a2e 0%, #16213e 50%, #0f3460 100%);
    }
    
    h1, h2, h3 {
        font-family: 'Cormorant Garamond', 'Noto Serif KR', serif !important;
        color: #f5e6c8 !important;
        text-align: center;
    }
    
    .main-title {
        font-size: 3.2rem;
        font-weight: 700;
        text-align: center;
        background: linear-gradient(90deg, #d4af37, #f5e6c8, #d4af37);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 0.5rem;
        letter-spacing: 2px;
    }
    
    .subtitle {
        text-align: center;
        color: #b8b8d1;
        font-style: italic;
        font-family: 'Cormorant Garamond', serif;
        font-size: 1.2rem;
        margin-bottom: 2rem;
    }
    
    .philosopher-card {
        background: rgba(245, 230, 200, 0.08);
        border: 1px solid rgba(212, 175, 55, 0.3);
        border-radius: 15px;
        padding: 2rem;
        margin-top: 1.5rem;
        backdrop-filter: blur(10px);
        box-shadow: 0 8px 32px rgba(0, 0, 0, 0.3);
    }
    
    .philosopher-name {
        font-family: 'Cormorant Garamond', serif;
        font-size: 2.5rem;
        color: #d4af37;
        text-align: center;
        margin-bottom: 0.5rem;
    }
    
    .philosopher-era {
        text-align: center;
        color: #b8b8d1;
        font-style: italic;
        margin-bottom: 1.5rem;
    }
    
    .quote {
        font-family: 'Cormorant Garamond', serif;
        font-size: 1.3rem;
        font-style: italic;
        color: #f5e6c8;
        text-align: center;
        padding: 1rem;
        border-left: 3px solid #d4af37;
        border-right: 3px solid #d4af37;
        margin: 1.5rem 0;
    }
    
    .description {
        color: #e0e0e0;
        line-height: 1.8;
        font-size: 1.05rem;
        font-family: 'Noto Serif KR', serif;
    }
    
    .stSelectbox label {
        color: #f5e6c8 !important;
        font-family: 'Cormorant Garamond', serif;
        font-size: 1.2rem !important;
    }
    
    div[data-testid="stMarkdownContainer"] p {
        color: #e0e0e0;
    }
    </style>
""", unsafe_allow_html=True)

# ─────────────────────────────────────────────
# 철학자 데이터
# ─────────────────────────────────────────────
philosophers = {
    "INTJ": {
        "name": "프리드리히 니체",
        "emoji": "⚡🦅",
        "era": "독일 · 1844–1900 · 실존주의",
        "quote": "그대의 운명을 사랑하라(Amor Fati).",
        "desc": "전략적 사고와 깊은 통찰을 지닌 INTJ에게는 기존 가치를 전복하고 '초인(Übermensch)'을 꿈꾼 니체가 어울립니다. 그의 망치를 든 철학은 INTJ의 독립적이고 비판적인 정신과 공명합니다."
    },
    "INTP": {
        "name": "임마누엘 칸트",
        "emoji": "🧭📐",
        "era": "독일 · 1724–1804 · 비판철학",
        "quote": "내 위의 별이 빛나는 하늘과, 내 안의 도덕법칙.",
        "desc": "논리와 체계를 사랑하는 INTP에게는 인식의 한계와 이성의 구조를 정밀하게 분석한 칸트가 제격입니다. 그의 『순수이성비판』은 INTP가 평생 음미할 사유의 정원입니다."
    },
    "ENTJ": {
        "name": "니콜로 마키아벨리",
        "emoji": "♟️👑",
        "era": "이탈리아 · 1469–1527 · 정치철학",
        "quote": "목적이 수단을 정당화한다.",
        "desc": "타고난 지도자 ENTJ에게는 현실 정치의 냉철한 분석가 마키아벨리가 어울립니다. 『군주론』의 실용적 권력론은 ENTJ의 전략적 야망과 깊이 호응합니다."
    },
    "ENTP": {
        "name": "소크라테스",
        "emoji": "💬🏛️",
        "era": "고대 그리스 · BC 470–399 · 산파술",
        "quote": "나는 내가 아무것도 모른다는 것을 안다.",
        "desc": "끊임없는 질문과 토론을 즐기는 ENTP에게는 산파술로 진리를 캐묻던 소크라테스가 운명적 동반자입니다. 아테네 광장에서의 그의 변증은 ENTP의 지적 유희 그 자체입니다."
    },
    "INFJ": {
        "name": "쇠렌 키르케고르",
        "emoji": "🕯️🌌",
        "era": "덴마크 · 1813–1855 · 실존주의",
        "quote": "불안은 자유의 현기증이다.",
        "desc": "내면의 깊이와 통찰을 지닌 INFJ에게는 실존의 고독과 신앙의 도약을 탐구한 키르케고르가 어울립니다. 그의 고독한 사색은 INFJ의 영혼과 공명합니다."
    },
    "INFP": {
        "name": "장 자크 루소",
        "emoji": "🌿✒️",
        "era": "프랑스 · 1712–1778 · 계몽주의",
        "quote": "인간은 자유롭게 태어났으나, 어디서나 사슬에 묶여 있다.",
        "desc": "이상주의자 INFP에게는 자연 상태의 순수함과 인간의 본래적 선함을 노래한 루소가 어울립니다. 그의 『고백록』은 INFP의 내면 일기와 닮아 있습니다."
    },
    "ENFJ": {
        "name": "공자",
        "emoji": "📜🍃",
        "era": "고대 중국 · BC 551–479 · 유가",
        "quote": "자기가 원치 않는 바를 남에게 베풀지 말라.",
        "desc": "사람을 이끌고 조화를 이루는 ENFJ에게는 인(仁)과 예(禮)로 공동체의 윤리를 설계한 공자가 어울립니다. 그의 가르침은 ENFJ의 따뜻한 리더십에 깊이를 더합니다."
    },
    "ENFP": {
        "name": "장 폴 사르트르",
        "emoji": "🚬🗽",
        "era": "프랑스 · 1905–1980 · 실존주의",
        "quote": "실존은 본질에 앞선다.",
        "desc": "자유로운 영혼 ENFP에게는 인간의 절대적 자유와 책임을 선언한 사르트르가 어울립니다. '인간은 자유라는 형벌에 처해졌다'는 그의 외침은 ENFP의 열정과 닮았습니다."
    },
    "ISTJ": {
        "name": "아리스토텔레스",
        "emoji": "📚⚖️",
        "era": "고대 그리스 · BC 384–322 · 형이상학",
        "quote": "우리가 반복적으로 하는 행위가 곧 우리 자신이다.",
        "desc": "성실하고 체계적인 ISTJ에게는 모든 학문을 분류하고 체계화한 아리스토텔레스가 어울립니다. 중용(中庸)의 윤리학은 ISTJ의 균형 잡힌 삶의 태도와 통합니다."
    },
    "ISFJ": {
        "name": "맹자",
        "emoji": "🌱🤲",
        "era": "고대 중국 · BC 372–289 · 유가",
        "quote": "측은지심은 인(仁)의 단서이다.",
        "desc": "헌신적이고 따뜻한 ISFJ에게는 인간의 본성이 본래 선하다고 믿은 맹자가 어울립니다. 사단(四端)의 가르침은 ISFJ의 보살핌의 정서와 깊이 공명합니다."
    },
    "ESTJ": {
        "name": "토머스 홉스",
        "emoji": "🛡️📕",
        "era": "영국 · 1588–1679 · 사회계약론",
        "quote": "만인의 만인에 대한 투쟁.",
        "desc": "질서와 규율을 중시하는 ESTJ에게는 『리바이어던』으로 강력한 사회계약을 설계한 홉스가 어울립니다. 그의 현실적 정치철학은 ESTJ의 실용주의와 만납니다."
    },
    "ESFJ": {
        "name": "데이비드 흄",
        "emoji": "🤝☕",
        "era": "스코틀랜드 · 1711–1776 · 경험론",
        "quote": "이성은 정념의 노예이며, 그래야만 한다.",
        "desc": "공감과 관계를 중시하는 ESFJ에게는 도덕의 근원을 '공감(sympathy)'에서 찾은 흄이 어울립니다. 그의 따뜻한 경험론은 ESFJ의 인간애와 맞닿아 있습니다."
    },
    "ISTP": {
        "name": "디오게네스",
        "emoji": "🏺🐕",
        "era": "고대 그리스 · BC 412–323 · 견유학파",
        "quote": "햇빛을 가리지 말고 비켜서 주시오.",
        "desc": "실용적이고 자유로운 ISTP에게는 통 속에 살며 모든 권위를 비웃은 디오게네스가 어울립니다. 그의 본질주의적 단순함은 ISTP의 미니멀한 정신과 통합니다."
    },
    "ISFP": {
        "name": "노자",
        "emoji": "🌊☯️",
        "era": "고대 중국 · BC 6세기경 · 도가",
        "quote": "최상의 선은 물과 같다(上善若水).",
        "desc": "고요하고 예술적인 ISFP에게는 무위자연(無爲自然)을 노래한 노자가 어울립니다. 흐르는 물과 같은 그의 사상은 ISFP의 부드러운 감수성과 깊이 공명합니다."
    },
    "ESTP": {
        "name": "에피쿠로스",
        "emoji": "🍇🌅",
        "era": "고대 그리스 · BC 341–270 · 쾌락주의",
        "quote": "현명하게, 훌륭하게, 정의롭게 살지 않고는 즐겁게 살 수 없다.",
        "desc": "현재를 즐기는 ESTP에게는 '아타락시아(평정심)'와 절제된 쾌락을 추구한 에피쿠로스가 어울립니다. 그의 정원학파는 ESTP의 감각적 지혜를 일깨웁니다."
    },
    "ESFP": {
        "name": "장자",
        "emoji": "🦋🎭",
        "era": "고대 중국 · BC 369–286 · 도가",
        "quote": "내가 나비인가, 나비가 나인가.",
        "desc": "자유롭고 유쾌한 ESFP에게는 호접지몽(胡蝶之夢)의 장자가 어울립니다. 경계를 넘나드는 그의 상상력과 소요유(逍遙遊)의 정신은 ESFP의 삶 그 자체입니다."
    },
}

# ─────────────────────────────────────────────
# 메인 UI
# ─────────────────────────────────────────────
st.markdown('<div class="main-title">🏛️ MBTI 철학자 매칭소 🏛️</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">— Philosophia, Speculum Animae —<br><span style="font-size:0.95rem;">당신의 영혼을 비추는 철학의 거울</span></div>', unsafe_allow_html=True)

st.markdown("---")

mbti_list = ["선택하세요"] + sorted(philosophers.keys())

selected = st.selectbox(
    "✨ 당신의 MBTI를 선택하세요",
    mbti_list,
)

if selected != "선택하세요":
    p = philosophers[selected]
    
    st.markdown(f"""
        <div class="philosopher-card">
            <div style="text-align:center; font-size:3rem; margin-bottom:0.5rem;">{p['emoji']}</div>
            <div class="philosopher-name">{p['name']}</div>
            <div class="philosopher-era">{p['era']}</div>
            <div class="quote">“{p['quote']}”</div>
            <div class="description">{p['desc']}</div>
        </div>
    """, unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown(
        f'<div style="text-align:center; color:#d4af37; font-family:Cormorant Garamond, serif; font-style:italic; font-size:1.1rem;">— {selected} 유형이여, {p["name"]}의 사유와 동행하시길 —</div>',
        unsafe_allow_html=True
    )

st.markdown("---")
st.markdown(
    '<div style="text-align:center; color:#8888aa; font-size:0.85rem; font-style:italic;">🪶 Sapere aude — 감히 알려고 하라. (Kant)</div>',
    unsafe_allow_html=True
)
