import streamlit as st
# ─────────────────────────────────────────────
# 페이지 설정
# ─────────────────────────────────────────────
st.set_page_config(
    page_title="MBTI 문화예술 큐레이션",
    page_icon="🎨",
    layout="centered",
)

# ─────────────────────────────────────────────
# 세션 상태 초기화
# ─────────────────────────────────────────────
if "page" not in st.session_state:
    st.session_state.page = 0  # 0: MBTI선택, 1: 고전, 2: 현대, 3: 예술가

# ─────────────────────────────────────────────
# MBTI 인구 비율 데이터 (16Personalities 기준 대략치)
# ─────────────────────────────────────────────
mbti_ratio = {
    "ISTJ": 11.6, "ISFJ": 13.8, "INFJ": 1.5, "INTJ": 2.1,
    "ISTP": 5.4,  "ISFP": 8.8,  "INFP": 4.4, "INTP": 3.3,
    "ESTP": 4.3,  "ESFP": 8.5,  "ENFP": 8.1, "ENTP": 3.2,
    "ESTJ": 8.7,  "ESFJ": 12.3, "ENFJ": 2.5, "ENTJ": 1.8,
}

# ─────────────────────────────────────────────
# MBTI별 추천 데이터
# ─────────────────────────────────────────────
recommendations = {
    "INTJ": {
        "classic": {
            "title": "죄와 벌",
            "author": "표도르 도스토옙스키 (1866)",
            "desc": "라스콜니코프의 치밀한 사상과 내면의 붕괴를 그린 심리 소설. 자신만의 논리로 세계를 재구성하려는 INTJ의 사유와 깊이 공명합니다.",
            "imgs": ["https://images.unsplash.com/photo-1519682337058-a94d519337bc?w=1200",
                     "https://images.unsplash.com/photo-1532012197267-da84d127e765?w=800",
                     "https://images.unsplash.com/photo-1457369804613-52c61a468e7d?w=400"]
        },
        "modern": {
            "title": "1984",
            "author": "조지 오웰 (1949)",
            "desc": "전체주의 사회를 꿰뚫는 날카로운 통찰. 시스템의 본질을 간파하는 INTJ의 비판적 시선과 맞닿아 있습니다.",
            "imgs": ["https://images.unsplash.com/photo-1495020689067-958852a7765e?w=1200",
                     "https://images.unsplash.com/photo-1481627834876-b7833e8f5570?w=800",
                     "https://images.unsplash.com/photo-1457369804613-52c61a468e7d?w=400"]
        },
        "artist": {
            "name": "M.C. 에셔",
            "era": "네덜란드 · 1898–1972",
            "desc": "수학적 정밀함과 무한한 사유의 미로. 논리와 상상의 경계를 허무는 에셔의 세계는 INTJ의 정신구조 그 자체입니다.",
            "style": "geometric",
            "imgs": ["https://images.unsplash.com/photo-1507908708918-778587c9e563?w=1200",
                     "https://images.unsplash.com/photo-1550684848-fac1c5b4e853?w=800",
                     "https://images.unsplash.com/photo-1561839561-b13bcfe95249?w=400"]
        }
    },
    "INTP": {
        "classic": {
            "title": "파우스트",
            "author": "요한 볼프강 폰 괴테 (1808)",
            "desc": "모든 지식을 갈망하는 학자의 영혼. 진리를 향한 끝없는 탐구심은 INTP의 본질입니다.",
            "imgs": ["https://images.unsplash.com/photo-1457369804613-52c61a468e7d?w=1200",
                     "https://images.unsplash.com/photo-1519682337058-a94d519337bc?w=800",
                     "https://images.unsplash.com/photo-1532012197267-da84d127e765?w=400"]
        },
        "modern": {
            "title": "이방인",
            "author": "알베르 카뮈 (1942)",
            "desc": "부조리한 세계를 관조하는 뫼르소. 감정보다 인식이 앞서는 INTP의 시선과 닮았습니다.",
            "imgs": ["https://images.unsplash.com/photo-1481627834876-b7833e8f5570?w=1200",
                     "https://images.unsplash.com/photo-1495020689067-958852a7765e?w=800",
                     "https://images.unsplash.com/photo-1457369804613-52c61a468e7d?w=400"]
        },
        "artist": {
            "name": "레오나르도 다 빈치",
            "era": "이탈리아 · 1452–1519",
            "desc": "그림, 해부학, 공학을 넘나든 만능 천재. 모든 분야를 호기심으로 탐구한 다 빈치는 INTP의 이상형입니다.",
            "style": "renaissance",
            "imgs": ["https://images.unsplash.com/photo-1577720580479-7d839d829c73?w=1200",
                     "https://images.unsplash.com/photo-1578321272176-b7bbc0679853?w=800",
                     "https://images.unsplash.com/photo-1554907984-15263bfd63bd?w=400"]
        }
    },
    "ENTJ": {
        "classic": {
            "title": "전쟁과 평화",
            "author": "레프 톨스토이 (1869)",
            "desc": "역사의 거대한 흐름 속 인간 군상의 서사시. 큰 그림을 그리는 ENTJ의 통찰력과 만납니다.",
            "imgs": ["https://images.unsplash.com/photo-1519682337058-a94d519337bc?w=1200",
                     "https://images.unsplash.com/photo-1532012197267-da84d127e765?w=800",
                     "https://images.unsplash.com/photo-1457369804613-52c61a468e7d?w=400"]
        },
        "modern": {
            "title": "위대한 개츠비",
            "author": "F. 스콧 피츠제럴드 (1925)",
            "desc": "야망과 성취를 향한 집념의 서사. 목표 지향적인 ENTJ에게 공명하는 작품입니다.",
            "imgs": ["https://images.unsplash.com/photo-1519681393784-d120267933ba?w=1200",
                     "https://images.unsplash.com/photo-1497436072909-60f360e1d4b1?w=800",
                     "https://images.unsplash.com/photo-1470770841072-f978cf4d019e?w=400"]
        },
        "artist": {
            "name": "미켈란젤로",
            "era": "이탈리아 · 1475–1564",
            "desc": "시스티나 성당을 홀로 완성한 거장. 대담한 비전과 강철 같은 의지는 ENTJ 그 자체입니다.",
            "style": "renaissance",
            "imgs": ["https://images.unsplash.com/photo-1564399579883-451a5d44ec08?w=1200",
                     "https://images.unsplash.com/photo-1577083287905-2afdb9b97152?w=800",
                     "https://images.unsplash.com/photo-1578321272176-b7bbc0679853?w=400"]
        }
    },
    "ENTP": {
        "classic": {
            "title": "돈키호테",
            "author": "미겔 데 세르반테스 (1605)",
            "desc": "현실의 경계를 넘어 풍차로 돌진하는 기발한 영혼. ENTP의 발랄한 도전정신과 닮았습니다.",
            "imgs": ["https://images.unsplash.com/photo-1500380804539-4e1e8c1e7118?w=1200",
                     "https://images.unsplash.com/photo-1519682337058-a94d519337bc?w=800",
                     "https://images.unsplash.com/photo-1532012197267-da84d127e765?w=400"]
        },
        "modern": {
            "title": "은하수를 여행하는 히치하이커를 위한 안내서",
            "author": "더글러스 애덤스 (1979)",
            "desc": "우주를 가로지르는 기상천외한 위트. ENTP의 번뜩이는 아이디어와 유머의 결정체입니다.",
            "imgs": ["https://images.unsplash.com/photo-1462331940025-496dfbfc7564?w=1200",
                     "https://images.unsplash.com/photo-1419242902214-272b3f66ee7a?w=800",
                     "https://images.unsplash.com/photo-1444703686981-a3abbc4d4fe3?w=400"]
        },
        "artist": {
            "name": "살바도르 달리",
            "era": "스페인 · 1904–1989",
            "desc": "녹아내리는 시계와 초현실의 향연. 기존의 틀을 깨부수는 달리의 유희는 ENTP의 정신입니다.",
            "style": "surreal",
            "imgs": ["https://images.unsplash.com/photo-1547891654-e66ed7ebb968?w=1200",
                     "https://images.unsplash.com/photo-1578926375605-eaf7559b1458?w=800",
                     "https://images.unsplash.com/photo-1569091791842-7cfb64e04797?w=400"]
        }
    },
    "INFJ": {
        "classic": {
            "title": "데미안",
            "author": "헤르만 헤세 (1919)",
            "desc": "자아의 알을 깨고 나오는 영혼의 여정. INFJ의 내면 탐구와 깊이 맞닿아 있습니다.",
            "imgs": ["https://images.unsplash.com/photo-1518709268805-4e9042af2176?w=1200",
                     "https://images.unsplash.com/photo-1519682337058-a94d519337bc?w=800",
                     "https://images.unsplash.com/photo-1532012197267-da84d127e765?w=400"]
        },
        "modern": {
            "title": "연금술사",
            "author": "파울로 코엘료 (1988)",
            "desc": "자아의 신화를 찾아 떠나는 산티아고의 여정. 의미를 좇는 INFJ의 영혼과 공명합니다.",
            "imgs": ["https://images.unsplash.com/photo-1473773508845-188df298d2d1?w=1200",
                     "https://images.unsplash.com/photo-1502134249126-9f3755a50d78?w=800",
                     "https://images.unsplash.com/photo-1500964757637-c85e8a162699?w=400"]
        },
        "artist": {
            "name": "빈센트 반 고흐",
            "era": "네덜란드 · 1853–1890",
            "desc": "별이 빛나는 밤의 소용돌이. 고독과 열정이 뒤엉킨 고흐의 붓질은 INFJ의 심연입니다.",
            "style": "postimpressionism",
            "imgs": ["https://images.unsplash.com/photo-1541680670548-88e8cd23c0f4?w=1200",
                     "https://images.unsplash.com/photo-1579783902614-a3fb3927b6a5?w=800",
                     "https://images.unsplash.com/photo-1578321272176-b7bbc0679853?w=400"]
        }
    },
    "INFP": {
        "classic": {
            "title": "젊은 베르테르의 슬픔",
            "author": "요한 볼프강 폰 괴테 (1774)",
            "desc": "순수한 사랑과 격정의 편지. INFP의 섬세한 감수성을 그대로 옮긴 듯한 작품입니다.",
            "imgs": ["https://images.unsplash.com/photo-1490750967868-88aa4486c946?w=1200",
                     "https://images.unsplash.com/photo-1519682337058-a94d519337bc?w=800",
                     "https://images.unsplash.com/photo-1502082553048-f009c37129b9?w=400"]
        },
        "modern": {
            "title": "호밀밭의 파수꾼",
            "author": "J.D. 샐린저 (1951)",
            "desc": "위선적인 세상에 균열을 느끼는 홀든. INFP의 순수와 방황을 대변하는 청춘의 고전입니다.",
            "imgs": ["https://images.unsplash.com/photo-1500964757637-c85e8a162699?w=1200",
                     "https://images.unsplash.com/photo-1502082553048-f009c37129b9?w=800",
                     "https://images.unsplash.com/photo-1490750967868-88aa4486c946?w=400"]
        },
        "artist": {
            "name": "클로드 모네",
            "era": "프랑스 · 1840–1926",
            "desc": "수련 연못 위의 빛과 색의 시. 순간의 감각을 포착하는 모네는 INFP의 영혼입니다.",
            "style": "impressionism",
            "imgs": ["https://images.unsplash.com/photo-1578926375605-eaf7559b1458?w=1200",
                     "https://images.unsplash.com/photo-1547891654-e66ed7ebb968?w=800",
                     "https://images.unsplash.com/photo-1569091791842-7cfb64e04797?w=400"]
        }
    },
    "ENFJ": {
        "classic": {
            "title": "레 미제라블",
            "author": "빅토르 위고 (1862)",
            "desc": "사랑과 구원, 인간애의 대서사시. 타인의 삶을 끌어안는 ENFJ의 마음과 일치합니다.",
            "imgs": ["https://images.unsplash.com/photo-1519682337058-a94d519337bc?w=1200",
                     "https://images.unsplash.com/photo-1532012197267-da84d127e765?w=800",
                     "https://images.unsplash.com/photo-1457369804613-52c61a468e7d?w=400"]
        },
        "modern": {
            "title": "모리와 함께한 화요일",
            "author": "미치 앨봄 (1997)",
            "desc": "삶의 의미를 전하는 스승의 마지막 수업. 사람을 변화시키는 ENFJ의 사명감을 비춥니다.",
            "imgs": ["https://images.unsplash.com/photo-1529156069898-49953e39b3ac?w=1200",
                     "https://images.unsplash.com/photo-1543269664-7eef42226a21?w=800",
                     "https://images.unsplash.com/photo-1517486808906-6ca8b3f04846?w=400"]
        },
        "artist": {
            "name": "라파엘로 산치오",
            "era": "이탈리아 · 1483–1520",
            "desc": "조화와 균형의 화신. 따뜻한 인간성을 담은 라파엘로는 ENFJ의 미적 이상입니다.",
            "style": "renaissance",
            "imgs": ["https://images.unsplash.com/photo-1577720580479-7d839d829c73?w=1200",
                     "https://images.unsplash.com/photo-1578321272176-b7bbc0679853?w=800",
                     "https://images.unsplash.com/photo-1554907984-15263bfd63bd?w=400"]
        }
    },
    "ENFP": {
        "classic": {
            "title": "어린 왕자",
            "author": "앙투안 드 생텍쥐페리 (1943)",
            "desc": "별과 별 사이를 여행하며 마음의 진실을 발견하는 이야기. ENFP의 천진한 영혼 그 자체입니다.",
            "imgs": ["https://images.unsplash.com/photo-1419242902214-272b3f66ee7a?w=1200",
                     "https://images.unsplash.com/photo-1444703686981-a3abbc4d4fe3?w=800",
                     "https://images.unsplash.com/photo-1462331940025-496dfbfc7564?w=400"]
        },
        "modern": {
            "title": "미드나잇 라이브러리",
            "author": "매트 헤이그 (2020)",
            "desc": "선택하지 않은 인생들을 탐험하는 도서관. 가능성을 사랑하는 ENFP에게 꼭 맞는 책입니다.",
            "imgs": ["https://images.unsplash.com/photo-1481627834876-b7833e8f5570?w=1200",
                     "https://images.unsplash.com/photo-1495020689067-958852a7765e?w=800",
                     "https://images.unsplash.com/photo-1507842217343-583bb7270b66?w=400"]
        },
        "artist": {
            "name": "앙리 마티스",
            "era": "프랑스 · 1869–1954",
            "desc": "원색의 춤과 자유로운 형태. 색채의 야수 마티스는 ENFP의 환희를 캔버스에 담아냅니다.",
            "style": "fauvism",
            "imgs": ["https://images.unsplash.com/photo-1547891654-e66ed7ebb968?w=1200",
                     "https://images.unsplash.com/photo-1569091791842-7cfb64e04797?w=800",
                     "https://images.unsplash.com/photo-1578926375605-eaf7559b1458?w=400"]
        }
    },
    "ISTJ": {
        "classic": {
            "title": "제인 에어",
            "author": "샬럿 브론테 (1847)",
            "desc": "원칙과 자존을 지키는 강인한 여성의 일대기. ISTJ의 신념과 절제를 보여줍니다.",
            "imgs": ["https://images.unsplash.com/photo-1519682337058-a94d519337bc?w=1200",
                     "https://images.unsplash.com/photo-1532012197267-da84d127e765?w=800",
                     "https://images.unsplash.com/photo-1457369804613-52c61a468e7d?w=400"]
        },
        "modern": {
            "title": "남아 있는 나날",
            "author": "가즈오 이시구로 (1989)",
            "desc": "묵묵히 자신의 자리를 지킨 집사의 회고. ISTJ의 책임감과 절제의 미학이 깃든 작품입니다.",
            "imgs": ["https://images.unsplash.com/photo-1507842217343-583bb7270b66?w=1200",
                     "https://images.unsplash.com/photo-1481627834876-b7833e8f5570?w=800",
                     "https://images.unsplash.com/photo-1495020689067-958852a7765e?w=400"]
        },
        "artist": {
            "name": "요하네스 페르메이르",
            "era": "네덜란드 · 1632–1675",
            "desc": "고요한 일상의 빛을 정교하게 포착한 거장. 세밀함과 차분함은 ISTJ의 미적 가치입니다.",
            "style": "baroque",
            "imgs": ["https://images.unsplash.com/photo-1577720580479-7d839d829c73?w=1200",
                     "https://images.unsplash.com/photo-1578321272176-b7bbc0679853?w=800",
                     "https://images.unsplash.com/photo-1554907984-15263bfd63bd?w=400"]
        }
    },
    "ISFJ": {
        "classic": {
            "title": "작은 아씨들",
            "author": "루이자 메이 올컷 (1868)",
            "desc": "가족을 지키는 따뜻한 자매들의 이야기. ISFJ의 헌신과 사랑이 빛나는 작품입니다.",
            "imgs": ["https://images.unsplash.com/photo-1490750967868-88aa4486c946?w=1200",
                     "https://images.unsplash.com/photo-1519682337058-a94d519337bc?w=800",
                     "https://images.unsplash.com/photo-1502082553048-f009c37129b9?w=400"]
        },
        "modern": {
            "title": "나미야 잡화점의 기적",
            "author": "히가시노 게이고 (2012)",
            "desc": "타인의 고민에 정성으로 답하는 작은 가게. ISFJ의 따뜻한 마음씨를 그대로 옮긴 듯합니다.",
            "imgs": ["https://images.unsplash.com/photo-1529156069898-49953e39b3ac?w=1200",
                     "https://images.unsplash.com/photo-1543269664-7eef42226a21?w=800",
                     "https://images.unsplash.com/photo-1517486808906-6ca8b3f04846?w=400"]
        },
        "artist": {
            "name": "메리 카사트",
            "era": "미국 · 1844–1926",
            "desc": "어머니와 아이의 다정한 순간을 그린 인상주의 화가. ISFJ의 보살핌이 화폭에 살아 숨쉽니다.",
            "style": "impressionism",
            "imgs": ["https://images.unsplash.com/photo-1578926375605-eaf7559b1458?w=1200",
                     "https://images.unsplash.com/photo-1547891654-e66ed7ebb968?w=800",
                     "https://images.unsplash.com/photo-1569091791842-7cfb64e04797?w=400"]
        }
    },
    "ESTJ": {
        "classic": {
            "title": "삼국지연의",
            "author": "나관중 (14세기)",
            "desc": "천하 통일의 야망과 통솔의 서사. 질서를 세우는 ESTJ의 리더십과 통합니다.",
            "imgs": ["https://images.unsplash.com/photo-1519682337058-a94d519337bc?w=1200",
                     "https://images.unsplash.com/photo-1532012197267-da84d127e765?w=800",
                     "https://images.unsplash.com/photo-1457369804613-52c61a468e7d?w=400"]
        },
        "modern": {
            "title": "아틀라스",
            "author": "에인 랜드 (1957)",
            "desc": "능력과 책임의 가치를 옹호한 대작. ESTJ의 실용주의와 결단력을 응원하는 책입니다.",
            "imgs": ["https://images.unsplash.com/photo-1519681393784-d120267933ba?w=1200",
                     "https://images.unsplash.com/photo-1497436072909-60f360e1d4b1?w=800",
                     "https://images.unsplash.com/photo-1470770841072-f978cf4d019e?w=400"]
        },
        "artist": {
            "name": "자크 루이 다비드",
            "era": "프랑스 · 1748–1825",
            "desc": "엄격한 구도와 영웅적 서사의 신고전주의 거장. ESTJ의 질서와 권위를 담아냅니다.",
            "style": "neoclassicism",
            "imgs": ["https://images.unsplash.com/photo-1564399579883-451a5d44ec08?w=1200",
                     "https://images.unsplash.com/photo-1577083287905-2afdb9b97152?w=800",
                     "https://images.unsplash.com/photo-1578321272176-b7bbc0679853?w=400"]
        }
    },
    "ESFJ": {
        "classic": {
            "title": "오만과 편견",
            "author": "제인 오스틴 (1813)",
            "desc": "사람들의 관계와 사교계의 미묘함을 섬세히 그린 명작. ESFJ의 사회적 감각이 빛납니다.",
            "imgs": ["https://images.unsplash.com/photo-1490750967868-88aa4486c946?w=1200",
                     "https://images.unsplash.com/photo-1519682337058-a94d519337bc?w=800",
                     "https://images.unsplash.com/photo-1502082553048-f009c37129b9?w=400"]
        },
        "modern": {
            "title": "안녕, 소중한 사람",
            "author": "오가와 이토 (2008)",
            "desc": "음식과 관계로 사람을 위로하는 따스한 이야기. ESFJ의 다정함이 가득합니다.",
            "imgs": ["https://images.unsplash.com/photo-1529156069898-49953e39b3ac?w=1200",
                     "https://images.unsplash.com/photo-1543269664-7eef42226a21?w=800",
                     "https://images.unsplash.com/photo-1517486808906-6ca8b3f04846?w=400"]
        },
        "artist": {
            "name": "피에르 오귀스트 르누아르",
            "era": "프랑스 · 1841–1919",
            "desc": "햇살 아래 사람들의 행복한 순간을 그린 화가. ESFJ의 따뜻한 시선과 일치합니다.",
            "style": "impressionism",
            "imgs": ["https://images.unsplash.com/photo-1578926375605-eaf7559b1458?w=1200",
                     "https://images.unsplash.com/photo-1547891654-e66ed7ebb968?w=800",
                     "https://images.unsplash.com/photo-1569091791842-7cfb64e04797?w=400"]
        }
    },
    "ISTP": {
        "classic": {
            "title": "모비딕",
            "author": "허먼 멜빌 (1851)",
            "desc": "거대한 흰 고래를 쫓는 침묵의 모험. ISTP의 실용적 모험심과 통하는 대서사시입니다.",
            "imgs": ["https://images.unsplash.com/photo-1500964757637-c85e8a162699?w=1200",
                     "https://images.unsplash.com/photo-1502134249126-9f3755a50d78?w=800",
                     "https://images.unsplash.com/photo-1473773508845-188df298d2d1?w=400"]
        },
        "modern": {
            "title": "노인과 바다",
            "author": "어니스트 헤밍웨이 (1952)",
            "desc": "묵묵히 자신과 싸우는 어부의 사투. 군더더기 없는 ISTP의 행동주의와 닮았습니다.",
            "imgs": ["https://images.unsplash.com/photo-1507842217343-583bb7270b66?w=1200",
                     "https://images.unsplash.com/photo-1481627834876-b7833e8f5570?w=800",
                     "https://images.unsplash.com/photo-1495020689067-958852a7765e?w=400"]
        },
        "artist": {
            "name": "에드워드 호퍼",
            "era": "미국 · 1882–1967",
            "desc": "고요한 도시의 풍경과 침묵의 인물들. 관조적이고 절제된 호퍼는 ISTP의 정서입니다.",
            "style": "realism",
            "imgs": ["https://images.unsplash.com/photo-1518709268805-4e9042af2176?w=1200",
                     "https://images.unsplash.com/photo-1547891654-e66ed7ebb968?w=800",
                     "https://images.unsplash.com/photo-1578926375605-eaf7559b1458?w=400"]
        }
    },
    "ISFP": {
        "classic": {
            "title": "폭풍의 언덕",
            "author": "에밀리 브론테 (1847)",
            "desc": "황야의 거친 바람 같은 격정의 사랑. ISFP의 깊고 강렬한 내면 정서와 만납니다.",
            "imgs": ["https://images.unsplash.com/photo-1500964757637-c85e8a162699?w=1200",
                     "https://images.unsplash.com/photo-1502134249126-9f3755a50d78?w=800",
                     "https://images.unsplash.com/photo-1473773508845-188df298d2d1?w=400"]
        },
        "modern": {
            "title": "노르웨이의 숲",
            "author": "무라카미 하루키 (1987)",
            "desc": "잔잔한 음악처럼 흐르는 청춘의 상실과 사랑. ISFP의 섬세한 감성과 공명합니다.",
            "imgs": ["https://images.unsplash.com/photo-1502082553048-f009c37129b9?w=1200",
                     "https://images.unsplash.com/photo-1490750967868-88aa4486c946?w=800",
                     "https://images.unsplash.com/photo-1500964757637-c85e8a162699?w=400"]
        },
        "artist": {
            "name": "폴 세잔",
            "era": "프랑스 · 1839–1906",
            "desc": "자연의 본질을 색과 형태로 재구성한 화가. ISFP의 조용한 깊이를 닮았습니다.",
            "style": "postimpressionism",
            "imgs": ["https://images.unsplash.com/photo-1541680670548-88e8cd23c0f4?w=1200",
                     "https://images.unsplash.com/photo-1579783902614-a3fb3927b6a5?w=800",
                     "https://images.unsplash.com/photo-1578321272176-b7bbc0679853?w=400"]
        }
    },
    "ESTP": {
        "classic": {
            "title": "삼총사",
            "author": "알렉상드르 뒤마 (1844)",
            "desc": "검과 우정과 모험의 향연. 즉각 행동하는 ESTP의 에너지를 그대로 담은 명작입니다.",
            "imgs": ["https://images.unsplash.com/photo-1519682337058-a94d519337bc?w=1200",
                     "https://images.unsplash.com/photo-1532012197267-da84d127e765?w=800",
                     "https://images.unsplash.com/photo-1457369804613-52c61a468e7d?w=400"]
        },
        "modern": {
            "title": "파이트 클럽",
            "author": "척 팔라닉 (1996)",
            "desc": "규칙을 깨고 본능으로 돌진하는 강렬한 서사. ESTP의 즉흥과 스릴 추구를 자극합니다.",
            "imgs": ["https://images.unsplash.com/photo-1519681393784-d120267933ba?w=1200",
                     "https://images.unsplash.com/photo-1497436072909-60f360e1d4b1?w=800",
                     "https://images.unsplash.com/photo-1470770841072-f978cf4d019e?w=400"]
        },
        "artist": {
            "name": "잭슨 폴록",
            "era": "미국 · 1912–1956",
            "desc": "캔버스 위를 춤추는 격렬한 액션 페인팅. ESTP의 즉흥적 에너지가 폭발합니다.",
            "style": "abstract",
            "imgs": ["https://images.unsplash.com/photo-1547891654-e66ed7ebb968?w=1200",
                     "https://images.unsplash.com/photo-1578926375605-eaf7559b1458?w=800",
                     "https://images.unsplash.com/photo-1569091791842-7cfb64e04797?w=400"]
        }
    },
    "ESFP": {
        "classic": {
            "title": "춘향전",
            "author": "작자미상 (조선후기)",
            "desc": "사랑과 흥이 넘치는 한국의 대표 고전. ESFP의 발랄함과 진솔한 감정이 살아있습니다.",
            "imgs": ["https://images.unsplash.com/photo-1490750967868-88aa4486c946?w=1200",
                     "https://images.unsplash.com/photo-1519682337058-a94d519337bc?w=800",
                     "https://images.unsplash.com/photo-1502082553048-f009c37129b9?w=400"]
        },
        "modern": {
            "title": "먹고 기도하고 사랑하라",
            "author": "엘리자베스 길버트 (2006)",
            "desc": "세계를 누비며 인생의 즐거움을 만끽하는 여정. ESFP의 자유로움 그 자체입니다.",
            "imgs": ["https://images.unsplash.com/photo-1488646953014-85cb44e25828?w=1200",
                     "https://images.unsplash.com/photo-1530789253388-582c481c54b0?w=800",
                     "https://images.unsplash.com/photo-1469854523086-cc02fe5d8800?w=400"]
        },
        "artist": {
            "name": "키스 해링",
            "era": "미국 · 1958–1990",
            "desc": "거리에서 피어난 발랄한 선과 원색의 향연. ESFP의 즐거움이 춤추는 그림입니다.",
            "style": "popart",
            "imgs": ["https://images.unsplash.com/photo-1547891654-e66ed7ebb968?w=1200",
                     "https://images.unsplash.com/photo-1569091791842-7cfb64e04797?w=800",
                     "https://images.unsplash.com/photo-1578926375605-eaf7559b1458?w=400"]
        }
    },
}

