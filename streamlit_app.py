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
