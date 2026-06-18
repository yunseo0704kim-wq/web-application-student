import streamlit as st


def main():
    st.set_page_config(page_title="합동과 선대칭 학습", page_icon="🪄")
    st.title("📐 합동과 선대칭의 비밀을 풀자!")
    st.markdown("### 직접 돌리고 접어보며 완벽한 도형의 규칙을 찾아봐요!")

    st.markdown(
        """
        **오늘의 학습 목표:**

        - ✓ 모양과 크기가 같아서 완전히 겹치는 도형(합동)을 구별할 수 있다.
        - ✓ 한 직선을 따라 접었을 때 완전히 겹치는 도형(선대칭도형)의 성질을 이해한다.
        """
    )

    st.markdown(
        """
        <div style='display:flex; align-items:center; justify-content:center; gap:16px;'>
            <div style='text-align:center;'>
                <div style='font-size:5rem;'>🧙‍♀️✨</div>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.write("---")
    button_col1, button_col2 = st.columns(2)
    with button_col1:
        st.markdown(
            "<a href='/1_도형의_합동' style='text-decoration:none;'>"
            "<div style='background:#0d6efd; color:#ffffff; padding:16px; border-radius:12px; text-align:center; font-weight:600;'>"
            "[1단계] 완벽한 쌍둥이, 합동 투어 ➔"
            "</div></a>",
            unsafe_allow_html=True,
        )
    with button_col2:
        if st.button("[2단계] 반짝반짝 거울 마법, 선대칭 탐험 ➔"):
            st.session_state.page = "symmetry"

    if "page" not in st.session_state:
        st.session_state.page = None

    if st.session_state.page == "congruence":
        st.header("🔹 1단계: 완벽한 쌍둥이, 합동 투어")
        st.write("두 도형이 크기와 모양까지 같아서 서로 딱 맞는지 확인해보는 시간이에요.")
        st.markdown("- 서로 겹쳤을 때 완전히 일치하면 합동이에요.")
        st.markdown("- SSS, SAS, ASA처럼 간단한 판정 기준으로 확인해봐요.")
    elif st.session_state.page == "symmetry":
        st.header("🔸 2단계: 반짝반짝 거울 마법, 선대칭 탐험")
        st.write("도형을 거울에 비추면 어떻게 보일지 상상해보세요.")
        st.markdown("- 대칭선 기준으로 좌우가 완벽히 맞는지 확인해요.")
        st.markdown("- 반사대칭과 회전대칭을 모두 탐험해봐요.")
    else:
        st.write("버튼을 눌러 원하는 마법 탐험을 시작해보세요!")


if __name__ == "__main__":
    main()
