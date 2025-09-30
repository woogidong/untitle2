st.title("🎈 My new app")
st.write(
import streamlit as st
import sympy as sp
import matplotlib.pyplot as plt
import numpy as np
from sympy.parsing.sympy_parser import parse_expr
from sympy import Symbol

st.title('수학 노트: 수식 LaTeX 변환 및 그래프 그리기')

# 수식 입력
equation = st.text_input('수식을 입력하세요 (예: x**2 + 2*x + 1):', value='x**2')

if equation:
    # LaTeX 변환
    try:
        expr = parse_expr(equation, evaluate=True)
        latex_expr = sp.latex(expr)
        st.markdown('**LaTeX 표현식:**')
        st.latex(latex_expr)
    except Exception as e:
        st.error(f"수식 파싱 오류: {e}")

    # 그래프 그리기
    try:
        x = Symbol('x')
        f = sp.lambdify(x, expr, modules=['numpy'])
        x_vals = np.linspace(-10, 10, 400)
        y_vals = f(x_vals)
        fig, ax = plt.subplots()
        ax.plot(x_vals, y_vals)
        ax.set_xlabel('x')
        ax.set_ylabel('y')
        ax.set_title('그래프')
        st.markdown('**그래프:**')
        st.pyplot(fig)
    except Exception as e:
        st.error(f"그래프 그리기 오류: {e}")

# 두 수를 근으로 하는 이차방정식 생성
st.markdown('---')
st.header('두 수를 근으로 하는 이차방정식 만들기')
a = st.number_input('첫 번째 근을 입력하세요', value=1.0, format="%g")
b = st.number_input('두 번째 근을 입력하세요', value=-2.0, format="%g")

if st.button('이차방정식 생성'):
    x = sp.Symbol('x')
    # (x - a)(x - b) = 0 -> x^2 - (a+b)x + ab = 0
    quad_eq = (x - a)*(x - b)
    expanded = sp.expand(quad_eq)
    latex_quad = sp.latex(sp.Eq(expanded, 0))
    st.markdown('**이차방정식:**')
    st.latex(latex_quad)
