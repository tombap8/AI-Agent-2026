import streamlit as st
from datetime import datetime

st.set_page_config(page_title="Coffee Shop", page_icon="☕", layout="centered")

st.title("Coffee Shop")
st.write("간단한 주문 앱입니다. 아래에서 선택하세요.")

name = st.text_input("이름")
menu = st.selectbox("메뉴 선택", ["Americano", "Latte", "Cappuccino", "Mocha"])
size = st.radio("사이즈", ["Small", "Medium", "Large"])
qty = st.number_input("수량", min_value=1, value=1, step=1)

if st.button("주문하기"):
	now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
	st.success(f"{name}님, 주문이 접수되었습니다.")
	st.write("주문 내역:")
	st.write(f"- 메뉴: {menu}")
	st.write(f"- 사이즈: {size}")
	st.write(f"- 수량: {qty}")
	st.write(f"- 시간: {now}")
	st.balloons()