# ─────────────────────────────────────────────
# 페이지별 배경색 (같은 채도, 다른 색조)
# ─────────────────────────────────────────────
page_bg = {
    0: "#2C2C3E",           # MBTI 선택: 차분한 보라회색
    1: "#3D2E1F",           # 고전: 고풍스러운 다크브라운
    2: "#1F3D3D",           # 현대: 모던한 다크틸
    3: "#3D1F2E",           # 예술가: 예술적인 다크와인
}

# ─────────────────────────────────────────────
# 페이지별 스타일 (고전: 고풍, 현대: 캐주얼, 예술가: 화풍별)
# ─────────────────────────────────────────────
def get_style(page, art_style=None):
    base = f"""
    <style>
    .stApp {{
        background: linear-gradient(135deg, {page_bg[page]} 0%, {page_bg[page]}dd 100%);
    }}
    </style>
    """
    if page == 0:
        return base + """
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@600&family=Noto+Sans+KR:wght@300;500&display=swap');
        h1, h2, h3 { font-family: 'Playfair Display', serif !important; color: #E8DCC4 !important; text-align: center; }
        .stApp p, .stApp label, .stApp div { color: #E8DCC4 !important; font-family: 'Noto Sans KR', sans-serif; }
        </style>
        """
    elif page == 1:  # 고전 - 고풍스럽게
        return base + """
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@500;700&family=Nanum+Myeongjo:wght@400;700&display=swap');
        h1, h2, h3 { font-family: 'Cormorant Garamond', 'Nanum Myeongjo', serif !important; color: #E8C9A0 !important; }
        .title-deco { text-align: center; font-family: 'Cormorant Garamond', serif; font-size: 3rem; color: #D4AF37; letter-spacing: 4px; font-style: italic; }
        .content-box { background: rgba(232, 201, 160, 0.08); border: 1px solid #8B6F47; border-radius: 4px; padding: 2rem; font-family: 'Nanum Myeongjo', serif; color: #E8DCC4; line-height: 2; }
        .book-title { font-family: 'Cormorant Garamond', serif; font-size: 2.4rem; color: #D4AF37; text-align: center; font-weight: 700; }
        .book-author { text-align: center; color: #B89968; font-style: italic; font-family: 'Cormorant Garamond', serif; }
        .ornament { text-align: center; color: #D4AF37; font-size: 1.5rem; margin: 1rem 0; }
        </style>
        """
    elif page == 2:  # 현대 - 캐주얼
        return base + """
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;600;800&family=Nanum+Gothic:wght@400;700&display=swap');
        h1, h2, h3 { font-family: 'Poppins', sans-serif !important; color: #7FD4C9 !important; font-weight: 800 !important; }
        .modern-title { font-family: 'Poppins', sans-serif; font-size: 2.8rem; font-weight: 800; color: #7FD4C9; letter-spacing: -1px; }
        .modern-box { background: rgba(127, 212, 201, 0.1); border-left: 5px solid #7FD4C9; border-radius: 12px; padding: 1.5rem; font-family: 'Nanum Gothic', sans-serif; color: #E0F5F0; line-height: 1.7; }
        .book-title-modern { font-family: 'Poppins', sans-serif; font-size: 2.2rem; font-weight: 800; color: #7FD4C9; }
        .book-author-modern { color: #A8D8D0; font-family: 'Poppins', sans-serif; font-weight: 400; }
        .tag { display: inline-block; background: #7FD4C9; color: #1F3D3D; padding: 4px 12px; border-radius: 20px; font-size: 0.85rem; font-weight: 600; margin: 4px; font-family: 'Poppins', sans-serif; }
        </style>
        """
    elif page == 3:  # 예술가 - 화풍별
        styles = {
            "renaissance": "font-family: 'Cinzel', serif; color: #E8C9A0;",
            "impressionism": "font-family: 'Dancing Script', cursive; color: #F5D5C5;",
            "postimpressionism": "font-family: 'Caveat', cursive; color: #FFD4B8;",
            "surreal": "font-family: 'Abril Fatface', serif; color: #D8A8E0;",
            "popart": "font-family: 'Bungee', sans-serif; color: #FFB8D4;",
            "abstract": "font-family: 'Anton', sans-serif; color: #F5C2C2;",
            "geometric": "font-family: 'Orbitron', sans-serif; color: #C2D8F5;",
            "neoclassicism": "font-family: 'Cinzel', serif; color: #E8DCC4;",
            "fauvism": "font-family: 'Pacifico', cursive; color: #FFB8B8;",
            "realism": "font-family: 'Lora', serif; color: #D4D4C2;",
            "baroque": "font-family: 'Cormorant Garamond', serif; color: #E8C9A0;",
        }
        font_style = styles.get(art_style, "font-family: 'Playfair Display', serif; color: #E8C9A0;")
        return base + f"""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Cinzel:wght@600&family=Dancing+Script:wght@600;700&family=Caveat:wght@500;700&family=Abril+Fatface&family=Bungee&family=Anton&family=Orbitron:wght@700&family=Pacifico&family=Lora:wght@500&family=Cormorant+Garamond:wght@600&family=Playfair+Display:wght@600&family=Noto+Sans+KR&display=swap');
        .artist-name {{ {font_style} font-size: 3rem; text-align: center; font-weight: 700; }}
        .artist-era {{ text-align: center; color: #C8B8D8; font-style: italic; margin-bottom: 1rem; }}
        .art-box {{ background: rgba(232, 201, 160, 0.08); border: 1px solid #8B6F8B; border-radius: 8px; padding: 2rem; color: #F0E0E8; line-height: 1.9; font-family: 'Noto Sans KR', sans-serif; }}
        h1, h2, h3 {{ color: #E8C9D8 !important; text-align: center; }}
        </style>
        """
    return base

