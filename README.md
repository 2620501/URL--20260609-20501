# 🎈 Blank app template

A simple Streamlit app template for you to modify!

[![Open in Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://blank-app-template.streamlit.app/)

### How to run it on your own machine

1. Install the requirements

   ```
   $ pip install -r requirements.txt
   ```

2. Run the app

   ```
   $ streamlit run streamlit_app.py
   ```
import streamlit as st
import time

# 웹 페이지 제목 설정
st.title("💓 스마트 심박수 모니터링 시스템")
st.write("실시간으로 심박수 데이터를 분석하여 건강 상태를 모니터링합니다.")

# 1. 가상의 심박수 데이터 리스트 정의
# (60 미만: 서맥 / 60~100: 정상 / 100 초과: 빈맥)
heart_rates = [72, 55, 85, 110, 65, 45, 95, 105, 80]

st.subheader("📊 분석할 심박수 데이터")
st.write(f"현재 측정된 데이터: {heart_rates}")

# 모니터링 시작 버튼
if st.button("🔴 모니터링 시작"):
    st.write("---")
    st.subheader("🔄 실시간 상태 분석 중...")
    
    # 결과를 실시간으로 업데이트하기 위한 빈 비주얼 공간 생성
    status_text = st.empty()
    metric_display = st.empty()
    
    # 2. for문을 이용해 심박수 데이터를 순차적으로 훑기
    for idx, bpm in enumerate(heart_rates):
        # 화면 갱신 효과를 위해 1초씩 대기
        time.sleep(1)
        
        # 현재 처리 중인 데이터 표시
        status_text.write(f"**[{idx + 1}번째 측정]** 현재 심박수: **{bpm} BPM**")
        
        # 3. if-elif-else 조건문을 활용한 심박수 진단
        if bpm < 60:
            # 심맥(서맥) 경고 -> 파란색 계열 경고창
            metric_display.error(f"⚠️ 서맥 경고! 심박수가 지나치게 낮습니다. ({bpm} BPM)")
        elif bpm > 100:
            # 빈맥 경고 -> 빨간색 계열 경고창
            metric_display.error(f"🚨 빈맥 경고! 심박수가 지나치게 높습니다. ({bpm} BPM)")
        else:
            # 정상 범위 -> 초과/미만이 아닌 경우 (60 이상 100 이하)
            metric_display.success(f"✅ 정상 상태입니다. ({bpm} BPM)")
            
    st.success("🏁 모든 데이터 분석이 완료되었습니다!")