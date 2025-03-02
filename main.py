import streamlit as st
from length_conversion import convert_length
from units import length_units, weight_units
from weight_conversion import convert_weight

st.set_page_config(layout="wide")


# ✅ Streamlit UI
st.title("🌍 Unit Converter")

# 📌 Tabs for Length & Weight
tab1, tab2 = st.tabs(["📏 Length", "⚖️ Weight"])

with tab1:  # Length Conversion
    st.markdown("### 🚀 **Features:**")

    col1, col2 = st.columns(2)

    # 📝 Features Section
    with col1:
        st.markdown("""
        - ✅ Convert between **30+ Length Units** (Meters, Kilometers, Miles, etc.)
        - ✅ Supports **Metric, Imperial, Nautical, and Astronomical** units
        - ✅ **Instant Conversion** with real-time updates """)
    with col2:
        st.markdown("""
        - ✅ Shows **Conversion Formula** for better understanding
        - ✅ Simple and **User-Friendly Interface**
        - ✅ Accurate and **scientific unit conversions** """)

    col3, col4 = st.columns(2)

    with col3:
        from_unit = st.selectbox("Convert From:", length_units, key="length_from")

    with col4:
        to_unit = st.selectbox("Convert To:", length_units, key="length_to")

    value = st.number_input("Enter Value:", min_value=0.0, format="%.4f", key="length_value")

    if from_unit and to_unit:
        converted_value, formula = convert_length(value, from_unit, to_unit)
        st.success(f"✅ {value} {from_unit} = {converted_value:.4f} {to_unit}")
        st.info(f"📌 Formula Used: **{formula}**")

with tab2:  # Weight Conversion
    st.markdown("### 🚀 **Features:**")

    col1, col2 = st.columns(2)

    # 📝 Features Section
    with col1:
        st.markdown("""
        - ✅ Convert between **20+ Weight Units** (Kilograms, Pounds, Ounces, etc.)
        - ✅ Supports **Metric, Imperial, and Traditional** units
        - ✅ **Instant Conversion** with real-time updates """)
    with col2:
        st.markdown("""
        - ✅ Shows **Conversion Formula** for better understanding
        - ✅ Simple and **User-Friendly Interface**
        - ✅ Accurate and **scientific unit conversions** """)

    col3, col4 = st.columns(2)

    with col3:
        from_unit = st.selectbox("Convert From:", weight_units, key="weight_from")

    with col4:
        to_unit = st.selectbox("Convert To:", weight_units, key="weight_to")

    value = st.number_input("Enter Value:", min_value=0.0, format="%.4f", key="weight_value")

    if from_unit and to_unit:
        converted_value, formula = convert_weight(value, from_unit, to_unit)
        st.success(f"✅ {value} {from_unit} = {converted_value:.4f} {to_unit}")
        st.info(f"📌 Formula Used: **{formula}**")
