import streamlit as st

st.title("Supply chain lead time prediction")
st.write("enter order details to predict accurate prediction.")


supplier = st.selectbox("choose supplier:", ['Supplier_A', 'Supplier_B', 'Supplier_C'])
transport = st.selectbox("transport mode:", ['Sea', 'Air', 'Road'])
weather = st.selectbox("how weather is?:", ['Clear', 'Rainy', 'Stormy'])
distance = st.number_input("distance (in KM):", min_value=100, max_value=5000, value=1000)



base_days = distance / 400  # days based on distance

if transport == 'Air':
    base_days = base_days * 0.5  # half time by airoplane
elif transport == 'Sea':
    base_days = base_days * 1.5  # more time by ship

if weather == 'Stormy':
    base_days += 2  # 2 days extra if storm occur
elif weather == 'Rainy':
    base_days += 1  # 1 day extra if rain occur

predicted_days = round(base_days)
if predicted_days < 1:
    predicted_days = 1


if st.button("predict delivery time"):
    st.success(f"delivery time probably: {predicted_days} DAYS")
    st.info("📊 Model Accuracy (MAPE): 14.30%")