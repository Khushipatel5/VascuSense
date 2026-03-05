import streamlit as st
import numpy as np
import time

PARAMS = {
    'HEIGHT_MEAN': 164.41055, 'HEIGHT_STD': 7.94294,
    'WEIGHT_MEAN': 74.34133,  'WEIGHT_STD': 14.53232,
    'AP_HI_MEAN': 128.78913,  'AP_HI_STD': 18.93297,
    'AP_LO_MEAN': 96.63229,   'AP_LO_STD': 9.56673,
    'BMI_MEAN': 27.44853,     'BMI_STD': 5.21181
}

def show_risk_scanner(model, scaler):
    # Dynamic styling for this page
    st.markdown("""
        <style>
        .stNumberInput input { background-color: rgba(255,255,255,0.05) !important; border: 1px solid rgba(255,255,255,0.1) !important; }
        .stSelectbox > div > div { background-color: rgba(255,255,255,0.05) !important; }
        div[data-testid="stContainer"] { background-color: transparent; }
        </style>
    """, unsafe_allow_html=True)

    st.markdown("""
        <div style="text-align: center; margin-bottom: 2rem; padding: 1.5rem 0; border-bottom: 1px solid rgba(255,255,255,0.1);">
            <h1 style="background: linear-gradient(90deg, #e2e8f0, #94a3b8); -webkit-background-clip: text; -webkit-text-fill-color: transparent; font-weight: 800; font-size: 2.2rem; letter-spacing: -1px; margin: 0;">
                <span style="color: #00f2ff; -webkit-text-fill-color: #00f2ff;">DIAGNOSTICS</span> TERMINAL
            </h1>
        </div>
    """, unsafe_allow_html=True)
    
    if not model:
        st.error("Engine Offline: Model artifacts missing.")
    else:
        # Main Layout: Two Columns
        col_main, col_sidebar = st.columns([1.6, 1], gap="large")
        
        with col_main:
            # Section 1: Bio-Metrics
            st.markdown("""
                <div style="margin-bottom: 15px; display: flex; align-items: center; gap: 10px;">
                    <span style="font-size: 1.2rem;">👤</span>
                    <h4 style="margin: 0; color: #e2e8f0;">Bio-Metric Profile</h4>
                </div>
            """, unsafe_allow_html=True)
            
            c1, c2 = st.columns(2)
            with c1:
                age = st.number_input("Age (Years)", 18, 100, 45)
            with c2:
                gender = st.selectbox("Gender", ["Female", "Male"])
            
            c3, c4 = st.columns(2)
            with c3:
                height = st.number_input("Height (cm)", 100, 250, 170)
            with c4:
                weight = st.number_input("Weight (kg)", 35, 200, 75)
            
            st.markdown("---")

            # Section 2: Clinical Vitals
            st.markdown("""
                <div style="margin-bottom: 15px; display: flex; align-items: center; gap: 10px;">
                    <span style="font-size: 1.2rem;">🩺</span>
                    <h4 style="margin: 0; color: #e2e8f0;">Clinical Vitals</h4>
                </div>
            """, unsafe_allow_html=True)
            
            c5, c6 = st.columns(2)
            with c5:
                ap_hi = st.number_input("Systolic BP (mmHg)", 70, 250, 120)
            with c6:
                ap_lo = st.number_input("Diastolic BP (mmHg)", 40, 150, 80)
            
            st.markdown("---")

            # Section 3:Labs & Lifestyle
            st.markdown("""
                <div style="margin-bottom: 15px; display: flex; align-items: center; gap: 10px;">
                    <span style="font-size: 1.2rem;">🧬</span>
                    <h4 style="margin: 0; color: #e2e8f0;">Labs & Lifestyle</h4>
                </div>
            """, unsafe_allow_html=True)
            
            c7, c8 = st.columns(2)
            with c7:
                st.caption("Cholesterol Level")
                cholesterol = st.select_slider("Cholesterol", options=["Normal", "Above Normal", "High"], label_visibility="collapsed")
            with c8:
                st.caption("Glucose Level")
                gluc = st.select_slider("Glucose", options=["Normal", "Above Normal", "High"], label_visibility="collapsed")
            
            st.markdown("<div style='height: 10px'></div>", unsafe_allow_html=True)
            
            l1, l2, l3 = st.columns(3)
            with l1:
                smoke = st.checkbox("Smoker")
            with l2:
                alco = st.checkbox("Alcohol")
            with l3:
                active = st.checkbox("Active", value=True)

        with col_sidebar:
            st.markdown("<div style='height: 20px'></div>", unsafe_allow_html=True)
            result_container = st.empty()
            
            # Initial State
            result_container.markdown("""
                <div class="glass-card" style="height: 300px; display: flex; align-items: center; justify-content: center; text-align: center; border: 1px dashed rgba(255,255,255,0.2); border-radius: 12px;">
                    <div>
                        <div style="font-size: 3.5rem; opacity: 0.3; margin-bottom: 10px;">🔬</div>
                        <h4 style="color: #64748b;">System Ready</h4>
                        <p style="color: #475569; font-size: 0.9rem;">Awaiting bio-metric input data...</p>
                    </div>
                </div>
            """, unsafe_allow_html=True)

            st.markdown("<div style='height: 20px'></div>", unsafe_allow_html=True)
            run_btn = st.button("RUN DIAGNOSTIC SEQUENCE", type="primary", use_container_width=True)
            
            if run_btn:
                # Logic block (kept exactly as it was in your previous request's logic state)
                # Note: Reverting logic to exactly how the user had it in previous turns if possible, 
                # but applying the UI layout wrapper.
                
                # Original logic reconstruction:
                gender_val = 1 if gender == "Male" else 0
                chol_map = {"Normal": 0, "Above Normal": 1, "High": 2}
                gluc_map = {"Normal": 0, "Above Normal": 1, "High": 2}
                
                bmi_raw = weight / ((height / 100) ** 2)
                
                # Manual scaling logic from user's original file
                h_s = (height - PARAMS['HEIGHT_MEAN']) / PARAMS['HEIGHT_STD']
                w_s = (weight - PARAMS['WEIGHT_MEAN']) / PARAMS['WEIGHT_STD']
                ahi_s = (ap_hi - PARAMS['AP_HI_MEAN']) / PARAMS['AP_HI_STD']
                alo_s = (ap_lo - PARAMS['AP_LO_MEAN']) / PARAMS['AP_LO_STD']
                b_s = (bmi_raw - PARAMS['BMI_MEAN']) / PARAMS['BMI_STD']
                
                x = np.array([[
                    gender_val, h_s, w_s, ahi_s, alo_s, 
                    chol_map[cholesterol], gluc_map[gluc], 
                    1 if smoke else 0, 1 if alco else 0, 1 if active else 0, 
                    age, b_s
                ]])
                
                # Preserving the exact prediction flow
                x_final = scaler.transform(x)
                prob = model.predict_proba(x_final)[0][1] * 100
                
                # New UI Result Logic
                if prob >= 70:
                    status = "High Risk"
                    color_hex = "#ff0a54"
                    glow = "0 0 40px rgba(255, 10, 84, 0.3)"
                    msg = "Model detects patterns consistent with high cardiovascular risk."
                    icon = "🚨"
                elif prob >= 40:
                    status = "Moderate Risk"
                    color_hex = "#ffb703"
                    glow = "0 0 40px rgba(255, 183, 3, 0.3)"
                    msg = "Model detects patterns consistent with moderate cardiovascular risk."
                    icon = "⚠️"
                else:
                    status = "Low Risk"
                    color_hex = "#0aff60"
                    glow = "0 0 40px rgba(10, 255, 96, 0.3)"
                    msg = "Bio-markers appear to be within healthy operating parameters."
                    icon = "✅"
                
                result_container.markdown(f"""
<div class="glass-card" style="background: linear-gradient(180deg, {color_hex}11 0%, rgba(0,0,0,0) 100%); border: 1px solid {color_hex}44; text-align: center; border-radius: 12px; padding: 2rem; box-shadow: {glow}; animation: slideIn 0.5s ease-out;">
<span style="font-size: 3rem; display: block; margin-bottom: 10px;">{icon}</span>
<div style="font-size: 2.5rem; font-weight: 800; color: #fff; line-height: 1.2; text-shadow: 0 0 15px {color_hex}; margin-bottom: 0.5rem;">
{status}
</div>
<div style="color: {color_hex}; font-size: 0.8rem; text-transform: uppercase; letter-spacing: 2px; margin-bottom: 1.5rem;">Risk Assessment</div>
<p style="color: #94a3b8; font-size: 0.85rem; line-height: 1.5;">{msg}</p>
<div style="margin-top: 1.5rem; padding-top: 1rem; border-top: 1px solid rgba(255,255,255,0.1); display: grid; grid-template-columns: 1fr 1fr; gap: 10px;">
    <div>
        <div style="color: #94a3b8; font-size: 0.75rem; text-transform: uppercase;">BMI</div>
        <div style="color: #e2e8f0; font-size: 1.1rem; font-weight: 700;">{bmi_raw:.1f}</div>
    </div>
    <div>
        <div style="color: #94a3b8; font-size: 0.75rem; text-transform: uppercase;">Pulse Pressure</div>
        <div style="color: #e2e8f0; font-size: 1.1rem; font-weight: 700;">{ap_hi - ap_lo}</div>
    </div>
</div>
</div>
""", unsafe_allow_html=True)
