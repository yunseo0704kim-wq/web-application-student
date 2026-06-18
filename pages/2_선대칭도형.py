import streamlit as st


def render_butterfly_demo(wing_style: str) -> str:
    axis_x = 280
    if wing_style == "둥근 날개":
        left_path = "M 280,160 C 220,90 140,70 120,160 C 140,250 220,230 280,160 Z"
        right_path = "M 280,160 C 340,90 420,70 440,160 C 420,250 340,230 280,160 Z"
    elif wing_style == "뾰족 날개":
        left_path = "M 280,160 L 180,40 L 130,170 L 180,280 Z"
        right_path = "M 280,160 L 380,40 L 430,170 L 380,280 Z"
    else:
        left_path = "M 280,160 C 225,110 170,130 150,160 C 170,190 225,210 280,160 Z"
        right_path = "M 280,160 C 335,110 390,130 410,160 C 390,190 335,210 280,160 Z"

    svg = f"""
    <div style='display:flex; justify-content:center; margin-bottom:24px;'>
      <div style='background:#fff8f0; padding:18px; border-radius:24px; border:2px dashed #ffadad;'>
        <svg width='620' height='340' viewBox='0 0 620 340' xmlns='http://www.w3.org/2000/svg'>
          <rect x='0' y='0' width='620' height='340' fill='#fdf3e7' rx='24'/>
          <line x1='{axis_x}' y1='40' x2='{axis_x}' y2='300' stroke='#e63946' stroke-width='4' stroke-dasharray='8 8'/>
          <text x='{axis_x + 12}' y='50' font-size='18' fill='#e63946'>대칭축</text>
          <path d='{left_path}' fill='#ffb4a2' stroke='#9b2226' stroke-width='4' opacity='0.95'/>
          <path d='{right_path}' fill='#ffb4a2' stroke='#9b2226' stroke-width='4' opacity='0.95'/>
          <circle cx='{axis_x}' cy='160' r='18' fill='#7f5539'/>
          <circle cx='{axis_x}' cy='160' r='10' fill='#f7f7ff'/>
          <text x='260' y='184' font-size='14' fill='#3d1f00'>나비 몸통</text>
        </svg>
      </div>
    </div>
    """
    return svg


def render_shape_axis(shape: str) -> str:
    if shape == "이등변삼각형":
        return """
        <svg width='300' height='250' viewBox='0 0 300 250' xmlns='http://www.w3.org/2000/svg'>
          <rect x='0' y='0' width='300' height='250' fill='#eef2ff' rx='20'/>
          <polygon points='150,40 90,210 210,210' fill='#a5d8ff' stroke='#1c7ed6' stroke-width='4'/>
          <line x1='150' y1='40' x2='150' y2='210' stroke='#d00000' stroke-width='4' stroke-dasharray='6 6'/>
        </svg>
        """
    if shape == "정삼각형":
        return """
        <svg width='300' height='250' viewBox='0 0 300 250' xmlns='http://www.w3.org/2000/svg'>
          <rect x='0' y='0' width='300' height='250' fill='#effaf6' rx='20'/>
          <polygon points='150,40 70,200 230,200' fill='#8ce99a' stroke='#2f9e44' stroke-width='4'/>
          <line x1='150' y1='40' x2='150' y2='200' stroke='#186743' stroke-width='4' stroke-dasharray='6 6'/>
          <line x1='110' y1='120' x2='190' y2='120' stroke='#186743' stroke-width='4' stroke-dasharray='6 6'/>
          <line x1='72' y1='200' x2='228' y2='200' stroke='#186743' stroke-width='4' stroke-dasharray='6 6'/>
        </svg>
        """
    if shape == "직사각형":
        return """
        <svg width='300' height='250' viewBox='0 0 300 250' xmlns='http://www.w3.org/2000/svg'>
          <rect x='0' y='0' width='300' height='250' fill='#fff3bf' rx='20'/>
          <rect x='70' y='50' width='160' height='140' fill='#ffd670' stroke='#fd7e14' stroke-width='4'/>
          <line x1='150' y1='50' x2='150' y2='190' stroke='#ca6702' stroke-width='4' stroke-dasharray='6 6'/>
          <line x1='70' y1='120' x2='230' y2='120' stroke='#ca6702' stroke-width='4' stroke-dasharray='6 6'/>
        </svg>
        """
    if shape == "정사각형":
        return """
        <svg width='300' height='250' viewBox='0 0 300 250' xmlns='http://www.w3.org/2000/svg'>
          <rect x='0' y='0' width='300' height='250' fill='#f3f0ff' rx='20'/>
          <rect x='70' y='50' width='160' height='160' fill='#b197fc' stroke='#5f3dc4' stroke-width='4'/>
          <line x1='150' y1='50' x2='150' y2='210' stroke='#3b0b87' stroke-width='4' stroke-dasharray='6 6'/>
          <line x1='70' y1='130' x2='230' y2='130' stroke='#3b0b87' stroke-width='4' stroke-dasharray='6 6'/>
          <line x1='70' y1='50' x2='230' y2='210' stroke='#3b0b87' stroke-width='4' stroke-dasharray='6 6'/>
          <line x1='70' y1='210' x2='230' y2='50' stroke='#3b0b87' stroke-width='4' stroke-dasharray='6 6'/>
        </svg>
        """
    if shape == "원":
        return """
        <svg width='300' height='250' viewBox='0 0 300 250' xmlns='http://www.w3.org/2000/svg'>
          <rect x='0' y='0' width='300' height='250' fill='#e7f5ff' rx='20'/>
          <circle cx='150' cy='125' r='70' fill='#74c0fc' stroke='#1c7ed6' stroke-width='4'/>
          <line x1='150' y1='55' x2='150' y2='195' stroke='#1864ab' stroke-width='4' stroke-dasharray='6 6'/>
          <line x1='80' y1='125' x2='220' y2='125' stroke='#1864ab' stroke-width='4' stroke-dasharray='6 6'/>
          <line x1='110' y1='90' x2='190' y2='160' stroke='#1864ab' stroke-width='4' stroke-dasharray='6 6'/>
          <line x1='110' y1='160' x2='190' y2='90' stroke='#1864ab' stroke-width='4' stroke-dasharray='6 6'/>
        </svg>
        """
    return ""


