import streamlit as st

# 🎯 Function to convert units
def convert_units(value, from_unit, to_unit):
    convertions = {
    # Length conversions
    "meter-kilometer": 0.001,
    "kilometer-meter": 1000,
    "meter-centimeter": 100,
    "centimeter-meter": 0.01,
    "centimeter-inch": 0.393701,
    "inch-centimeter": 2.54,
    "meter-inch": 39.3701,
    "inch-meter": 0.0254,
    "mile-kilometer": 1.60934,
    "kilometer-mile": 0.621371,

    # Weight conversions
    "gram-kilogram": 0.001,
    "kilogram-gram": 1000,
    "pound-kilogram": 0.453592,
    "kilogram-pound": 2.20462,
    "gram-pound": 0.00220462,
    "pound-gram": 453.592,
}


    key = f"{from_unit}-{to_unit}"

    if key in convertions:
        conversion = convertions[key]
        return round(value * conversion, 4)
    else:
        return "❌ Conversion not supported."

st.markdown("<h1 style='text-align: center; color: #4CAF50;'>🌐 Unit Converter 🔄</h1>", unsafe_allow_html=True)
st.write("Welcome to the smart and simple unit converter! 🎉")

# taking input
st.markdown("### 🔢 Enter the value to convert:")
value = st.number_input("", min_value=0.0, step=0.5)

# options for units
unit_options = ["meter", "kilometer", "gram", "kilogram", "centimeter", "inch", "mile", "pound"]

# making 2 columns ansd putting selectbox in them
col1, col2 = st.columns(2)
with col1:
    from_unit = st.selectbox("📤 Convert from:", unit_options)
with col2:
    to_unit = st.selectbox("📥 Convert to:", unit_options)

# Convert button
if st.button("🚀 Convert Now"):
    result = convert_units(value, from_unit, to_unit)
    if isinstance(result, str):  # error string
        st.error(result)
    else:
        st.success(f"✅ {value} {from_unit} = {result} {to_unit}")