# ─────────────────────────────────────────────
# 0페이지: MBTI 선택
# ─────────────────────────────────────────────
def page_select():
    st.markdown(get_style(0), unsafe_allow_html=True)
    
    st.markdown("<h1 style='font-size:2.8rem; margin-top:1rem;'>🎨 MBTI 문화예술 큐레이션</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align:center; color:#B8A8C8; font-style:italic;'>당신의 영혼에 어울리는 책과 예술을 만나보세요</p>", unsafe_allow_html=True)
    st.markdown("---")
    
    st.markdown("<h3>✨ 당신의 MBTI를 한 글자씩 선택하세요</h3><br>", unsafe_allow_html=True)
    
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        e_i = st.radio("**1️⃣ 에너지**", ["E (외향)", "I (내향)"], key="ei")
    with col2:
        s_n = st.radio("**2️⃣ 인식**", ["S (감각)", "N (직관)"], key="sn")
    with col3:
        t_f = st.radio("**3️⃣ 판단**", ["T (사고)", "F (감정)"], key="tf")
    with col4:
        j_p = st.radio("**4️⃣ 생활**", ["J (계획)", "P (탐색)"], key="jp")
    
    mbti = e_i[0] + s_n[0] + t_f[0] + j_p[0]
    ratio = mbti_ratio.get(mbti, 0)
    
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown(
        f"""<div style='text-align:center; background:rgba(232,220,196,0.1); padding:1.5rem; border-radius:12px; border:1px solid #B8A8C8;'>
        <div style='font-size:1rem; color:#C8B8D8;'>당신의 MBTI는</div>
        <div style='font-size:3.5rem; font-weight:700; color:#E8DCC4; letter-spacing:6px; margin:0.5rem 0;'>{mbti}</div>
        <div style='font-size:1.1rem; color:#D4C4B0;'>📊 전 세계 인구의 약 <b style='color:#FFD700;'>{ratio}%</b></div>
        </div>""",
        unsafe_allow_html=True
    )
    
    st.markdown("<br>", unsafe_allow_html=True)
    col_a, col_b, col_c = st.columns([1, 2, 1])
    with col_b:
        if st.button("📜 큐레이션 시작하기", use_container_width=True, type="primary"):
            st.session_state.mbti = mbti
            st.session_state.page = 1
            st.rerun()

