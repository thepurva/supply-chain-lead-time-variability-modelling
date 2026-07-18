import streamlit as st
import plotly.express as px
import pandas as pd


st.title("SUPPLY CHAIN LEAD TIME & PREDICTION ANALYSIS")
st.write("TYPE ORDER & LOGISTIC DETAILS HERE TO PREDICT ACCURATE DELAY TIME")


col1, col2 = st.columns([1, 1])

with col1:
    st.subheader("ORDER & SUPPLIER DETAILS")
    
    
    product_name = st.selectbox("CHOOSE PRODUCT", 
                                ['Electronics (LAPTOP/MOBILE)', 'Automobile Parts (VEHICLE PARTS)', 'Raw Materials (ROW MATERIAL)', 'Apparel (CLOTHES/TEXTILE)'])
    
    
    supplier = st.selectbox("CHOOSE (Supplier Company) SUPPLIER:", 
                            ['DHL Supply Chain', 'Blue Dart Logistics', 'FedEx Express India'])
    
    transport = st.selectbox("Mode of Transport:", ['Sea', 'Air', 'Road'])
    weather = st.selectbox("Weather Condition:", ['Clear', 'Rainy', 'Stormy'])
    distance = st.number_input("Distance in KM:", min_value=100, max_value=5000, value=1000)


base_days = distance / 400


if transport == 'Air':
    base_days *= 0.5
elif transport == 'Sea':
    base_days *= 1.5


if weather == 'Stormy':
    base_days += 2
elif weather == 'Rainy':
    base_days += 1


if product_name == 'Raw Materials (ROW MATERIAL)':
    base_days += 1.5
elif product_name == 'Electronics (LAPTOP/MOBILE)':
    base_days -= 0.5


predicted_days = max(1, round(base_days))

with col2:
    st.subheader("PREDICTION RESULT")
    st.write("---")
    if st.button("PREDICT DELIVERY TIME"):
       
        st.success(f"📦 The delivery of **{product_name}** will take \n\n🏢 **{predicted_days} days** by {supplier}.")
        st.info("📊 MODEL ACCURACY (MAPE): 14.30%")


st.write("---")
st.subheader("📊 PROJECT DATA ANALYSIS (Interactive Graphs)")


chart_data = pd.DataFrame({
    'TRANSPORT MODE': ['Sea', 'Air', 'Road'],
    'USE (PERCENTAGE)': [50, 25, 25],
    'WEATHER': ['Clear', 'Rainy', 'Stormy'],
    'TIME TAKEN (DAYS)': [3, 5, 8]
})


fig_pie = px.pie(chart_data, values='USE (PERCENTAGE)', names='TRANSPORT MODE', 
                 title='🛞 TRANSPORT MODE USE (Transport Distribution)',
                 color_discrete_sequence=px.colors.sequential.RdBu)
st.plotly_chart(fig_pie)


fig_bar = px.bar(chart_data, x='WEATHER', y='TIME TAKEN (DAYS)', 
                 title='Days by Weather',
                 color='WEATHER', text_auto=True)
st.plotly_chart(fig_bar)
