import streamlit as st


def main():
    st.set_page_config(page_title="합동과 선대칭 학습", page_icon="🪄")
    st.title("📐 합동과 선대칭의 비밀을 풀자!")
    st.markdown("### 직접 돌리고 접어보며 완벽한 도형의 규칙을 찾아봐요!")

    # 사이드바: 빠른 이동 링크
    st.sidebar.title("학습 메뉴")
    st.sidebar.markdown(
        "<a href='/1_도형의_합동' style='text-decoration:none;'>[1단계] 완벽한 쌍둥이, 합동 투어 ➔</a>",
        unsafe_allow_html=True,
    )
    st.sidebar.markdown(
        "<a href='/2_선대칭도형' style='text-decoration:none;'>[2단계] 반짝반짝 거울 마법, 선대칭 탐험 ➔</a>",
        unsafe_allow_html=True,
    )
    st.sidebar.markdown(
        "<a href='/3_퀴즈' style='text-decoration:none;'>[3단계] 최종 퀴즈 ➔</a>",
        unsafe_allow_html=True,
    )
    st.sidebar.write("여기에서 원하는 페이지로 빠르게 이동할 수 있어요.")
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
    st.write("아래에서 원하는 페이지를 골라서 다음 학습으로 넘어가 보세요.")

    page_cols = st.columns(3)
    page_cols[0].markdown(
        "<a href='/1_도형의_합동' style='text-decoration:none;'>"
        "<div style='background:#0d6efd; color:#ffffff; padding:18px; border-radius:14px; text-align:center; font-weight:700;'>"
        "[1단계] 완벽한 쌍둥이, 합동 투어 ➔"
        "</div></a>",
        unsafe_allow_html=True,
    )
    page_cols[1].markdown(
        "<a href='/2_선대칭도형' style='text-decoration:none;'>"
        "<div style='background:#198754; color:#ffffff; padding:18px; border-radius:14px; text-align:center; font-weight:700;'>"
        "3페이지<br>선대칭도형"
        "</div></a>",
        unsafe_allow_html=True,
    )
    page_cols[2].markdown(
        "<a href='/3_퀴즈' style='text-decoration:none;'>"
        "<div style='background:#dc3545; color:#ffffff; padding:18px; border-radius:14px; text-align:center; font-weight:700;'>"
        "4페이지<br>최종 퀴즈"
        "</div></a>",
        unsafe_allow_html=True,
    )

    st.write("페이지 번호를 선택하여 다음 학습으로 바로 이동할 수 있어요.")


if __name__ == "__main__":
    main()
