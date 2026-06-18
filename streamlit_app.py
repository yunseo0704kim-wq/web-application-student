import streamlit as st


def main():
    st.set_page_config(page_title="합동과 대칭 학습", page_icon="🎈")
    st.title("🎈 합동과 대칭 학습")

    st.sidebar.title("메뉴")
    page = st.sidebar.radio("페이지 선택", ("소개", "합동", "대칭", "연습문제", "자료"))

    if page == "소개":
        st.header("학습 안내")
        st.write("간단한 합동과 대칭 학습 페이지입니다. 왼쪽 사이드바에서 섹션을 선택하세요.")

    elif page == "합동":
        st.header("합동 (Congruence)")
        st.write("두 도형이 합동이라는 의미와 판정 기준을 확인합니다.")

        st.subheader("인터랙티브 예시 (플레이스홀더)")
        col1, col2 = st.columns(2)
        with col1:
            angle = st.slider("각도 A", 0, 180, 60)
            side = st.slider("변 a 길이", 10, 300, 100)
            st.write(f"선택한 값 — 각도: {angle}°, 변 길이: {side}")
        with col2:
            st.write("여기에 합동 도형을 시각화하는 캔버스를 추가하세요.")
            if st.button("예시 그리기"):
                st.info("(시각화 로직을 여기에 연결하세요)")

        with st.expander("합동 판정 기준 (예: SSS, SAS, ASA)"):
            st.write("- SSS: 세 변이 각각 대응하여 같다\n- SAS: 두 변과 끼인 각이 같다\n- ASA: 두 각과 그 사이의 변이 같다")

    elif page == "대칭":
        st.header("대칭 (Symmetry)")
        st.write("대칭선, 회전대칭 등 기본 개념을 실습해봅니다.")

        symmetry_type = st.selectbox("대칭 종류 선택", ("반사대칭", "회전대칭"))
        if symmetry_type == "반사대칭":
            line_angle = st.slider("반사선 각도", 0, 180, 90)
            st.write(f"반사선 각도: {line_angle}°")
            if st.button("반사 시각화"):
                st.info("(반사 시각화 로직을 여기에 연결하세요)")
        else:
            rot_angle = st.slider("회전 각도", 0, 360, 180)
            st.write(f"회전 각도: {rot_angle}°")
            if st.button("회전 시각화"):
                st.info("(회전 시각화 로직을 여기에 연결하세요)")

    elif page == "연습문제":
        st.header("연습문제")
        st.write("개념을 확인하는 간단한 문제들입니다.")
        q = st.radio("문제 선택", ("문제 1: 합동 판별", "문제 2: 대칭 판별"))
        if q:
            st.write("문제 설명과 풀이 입력란을 여기에 추가하세요.")

    else:
        st.header("자료")
        st.write("참고자료와 외부 링크를 정리합니다.")
        st.markdown("- [Streamlit Docs](https://docs.streamlit.io/)\n- 추가 학습 자료를 여기에 연결하세요.")


if __name__ == "__main__":
    main()
