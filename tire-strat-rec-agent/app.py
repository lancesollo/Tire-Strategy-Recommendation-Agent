import streamlit as st
from tire_agent import recommend_tire, model

st.set_page_config(page_title="F1 Tire Strategy AI Agent", layout="centered")
st.title("🏎️ F1 Tire Strategy Recommendation Agent")

# Check if model loaded successfully
if model is None:
    st.error("❌ Failed to load the tire strategy model. Please check that 'tire_strategy_data.csv' exists and is properly formatted.")
    st.stop()

st.markdown("### 📊 Race Parameters")

# Input controls
col1, col2 = st.columns(2)

with col1:
    lap = st.slider("Current Lap", 1, 70, 25)
    temp = st.slider("Track Temperature (°C)", 10, 60, 35)
    weather = st.selectbox("Weather Condition", ["Dry", "Light Rain", "Moderate Rain", "Heavy Rain"])

with col2:
    current_tire = st.selectbox("Current Tire Compound", ["Soft", "Medium", "Hard", "Intermediate", "Wet", "Full Wet"])
    stint_laps = st.number_input("Current Tire Stint Length", min_value=0, max_value=50, value=10)

# Display current conditions
st.markdown("---")
st.markdown("### 🏁 Current Race Situation")
col1, col2, col3 = st.columns(3)
with col1:
    st.metric("Lap", f"{lap}/70")
with col2:
    st.metric("Track Temp", f"{temp}°C")
with col3:
    st.metric("Stint Length", f"{stint_laps} laps")

st.markdown(f"**Weather:** {weather}")
st.markdown(f"**Current Tire:** {current_tire}")

# Recommendation button
st.markdown("---")
if st.button("🧠 Get Tire Recommendation", type="primary"):
    with st.spinner("Analyzing race data..."):
        recommendation = recommend_tire(lap, temp, weather, current_tire, stint_laps)
        
        if recommendation.startswith("Error"):
            st.error(recommendation)
        else:
            st.success(f"### 🏆 Recommended Tire: **{recommendation}**")
            
            # Add some context based on the recommendation
            tire_info = {
                "Soft": "🔴 Best performance but shortest lifespan",
                "Medium": "🟡 Balanced performance and durability",
                "Hard": "⚪ Longest lasting but slower lap times",
                "Intermediate": "🟢 For light wet conditions",
                "Wet": "🔵 For moderate wet conditions", 
                "Full Wet": "🟣 For heavy rain conditions"
            }
            
            if recommendation in tire_info:
                st.info(tire_info[recommendation])

# Add some helpful information
st.markdown("---")
st.markdown("### ℹ️ About")
st.markdown("""
This AI agent uses machine learning to recommend optimal tire strategies for Formula 1 races based on:
- Current lap number and race progress
- Track temperature conditions
- Weather conditions
- Current tire compound and stint length

The recommendations are based on historical F1 tire strategy data and racing patterns.
""")

# Show model info if available
if model is not None:
    st.markdown("✅ **Model Status:** Loaded and ready")
else:
    st.markdown("❌ **Model Status:** Failed to load")
