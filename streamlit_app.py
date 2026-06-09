import streamlit as st

st.title("🎈 My new app")
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)
import streamlit as st
import time

# 웹 페이지 제목 및 설명
st.title("💓 스마트 심박수 모니터링 시스템")
st.write("사용자가 입력한 심박수 데이터를 기반으로 실시간 건강 상태를 분석합니다.")

# 1. 의미 있는 하나의 리스트 정의 (기본 데이터)
# streamlit의 session_state를 활용하여 사용자가 추가하는 데이터가 리스트에 계속 유지되도록 합니다.
if "heart_rates" not in st.session_state:
    st.session_state.heart_rates = [72, 55, 85, 110, 65]

# --- 사용자 입력 섹션 ---
st.subheader("📥 새로운 심박수 데이터 입력")

# 숫자를 입력받는 Streamlit 컴포넌트 (사용자 입력)
new_bpm = st.number_input(
    "측정된 심박수를 입력하세요 (BPM):", 
    min_value=30, 
    max_value=200, 
    value=80, 
    step=1
)

# [데이터 추가] 버튼을 누르면 리스트에 입력값이 추가됨
if st.button("➕ 데이터 추가"):
    st.session_state.heart_rates.append(new_bpm)
    st.success(f"리스트에 {new_bpm} BPM이 성공적으로 추가되었습니다!")

# --- 데이터 확인 및 모니터링 섹션 ---
st.write("---")
st.subheader("📊 현재 저장된 심박수 리스트")
st.info(f"현재 분석 대상 데이터: {st.session_state.heart_rates}")

# [모니터링 시작] 버튼을 누르면 분석 작동 (의미 있는 출력 시작)
if st.button("🔴 모니터링 시작"):
    st.subheader("🔄 실시간 상태 분석 중...")
    
    # 출력을 실시간으로 업데이트하기 위한 공간 생성
    status_text = st.empty()
    metric_display = st.empty()
    
    # 2. for 반복문을 사용하여 리스트를 순차적으로 탐색
    for idx, bpm in enumerate(st.session_state.heart_rates):
        # 실시간 시각 효과를 위해 0.5초 대기
        time.sleep(0.5)
        
        # 현재 검사 중인 데이터 출력
        status_text.write(f"**[{idx + 1}번째 측정 데이터]** 현재 심박수: **{bpm} BPM**")
        
        # 3. if 조건문을 사용하여 심박수 상태 판별
        if bpm < 60:
            # 60 미만일 때: 서맥 경고 출력
            metric_display.error(f"⚠️ [서맥 경고] 심박수가 너무 낮습니다! ({bpm} BPM)")
        elif bpm > 100:
            # 100 초과일 때: 빈맥 경고 출력
            metric_display.error(f"🚨 [빈맥 경고] 심박수가 너무 높습니다! ({bpm} BPM)")
        else:
            # 60 이상 100 이하일 때: 정상 출력
            metric_display.success(f"✅ [정상 상태] 안정적인 심박수입니다. ({bpm} BPM)")
            
    st.success("🏁 모든 심박수 데이터의 분석이 완료되었습니다!")