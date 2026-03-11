import streamlit as st
import numpy as np

PARAMS = {
    'HEIGHT_MEAN': 164.41055, 'HEIGHT_STD': 7.94294,
    'WEIGHT_MEAN': 74.34133,  'WEIGHT_STD': 14.53232,
    'AP_HI_MEAN':  128.78913, 'AP_HI_STD': 18.93297,
    'AP_LO_MEAN':  96.63229,  'AP_LO_STD': 9.56673,
    'BMI_MEAN':    27.44853,  'BMI_STD': 5.21181
}

def show_risk_scanner(model, scaler):
    st.markdown("""
    <div style="padding: 2.5rem 0 2rem;">
        <div style="font-size:1rem; color:#6a7c5e; letter-spacing:0.18em; text-transform:uppercase; margin-bottom:0.6rem;">Heart Risk Assessment</div>
        <h1 style="font-family:'DM Serif Display',serif; font-size:2.6rem; font-weight:400; color:#dde8d0; margin:0 0 0.75rem; letter-spacing:-0.01em;">
            Risk <em style="color:#b4d28c;">Scanner</em>
        </h1>
        <p style="color:#6a7c5e; font-size:1.1rem; font-weight:300; max-width:560px; line-height:1.65; margin:0;">
            Type your details below. Try to be as correct as possible — better answers give a better result. It only takes 2 minutes.
        </p>
    </div>
    """, unsafe_allow_html=True)

    if not model:
        st.error("⚠️ Model files are missing. Make sure `model.pkl` and `scaler.pkl` are in the same folder as `app.py`.")
        return

    col_form, col_result = st.columns([1.5, 1], gap="large")

    with col_form:
        # ── SECTION 1: ABOUT YOU ──
        st.markdown("""
        <div style="display:flex; align-items:center; gap:10px; margin-bottom:1rem;">
            <div style="width:3px; height:1rem; background:#b4d28c; border-radius:2px;"></div>
            <span style="font-size:1rem; color:#b4d28c; letter-spacing:0.12em; text-transform:uppercase; font-weight:500;">About You</span>
        </div>
        """, unsafe_allow_html=True)

        c1, c2 = st.columns(2)
        with c1:
            age = st.number_input("How old are you?", 18, 100, 45,
                help="Your age is very important. Heart risk naturally goes up after age 45.")
        with c2:
            gender = st.selectbox("Gender", ["Female", "Male"],
                help="Men and women face different natural heart risks. This helps our tool give a better result.")
        c3, c4 = st.columns(2)
        with c3:
            height = st.number_input("Height (cm)", 100, 250, 170,
                help="Used with your weight to check your body health.")
        with c4:
            weight = st.number_input("Weight (kg)", 35, 200, 75,
                help="Used along with height to calculate your BMI.")

        # Live BMI preview
        if height > 0 and weight > 0:
            bmi_prev = weight / ((height / 100) ** 2)
            if bmi_prev < 18.5: bmi_c, bmi_color = "Underweight", "#38bdf8"
            elif bmi_prev < 25: bmi_c, bmi_color = "Healthy", "#6abf82"
            elif bmi_prev < 30: bmi_c, bmi_color = "Overweight", "#d4a84b"
            else:               bmi_c, bmi_color = "Obese", "#e06060"
            st.markdown(f"""
            <div style="padding:0.6rem 1rem; background:rgba(21,26,21,0.8); border:1px solid rgba(255,255,255,0.05); border-radius:6px; display:flex; justify-content:space-between; align-items:center; margin-top:0.3rem;">
                <span style="font-size:1.1rem; color:#6a7c5e;">Your BMI</span>
                <span style="font-size:1rem; font-weight:600; color:{bmi_color};">{bmi_prev:.1f} — {bmi_c}</span>
            </div>
            """, unsafe_allow_html=True)

        st.markdown("<div style='height:1.5rem'></div>", unsafe_allow_html=True)

        # ── SECTION 2: BLOOD PRESSURE ──
        st.markdown("""
        <div style="display:flex; align-items:center; gap:10px; margin-bottom:0.5rem;">
            <div style="width:3px; height:1rem; background:#d4a84b; border-radius:2px;"></div>
            <span style="font-size:1rem; color:#d4a84b; letter-spacing:0.12em; text-transform:uppercase; font-weight:500;">Blood Pressure</span>
        </div>
        """, unsafe_allow_html=True)

        c5, c6 = st.columns(2)
        with c5:
            ap_hi = st.number_input("Systolic (mmHg)", 70, 250, 120,
                help="The top number. Normal is under 120.")
        with c6:
            ap_lo = st.number_input("Diastolic (mmHg)", 40, 150, 80,
                help="The bottom number. Normal is under 80.")

        # Live BP classification
        if ap_hi > 0 and ap_lo > 0:
            pp = ap_hi - ap_lo
            if   ap_hi < 120 and ap_lo < 80:  bp_lbl, bp_col, bp_msg = "✓ Normal",               "#6abf82", "Your blood pressure is in the healthy range."
            elif ap_hi < 130 and ap_lo < 80:  bp_lbl, bp_col, bp_msg = "⚠ Slightly Elevated",    "#d4a84b", "A little high — watch your salt and stress levels."
            elif ap_hi < 140 or ap_lo < 90:   bp_lbl, bp_col, bp_msg = "⚠ Stage 1 High BP",      "#e0804a", "Consider speaking to your doctor about this."
            else:                              bp_lbl, bp_col, bp_msg = "🚨 Stage 2 High BP",      "#e06060", "This is significantly high. Please see a doctor."

            # st.markdown(f"""
            # <div style="padding:0.8rem 1rem; background:rgba(21,26,21,0.8); border:1px solid rgba(255,255,255,0.05); border-left:3px solid {bp_col}; border-radius:6px; margin-top:0.5rem;">
            #     <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:0.3rem;">
            #         <span style="font-size:1.1rem; color:#6a7c5e;">Blood Pressure Status</span>
            #         <span style="font-size:1rem; font-weight:600; color:{bp_col};">{bp_lbl}</span>
            #     </div>
            #     <div style="font-size:1.1rem; color:#6a7c5e;">{bp_msg} &nbsp;·&nbsp; Pulse gap: {pp} mmHg</div>
            # </div>
            # """, unsafe_allow_html=True)

        st.markdown("<div style='height:1.5rem'></div>", unsafe_allow_html=True)

        # ── SECTION 3: HEALTH MARKERS ──
        st.markdown("""
        <div style="display:flex; align-items:center; gap:10px; margin-bottom:0.5rem;">
            <div style="width:3px; height:1rem; background:#6abf82; border-radius:2px;"></div>
            <span style="font-size:1rem; color:#6abf82; letter-spacing:0.12em; text-transform:uppercase; font-weight:500;">Health Markers & Habits</span>
        </div>

        """, unsafe_allow_html=True)

        c7, c8 = st.columns(2)
        with c7:
            st.caption("Cholesterol Level  (from a blood test)")
            cholesterol = st.select_slider("Cholesterol", options=["Normal", "Above Normal", "High"],
                label_visibility="collapsed",
                help="Normal = below 200 mg/dL \n Above Normal = 200–239 \n High = 240+ mg/dL")
            st.markdown(f"""
            <div style="font-size:1rem; color:#6a7c5e; margin-top:-0.5rem; margin-bottom:0.5rem;">
                Normal &lt;200 · Above Normal 200–239 · High ≥240 mg/dL
            </div>
            """, unsafe_allow_html=True)
        with c8:
            st.caption("Blood Sugar Level  (fasting, from a blood test)")
            gluc = st.select_slider("Glucose", options=["Normal", "Above Normal", "High"],
                label_visibility="collapsed",
                help="Normal = below 100 mg/dL \n Pre-diabetes = 100–125 \n Diabetes = 126+ mg/dL")
            st.markdown(f"""
            <div style="font-size:1rem; color:#6a7c5e; margin-top:-0.5rem; margin-bottom:0.5rem;">
                Normal &lt;100 · Pre-diabetes 100–125 · High ≥126 mg/dL
            </div>
            """, unsafe_allow_html=True)

        st.markdown("<div style='height:0.75rem'></div>", unsafe_allow_html=True)

        c9, c10, c11 = st.columns(3)
        with c9:
            smoke = st.checkbox("🚬 I Smoke",
                help="Do you currently use cigarettes, cigars, or other tobacco products?")
        with c10:
            alco = st.checkbox("🍷 I Drink Alcohol Regularly",
                help="Do you drink alcohol several times a week or more?")
        with c11:
            active = st.checkbox("🏃 I Exercise Regularly", value=True,
                help="Do you get at least 30 minutes of moderate activity most days? (walking, cycling, swimming, etc.)")

    # ── RESULT PANEL ──
    with col_result:

        st.markdown("<div style='height:1rem'></div>", unsafe_allow_html=True)

        result_box = st.empty()

        # Placeholder before clicking button
        result_box.markdown("""
        <div style="background:rgba(21,26,21,0.6); border:1px solid rgba(255,255,255,0.05); border-radius:10px; padding:2.5rem; min-height:320px; display:flex; flex-direction:column; align-items:center; justify-content:center; text-align:center;">
            <div style="font-size:2.5rem; margin-bottom:1rem; opacity:0.25;">🫀</div>
            <div style="font-size:1.05rem; color:#6a7c5e; font-weight:500;">Your result will appear here</div>
            <div style="font-size:1.1rem; color:#3d4d38; margin-top:0.5rem; max-width:220px; line-height:1.6;">
                Fill in your details on the left and press the button below.
            </div>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("<div style='height:1rem'></div>", unsafe_allow_html=True)

        run = st.button("🫀   GET MY RESULT", type="primary", use_container_width=True)

        if run:

            gender_val = 1 if gender == "Male" else 0

            chol_map = {"Normal":0,"Above Normal":1,"High":2}
            gluc_map = {"Normal":0,"Above Normal":1,"High":2}

            bmi_raw = weight / ((height / 100) ** 2)

            h_s   = (height - PARAMS['HEIGHT_MEAN']) / PARAMS['HEIGHT_STD']
            w_s   = (weight - PARAMS['WEIGHT_MEAN']) / PARAMS['WEIGHT_STD']
            ahi_s = (ap_hi - PARAMS['AP_HI_MEAN']) / PARAMS['AP_HI_STD']
            alo_s = (ap_lo - PARAMS['AP_LO_MEAN']) / PARAMS['AP_LO_STD']
            b_s   = (bmi_raw - PARAMS['BMI_MEAN']) / PARAMS['BMI_STD']

            x = np.array([[

                gender_val,
                h_s,
                w_s,
                ahi_s,
                alo_s,
                chol_map[cholesterol],
                gluc_map[gluc],
                1 if smoke else 0,
                1 if alco else 0,
                1 if active else 0,
                age,
                b_s

            ]])

            x_final = scaler.transform(x)

            prob = model.predict_proba(x_final)[0][1] * 100

            # -------- HEART AGE --------

            heart_age = age

            if ap_hi >= 140:
                heart_age += 5
            elif ap_hi >= 130:
                heart_age += 2

            if bmi_raw >= 30:
                heart_age += 4
            elif bmi_raw >= 25:
                heart_age += 2

            if smoke:
                heart_age += 6

            if chol_map[cholesterol] == 2:
                heart_age += 3
            elif chol_map[cholesterol] == 1:
                heart_age += 1

            if not active:
                heart_age += 3

            if alco:
                heart_age += 2

            heart_age = min(heart_age, age + 20)

            heart_age_diff = heart_age - age

            # Heart age color

            if heart_age_diff > 5:
                heart_age_color = "#e06060"
            elif heart_age_diff > 0:
                heart_age_color = "#d4a84b"
            else:
                heart_age_color = "#6abf82"

            # -------- RISK CATEGORY --------

            if prob >= 70:

                status="HIGH RISK"
                color="#e06060"
                emoji="🚨"

                plain_msg="Your numbers show a high chance of heart problems. Please consult a doctor soon."

                next_steps=[

                    "📅 Book a doctor appointment soon",
                    "💊 Ask about blood pressure or cholesterol treatment",
                    "🥗 Reduce fried food and processed snacks",
                    "🚭 Quit smoking if you smoke",
                    "🏃 Start light daily walking"

                ]

            elif prob >= 40:

                status="ELEVATED RISK"
                color="#d4a84b"
                emoji="⚠️"

                plain_msg="Some of your numbers are a bit high. Healthy lifestyle changes can reduce your risk."

                next_steps=[

                    "📅 Mention these results during your next checkup",
                    "🏃 Exercise at least 30 minutes most days",
                    "🧂 Reduce salt intake",
                    "🍎 Eat more fruits and vegetables",
                    "😴 Aim for 7–8 hours of sleep"

                ]

            else:

                status="LOW RISK"
                color="#6abf82"
                emoji="✅"

                plain_msg="Great news — your numbers look healthy. Keep up your good habits."

                next_steps=[

                    "✅ Continue your healthy lifestyle",
                    "📅 Routine health checkup yearly",
                    "🏃 Maintain regular exercise",
                    "🥗 Keep a heart healthy diet",
                    "📊 Check BP and cholesterol every 1–2 years"

                ]

            # BMI category

            if bmi_raw < 18.5:
                bmi_cat="Underweight"
            elif bmi_raw < 25:
                bmi_cat="Healthy"
            elif bmi_raw < 30:
                bmi_cat="Overweight"
            else:
                bmi_cat="Obese"

            next_html="".join([

                f'<div style="font-size:0.95rem;color:#6a7c5e;padding:0.4rem 0;border-bottom:1px solid rgba(255,255,255,0.03);">{s}</div>'

                for s in next_steps

            ])

            # -------- RESULT CARD --------

            result_box.markdown(f"""

            <div style="background:rgba(21,26,21,0.95);border:1px solid rgba(255,255,255,0.06);border-top:3px solid {color};border-radius:10px;padding:2rem;">

            <div style="font-size:1rem;color:#6a7c5e;letter-spacing:0.14em;text-transform:uppercase;margin-bottom:0.5rem;">
            Your Result
            </div>

            <div style="font-size:1.9rem;color:{color};margin-bottom:0.25rem;">
            {emoji} {status}
            </div>

            <div style="font-size:1.1rem;color:#dde8d0;margin-bottom:1rem;">
            Risk Score:
            <span style="color:{color};font-family:monospace;">{prob:.0f}%</span>
            </div>

            <p style="color:#6a7c5e;margin-bottom:1rem;">
            {plain_msg}
            </p>


            <div style="font-size:0.9rem;color:#b4d28c;margin-bottom:0.6rem;">
            What to Do Next
            </div>

            {next_html}

            </div>

            """, unsafe_allow_html=True)