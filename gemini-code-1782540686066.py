# -------------------------------------------------------------------------
# [서·논술형 1] 채점 로직 (에러 수정본)
# -------------------------------------------------------------------------
with tabs[0]:
    st.subheader("📋 [서·논술형 1] 표 빈칸 채우기 요약 답안 채점")
    
    if selected_set_key == "set_1":
        ans_1 = st.text_input("(1) 과제의 특성 입력:", placeholder="예: 비교적 쉬운 취미 생활이나 큰 노력을 들일 필요가 없는 과제")
        ans_2 = st.text_input("(2) 효율적인 환경 및 방법 입력:", placeholder="예: 충분히 연습하며 익숙해질 때까지 차분하게 혼자 집중하는 시간을 가짐")
        ans_3 = st.text_input("(3) 관련된 심리 현상 입력:", placeholder="예: 사회적 억제")
        
        if st.button("표 요약 문항 채점하기"):
            score = 0
            feedback = []
            
            # (1)번 검증
            if any(k in ans_1 for k in db["q1_keywords"]["1"]):
                score += 2
                feedback.append("✔️ (1)번 문항: 만점 (2/2) - 과제의 난이도 특성이 적절히 반영되었습니다.")
            else:
                feedback.append("❌ (1)번 문항: 오답 (0/2) - '쉬움/낮은 난이도'의 특성이 기술되지 않았습니다.")
                
            # (2)번 검증
            if any(k in ans_2 for k in db["q1_keywords"]["2"]):
                score += 2
                feedback.append("✔️ (2)번 문항: 만점 (2/2) - '혼자 집중하는 환경'의 조건이 명확히 제시되었습니다.")
            else:
                feedback.append("❌ (2)번 문항: 오답 (0/2) - '혼자'라는 필수 환경 조건이 누락되었습니다.")
                
            # (3)번 검증
            if "사회적 억제" in ans_3.replace(" ", ""):
                score += 2
                feedback.append("✔️ (3)번 문항: 만점 (2/2) - 학술 고유 명사가 정확합니다.")
            else:
                feedback.append("❌ (3)번 문항: 오답 (0/2) - 정답은 '사회적 억제'입니다.")
                
            st.metric("최종 점수", f"{score} / 6 점")
            for f in feedback: 
                st.write(f)

    elif selected_set_key == "set_2":
        ans_1 = st.text_input("(1) 정전기의 비유 입력:", placeholder="예: 높은 곳에 고여 있는 물")
        ans_2 = st.text_input("(2) 전하의 상태 입력:", placeholder="예: 전하가 이동하지 않고 머물러 있음")
        ans_3 = st.text_input("(3) 정전기의 위험성 여부 입력:", placeholder="예: 위험하지 않음")
        
        if st.button("표 요약 문항 채점하기"):
            score = 0
            feedback = []
            if all(k in ans_1 for k in ["높은", "물"]): 
                score += 2
                feedback.append("✔️ (1)번 통과 (2/2)")
            else: 
                feedback.append("❌ (1)번 오답 (0/2) - '높은 곳'과 '물'의 비유가 필수입니다.")
                
            if any(k in ans_2 for k in db["q1_keywords"]["2"]): 
                score += 2
                feedback.append("✔️ (2)번 통과 (2/2)")
            else: 
                feedback.append("❌ (2)번 오답 (0/2) - 전하가 '이동하지 않고 머무름'의 특성이 필요합니다.")
                
            if any(k in ans_3 for k in db["q1_keywords"]["3"]): 
                score += 2
                feedback.append("✔️ (3)번 통과 (2/2)")
            else: 
                feedback.append("❌ (3)번 오답 (0/2) - '위험하지 않음'의 결론이 필요합니다.")
                
            st.metric("최종 점수", f"{score} / 6 점")
            for f in feedback: 
                st.write(f)

    elif selected_set_key == "set_3":
        ans_1 = st.text_input("(1) 인공지능의 비유 입력:", placeholder="예: 로봇이 실수 없이 완벽하게 피겨 경기를 해내는 것")
        ans_2 = st.text_input("(2) 예술로 보기 어려운 근거 입력:", placeholder="예: 감정이 없고 독자적인 철학이나 이야기가 없음")
        ans_3 = st.text_input("(3) 가치와 의의 입력:", placeholder="예: 기존 미술계에 큰 변화를 주고 예술 범주를 확장함")
        
        if st.button("표 요약 문항 채점하기"):
            score = 0
            feedback = []
            if any(k in ans_1 for k in db["q1_keywords"]["1"]): 
                score += 2
                feedback.append("✔️ (1)번 통과 (2/2)")
            else: 
                feedback.append("❌ (1)번 오답 (0/2) - 로봇의 '실수 없는 완벽함' 비유가 핵심입니다.")
            
            has_emo = "감정" in ans_2
            has_phil = any(k in ans_2 for k in ["철학", "이야기"])
            if has_emo and has_phil: 
                score += 2
                feedback.append("✔️ (2)번 통과 (2/2)")
            elif has_emo or has_phil: 
                score += 1
                feedback.append("🔺 (2)번 부분점수 (1/2) - 감정과 철학 중 한 가지 근거만 서술되었습니다.")
            else: 
                feedback.append("❌ (2)번 오답 (0/2)")
            
            if any(k in ans_3 for k in db["q1_keywords"]["3"]): 
                score += 2
                feedback.append("✔️ (3)번 통과 (2/2)")
            else: 
                feedback.append("❌ (3)번 오답 (0/2) - '미술계 변화' 또는 '범주 확장'의 가치가 포함되어야 합니다.")
                
            st.metric("최종 점수", f"{score} / 6 점")
            for f in feedback: 
                st.write(f)