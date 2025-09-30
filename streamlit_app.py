
import streamlit as st
import sympy as sp
import matplotlib.pyplot as plt
import numpy as np

st.title('수학 노트: 두 정수를 근으로 하는 이차방정식 생성기')

st.markdown('두 정수 a, b를 입력하면, 두 수를 근으로 하는 이차방정식 $x^2 - (a+b)x + ab = 0$ 을 만들어줍니다. 그리고 해당 함수의 그래프도 그려줍니다.')

a = st.number_input('첫 번째 근 a를 입력하세요', value=1, step=1, format="%d")
b = st.number_input('두 번째 근 b를 입력하세요', value=-2, step=1, format="%d")

if st.button('이차방정식 생성'):
	x = sp.Symbol('x')
	# 입력값을 정수로 변환
	a_int = int(a)
	b_int = int(b)
	quad_eq = (x - a_int)*(x - b_int)
	expanded = sp.expand(quad_eq)
	latex_quad = sp.latex(sp.Eq(expanded, 0))
	st.markdown('**이차방정식:**')
	st.latex(latex_quad)

	# 그래프 그리기
	f = sp.lambdify(x, expanded, modules=['numpy'])
	x_vals = np.linspace(a_int-10, b_int+10, 400)
	y_vals = f(x_vals)
	fig, ax = plt.subplots()
	ax.plot(x_vals, y_vals, label=sp.latex(expanded))
	ax.axhline(0, color='gray', linewidth=0.8)
	ax.axvline(a_int, color='red', linestyle='--', label=f'x={a_int}')
	ax.axvline(b_int, color='blue', linestyle='--', label=f'x={b_int}')
	ax.set_xlabel('x')
	ax.set_ylabel('y')
	ax.set_title('이차방정식의 그래프')
	ax.legend()
	st.pyplot(fig)