# ─────────────────────────────────────────────
# 1페이지: 고전소설 (고풍스럽게)
# ─────────────────────────────────────────────
def page_classic():
    st.markdown(get_style(1), unsafe_allow_html=True)
    
    mbti = st.session_state.mbti
    data = recommendations[mbti]["classic"]
    
    st.markdown(f"<div class='title-deco'>～ Classic Literature ～</div>", unsafe_allow_html=True)
    st.markdown(f"<div class='ornament'>❦  ❦  ❦</div>", unsafe_allow_html=True)
    st.markdown(f"<p style='text-align:center; color:#B89968; font-style:italic;'>{mbti} 유형을 위한 고전의 향기</p>", unsafe_allow_html=True)
    
    # 이미지 대중소
    st.image(data["imgs"][0], use_container_width=True)
    col1, col2 = st.columns([2, 1])
    with col1:
        st.image(data["imgs"][1], use_container_width=True)
    with col2:
        st.image(data["imgs"][2], use_container_width=True)
    
    st.markdown(f"<div class='book-title'>『 {data['title']} 』</div>", unsafe_allow_html=True)
    st.markdown(f"<div class='book-author'>— {data['author']} —</div>", unsafe_allow_html=True)
    st.markdown(f"<div class='ornament'>✦</div>", unsafe_allow_html=True)
    st.markdown(f"<div class='content-box'>{data['desc']}</div>", unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    col_a, col_b, col_c = st.columns(3)
    with col_a:
        if st.button("← 처음으로", use_container_width=True):
            st.session_state.page = 0
            st.rerun()
    with col_c:
        if st.button("현대소설 →", use_container_width=True, type="primary"):
            st.session_state.page = 2
            st.rerun()

# ─────────────────────────────────────────────
# 2페이지: 현대소설 (캐주얼)
# ─────────────────────────────────────────────
def page_modern():
    st.markdown(get_style(2), unsafe_allow_html=True)
    
    mbti = st.session_state.mbti
    data = recommendations[mbti]["modern"]
    
    st.markdown(f"<div class='modern-title'>📚 Modern Novel</div>", unsafe_allow_html=True)
    st.markdown(f"<p style='color:#A8D8D0;'><span class='tag'>#{mbti}</span><span class='tag'>#오늘의책</span><span class='tag'>#감성충전</span></p>", unsafe_allow_html=True)
    
    # 이미지 대중소
    st.image(data["imgs"][0], use_container_width=True)
    col1, col2 = st.columns([2, 1])
    with col1:
        st.image(data["imgs"][1], use_container_width=True)
    with col2:
        st.image(data["imgs"][2], use_container_width=True)
    
    st.markdown(f"<div class='book-title-modern'>{data['title']}</div>", unsafe_allow_html=True)
    st.markdown(f"<div class='book-author-modern'>✍️ {data['author']}</div>", unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown(f"<div class='modern-box'>💬 {data['desc']}</div>", unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