def main():
    st.set_page_config(page_title="선대칭도형", page_icon="🪞")
    st.title("선대칭도형 (데칼코마니 거울 마법)")
    st.subheader("① 개념 쏙쏙: \"반으로 접으면 마법처럼 똑같아!\"")

    st.write(
        "한 직선을 따라 접었을 때, 왼쪽과 오른쪽이 완전히 겹치는 도형을 "
        "**선대칭도형**이라고 해. 이때 접는 선을 **대칭축**이라고 불러!"
    )

    st.markdown("---")
    st.write("### ✨ 반쪽 그리기 마술")
    st.write("왼쪽에 있는 반쪽 나비 날개를 보고, 오른쪽에 내가 그린 모양이 거울처럼 나타나는지 확인해봐요.")

    wing_style = st.radio(
        "오른쪽 빈 공간에 어떤 날개를 그릴래요?",
        ["둥근 날개", "뾰족 날개", "물결 날개"],
        index=0,
        horizontal=True,
    )

    st.markdown(render_butterfly_demo(wing_style), unsafe_allow_html=True)
    st.caption("대칭축(빨간 점선)을 기준으로 오른쪽 날개가 왼쪽 날개와 똑같이 나타나요.")

    st.markdown("---")
    st.subheader("② 탐구 활동: 도형마다 대칭축은 몇 개일까?")
    st.write("아래 도형 버튼을 눌러서, 대칭축이 어디에 있는지 직접 확인해봐요.")

    shapes = [
        {"name": "이등변삼각형", "axes": "1개", "hint": "가운데 세로로만 접을 수 있어요!"},
        {"name": "정삼각형", "axes": "3개", "hint": "세 꼭짓점에서 내린 선이 모두 대칭축이에요."},
        {"name": "직사각형", "axes": "2개", "hint": "가로, 세로 접기만 돼요. 대각선은 안 겹쳐요!"},
        {"name": "정사각형", "axes": "4개", "hint": "가로, 세로, 대각선까지 완벽하게 겹쳐요!"},
        {"name": "원", "axes": "무수히 많음", "hint": "중심을 지나는 선이라면 어디든 접어도 똑같아!"},
    ]

    for shape in shapes:
        key = f"show_{shape['name']}"
        if key not in st.session_state:
            st.session_state[key] = False

        cols = st.columns([2, 1, 1])
        cols[0].markdown(f"**{shape['name']}**")
        cols[1].markdown(f"**{shape['axes']}**")
        if cols[2].button("비밀 힌트", key=f"hint_{shape['name']}"):
            st.session_state[key] = not st.session_state[key]

        if st.session_state[key]:
            st.info(shape["hint"])
            st.markdown(render_shape_axis(shape["name"]), unsafe_allow_html=True)
            st.write("---")

    st.write(
        "도형을 직접 보고 덮어보면, 어떤 선이 대칭축인지 더 쉽고 재미있게 알 수 있어요!"
    )


if __name__ == "__main__":
    main()
