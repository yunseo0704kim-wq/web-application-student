import time

import streamlit as st


def render_triangle_frame(placeholder, frame: int) -> None:
    angle = -30 + frame * 6
    dx = 120 - frame * 24
    dy = -30 + frame * 6

    if frame >= 6:
        angle = 0
        dx = 0
        dy = 0

    svg = f"""
    <div style='display:flex; justify-content:center;'>
      <div style='background:#f8f7ff; padding:16px; border-radius:20px; border:2px dashed #9ab7ea;'>
        <svg width='340' height='260' viewBox='0 0 340 260' xmlns='http://www.w3.org/2000/svg'>
          <polygon points='80,190 40,70 190,150' fill='#8ecae6' stroke='#2a6f97' stroke-width='4' opacity='0.85'/>
          <g transform='translate({dx},{dy}) rotate({angle},100,140)'>
            <polygon points='80,190 40,70 190,150' fill='#ffb703' stroke='#fb8500' stroke-width='4' opacity='0.9'/>
          </g>
          <text x='20' y='30' font-size='18' fill='#073b4c'>삼각형 A</text>
          <text x='210' y='40' font-size='18' fill='#9d0208'>삼각형 B</text>
        </svg>
      </div>
    </div>
    """

    placeholder.markdown(svg, unsafe_allow_html=True)


def animate_triangle(placeholder) -> None:
    for frame in range(7):
        render_triangle_frame(placeholder, frame)
        time.sleep(0.12)


def render_match_frame(placeholder, highlight_vertex: bool, sticker_attached: bool) -> None:
    vertex_color = "#ffd60a" if highlight_vertex else "#ffffff"
    sticker_html = "<text x='260' y='220' font-size='18' fill='#006d77'>📌 짝꿍 변 ㄹㅁ</text>" if sticker_attached else ""
    sticker_box = (
        "<rect x='240' y='200' width='90' height='35' fill='#83c5be' rx='10'/>"
        "<text x='245' y='222' font-size='14' fill='#073b4c'>길이 5cm, 딱 붙었어요!</text>"
    ) if sticker_attached else ""

    svg = f"""
    <div style='display:flex; justify-content:center; gap:24px;'>
      <div style='background:#f8f7ff; padding:16px; border-radius:20px; border:2px dashed #9ab7ea;'>
        <svg width='260' height='260' viewBox='0 0 260 260' xmlns='http://www.w3.org/2000/svg'>
          <polygon points='60,180 40,80 180,160' fill='#8ecae6' stroke='#2a6f97' stroke-width='4' opacity='0.95'/>
          <circle cx='60' cy='80' r='12' fill='{vertex_color}' stroke='#073b4c' stroke-width='3'/>
          <text x='46' y='92' font-size='18' fill='#073b4c'>ㄱ</text>
          <text x='160' y='40' font-size='18' fill='#073b4c'>삼각형 A</text>
        </svg>
      </div>
      <div style='background:#fff0f0; padding:16px; border-radius:20px; border:2px dashed #ee6352;'>
        <svg width='260' height='260' viewBox='0 0 260 260' xmlns='http://www.w3.org/2000/svg'>
          <polygon points='80,180 60,80 200,160' fill='#ffb703' stroke='#fb8500' stroke-width='4' opacity='0.95'/>
          <circle cx='80' cy='80' r='12' fill='{vertex_color}' stroke='#9d0208' stroke-width='3'/>
          <text x='66' y='92' font-size='18' fill='#9d0208'>ㄹ</text>
          {sticker_box}
          {sticker_html}
          <text x='140' y='40' font-size='18' fill='#9d0208'>삼각형 B</text>
        </svg>
      </div>
    </div>
    """

    placeholder.markdown(svg, unsafe_allow_html=True)


def main():
    st.set_page_config(page_title="도형의 합동", page_icon="📐")
    st.title("도형의 합동 (완벽한 쌍둥이 찾기)")
    st.subheader("① 개념 쏙쏙: \"우린 모양도 크기도 똑같아!\"")

    st.write(
        "모양과 크기가 똑같아서, 서로 폭 포개었을 때 완전히 겹치는 두 도형을 "
        "**합동**이라고 해!"
    )

    st.markdown("---")
    st.write("화면에 약간 비틀어져 있는 삼각형 A와 삼각형 B가 있습니다.")
    st.write("[마법 주문 외우기] 버튼을 누르면 마법이 일어나요!")

    if "animate" not in st.session_state:
        st.session_state.animate = False

    if st.button("마법 주문 외우기"):
        st.session_state.animate = True

    animation_placeholder = st.empty()
    if st.session_state.animate:
        animate_triangle(animation_placeholder)
        st.session_state.animate = False
    else:
        render_triangle_frame(animation_placeholder, 0)

    st.markdown("---")
    st.subheader("② 개념 다지기: \"짝꿍을 찾아라! 대응점·대응변·대응각\"")
    st.write("완전히 겹쳐진 두 삼각형이 다시 양옆으로 나란히 분리됩니다.")
    st.write("아래 버튼을 눌러 대응점과 대응변을 찾아보세요.")

    if "vertex_selected" not in st.session_state:
        st.session_state.vertex_selected = False
    if "edge_dragged" not in st.session_state:
        st.session_state.edge_dragged = False

    col1, col2 = st.columns(2)
    with col1:
        if st.button("삼각형 A의 꼭짓점 ㄱ 클릭하기"):
            st.session_state.vertex_selected = True
    with col2:
        if st.button("변 ㄱㄴ을 ㄹㅁ 위로 붙이기"):
            st.session_state.edge_dragged = True

    match_placeholder = st.empty()
    render_match_frame(match_placeholder, st.session_state.vertex_selected, st.session_state.edge_dragged)

    if st.session_state.vertex_selected:
        st.success("삼각형 B의 대응점 ㄹ이 반짝반짝 빛나요! ✨")
    if st.session_state.edge_dragged:
        st.info("변의 길이는 둘 다 5cm로 똑같아! 📏")


if __name__ == "__main__":
    main()
