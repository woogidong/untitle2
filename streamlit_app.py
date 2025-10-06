
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
	ax.set_title(st.latex(f'y=(x - ({a_int}))(x - ({b_int}))'))
	ax.legend()

	st.pyplot(fig)

# --- 자기평가 체크박스 섹션 ---
st.markdown('---')
st.header('스스로 평가하기')

self_eval_items = [
	('개념 이해', '이차방정식과 이차함수 사이의 관계를 이해할 수 있다.', '😃'),
	('문제 해결', '두 수를 근으로 갖는 이차방정식을 이용하여 문제를 해결할 수 있다.', '🧐'),
	('응용력', '실생활에서 이차방정식을 어떻게 활용할 수 있을지 예를 들 수 있다.', '🤔'),
	('자신감', '오늘 배운 것을 자신있게 설명할 수 있다.', '😎'),
	('학습 태도', '수학 공부에 꾸준히 노력하고 있다.', '💪'),
	('질문하기', '모르는 부분이나 궁금한 점이 있어요.', '🗣️'),
	
]

st.markdown('아래 항목에 체크하며 오늘의 학습을 스스로 평가해보세요!')

cols = st.columns(2)
for i, (title, desc, emoji) in enumerate(self_eval_items):
	with cols[i % 2]:
		st.checkbox(f"{emoji} {title}", value=False, help=desc)
