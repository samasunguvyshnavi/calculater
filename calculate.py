import streamlit as st

st.title("🧮 Simple Calculator")

# Input numbers
num1 = st.number_input("Enter first number", format="%.2f")
num2 = st.number_input("Enter second number", format="%.2f")

# Choose operation
operation = st.selectbox("Select operation", ("Add", "Subtract", "Multiply", "Divide"))

# Calculate result
if st.button("Calculate"):
    if operation == "Add":
        result = num1 + num2
        st.success(f"Result: {num1} + {num2} = {result}")
    elif operation == "Subtract":
        result = num1 - num2
        st.success(f"Result: {num1} - {num2} = {result}")
    elif operation == "Multiply":
        result = num1 * num2
        st.success(f"Result: {num1} × {num2} = {result}")
    elif operation == "Divide":
        if num2 != 0:
            result = num1 / num2
            st.success(f"Result: {num1} ÷ {num2} = {result}")
        else:
            st.error("Division by zero is not allowed.")
import streamlit as st
import math

st.set_page_config(page_title="🧮 Enhanced Calculator", layout="centered")
st.title("🧮 Simple & Smart Calculator")

# Input numbers
num1 = st.number_input("Enter first number", format="%.2f", key="num1")
num2 = st.number_input("Enter second number", format="%.2f", key="num2")

# Operation selector
operation = st.selectbox(
    "Select operation",
    ("Add", "Subtract", "Multiply", "Divide", "Power", "Modulus")
)

# Rounding option
round_result = st.checkbox("Round result")

# Calculate
if st.button("Calculate"):
    try:
        if operation == "Add":
            result = num1 + num2
            symbol = "+"
        elif operation == "Subtract":
            result = num1 - num2
            symbol = "-"
        elif operation == "Multiply":
            result = num1 * num2
            symbol = "×"
        elif operation == "Divide":
            if num2 != 0:
                result = num1 / num2
                symbol = "÷"
            else:
                st.error("Division by zero is not allowed.")
                result = None
        elif operation == "Power":
            result = num1 ** num2
            symbol = "^"
        elif operation == "Modulus":
            result = num1 % num2
            symbol = "%"
        
        if result is not None:
            if round_result:
                result = round(result, 2)
            st.success(f"Result: {num1} {symbol} {num2} = {result}")
            st.session_state['last_result'] = f"{num1} {symbol} {num2} = {result}"

    except Exception as e:
        st.error(f"Error: {str(e)}")

# Show last result (if exists)
if 'last_result' in st.session_state:
    st.info(f"🕓 Last calculation: {st.session_state['last_result']}")

# Clear result
if st.button("Clear History"):
    st.session_state.pop('last_result', None)
    st.success("History cleared!")

# Toggle Advanced
st.write("---")
if st.checkbox("🔬 Show Advanced Math Functions"):
    adv_num = st.number_input("Enter a number for advanced operations", key="adv_num")
    
    col1, col2 = st.columns(2)
    with col1:
        st.write("√ Square Root:")
        if adv_num >= 0:
            st.code(f"{adv_num} → √ = {round(math.sqrt(adv_num), 4)}")
        else:
            st.warning("Square root of negative number is undefined.")
    
    with col2:
        st.write("Log10:")
        if adv_num > 0:
            st.code(f"{adv_num} → log10 = {round(math.log10(adv_num), 4)}")
        else:
            st.warning("Logarithm of non-positive number is undefined.")
