import streamlit as st

# Function to calculate HEART score
def calculate_heart_score(history, ecg, age, risk_factors, troponin):
    return history + ecg + age + risk_factors + troponin

# Streamlit app
def main():
    st.title("HEART Score Calculator for Major Cardiac Events")

    st.write("""
    ## Description
    This app calculates the HEART Score for Major Cardiac Events. 
    The HEART score is used to stratify the risk of major cardiac events in patients presenting with chest pain.
    It is based on five criteria: history, ECG, age, risk factors, and troponin levels.
    """)

    st.write("### Enter the following information to calculate the HEART score:")

    history = st.selectbox("History", [0, 1, 2], format_func=lambda x: ["Slightly suspicious", "Moderately suspicious", "Highly suspicious"][x])
    ecg = st.selectbox("ECG", [0, 1, 2], format_func=lambda x: ["Normal", "Nonspecific repolarization disturbance", "Significant ST deviation"][x])
    age = st.selectbox("Age", [0, 1, 2], format_func=lambda x: ["< 45 years", "45-65 years", "> 65 years"][x])
    risk_factors = st.selectbox("Risk Factors", [0, 1, 2], format_func=lambda x: ["No risk factors", "1-2 risk factors", "≥ 3 risk factors or history of atherosclerotic disease"][x])
    troponin = st.selectbox("Troponin", [0, 1, 2], format_func=lambda x: ["≤ normal limit", "1-3x normal limit", "> 3x normal limit"][x])

    if st.button("Calculate HEART Score"):
        score = calculate_heart_score(history, ecg, age, risk_factors, troponin)
        st.write(f"### The HEART Score is: {score}")
        if score <= 3:
            st.write("### Risk: Low (0.9-1.7% risk of major adverse cardiac events)")
        elif score <= 6:
            st.write("### Risk: Moderate (12-16.6% risk of major adverse cardiac events)")
        else:
            st.write("### Risk: High (50-65% risk of major adverse cardiac events)")

if __name__ == "__main__":
    main()
