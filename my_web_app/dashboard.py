import streamlit as st
import pandas as pd
import numpy as np

def show_dashboard():
    # ── HERO ──
    st.markdown("""
    <div style="padding: 3rem 0 2rem;">
        <div style="font-size:1rem; color:#6a7c5e; letter-spacing:0.18em; text-transform:uppercase; margin-bottom:0.75rem;">
            Your Heart Health, Simplified
        </div>
        <h1 style="font-family:'DM Serif Display',serif; font-size:3.2rem; font-weight:400; line-height:1.1; color:#dde8d0; margin:0 0 1.2rem; letter-spacing:-0.02em;">
            Know Your Heart.<br><em style="color:#b4d28c;">Before It Speaks.</em>
        </h1>
        <p style="color:#6a7c5e; font-size:1.05rem; font-weight:300; max-width:520px; line-height:1.7; margin:0;">
            VascuSense uses a smart tool tested on over 70,000 real patient records to help you check your heart risk — fast, safe, and free.
        </p>
    </div>
    """, unsafe_allow_html=True)

    col_cta, _, col_s1, col_s2, col_s3 = st.columns([1.2, 0.2, 1, 1, 1])
    with col_cta:
        if st.button("▶   Check My Risk Now"):
            st.session_state.page = "Risk Scanner"
            st.rerun()
    with col_s1:
        st.metric("Patients Studied", "70,000+")
    with col_s2:
        st.metric("Prediction Accuracy", "73.1%")
    with col_s3:
        st.metric("Takes Only", "~2 Minutes")

    st.markdown("<hr>", unsafe_allow_html=True)

    # ── HOW IT WORKS ──
    st.markdown("""
    <div style="text-align:center; margin-bottom:2rem;">
        <div style="font-size:1rem; color:#6a7c5e; letter-spacing:0.15em; text-transform:uppercase; margin-bottom:0.5rem;">Simple 3-Step Process</div>
        <h3 style="font-family:'DM Serif Display',serif; font-weight:400; color:#dde8d0; margin:0; font-size:1.8rem;">How VascuSense Works</h3>
    </div>
    """, unsafe_allow_html=True)

    s1, s2, s3 = st.columns(3, gap="large")
    for col, num, icon, title, desc in [
        (s1, "01", "📋", "Enter Your Details",
         "Type in some basic details — your age, height, weight, blood pressure, and a few questions about your daily life. You don't need to sign up. We don't save your data."),
        (s2, "02", "🤖", "AI Analyses Your Data",
         "Our tool quickly checks your numbers against 70,000+ other people to find out your heart risk."),
        (s3, "03", "📊", "Get Your Result",
         "You will get a clear result (Low / Medium / High Risk), see your health numbers, and get easy tips on what to do next."),
    ]:
        with col:
            st.markdown(f"""
            <div style="padding:1.5rem; background:rgba(21,26,21,0.7); border:1px solid rgba(255,255,255,0.05); border-radius:10px; text-align:center;">
                <div style="font-size:1rem; color:#6a7c5e; letter-spacing:0.15em; text-transform:uppercase; margin-bottom:0.5rem;">Step {num}</div>
                <div style="font-size:2rem; margin-bottom:0.75rem;">{icon}</div>
                <div style="font-size:1rem; font-weight:600; color:#dde8d0; margin-bottom:0.5rem;">{title}</div>
                <div style="font-size:1rem; color:#6a7c5e; line-height:1.6;">{desc}</div>
            </div>
            """, unsafe_allow_html=True)

    st.markdown("<hr>", unsafe_allow_html=True)

    # ── QUICK BMI CALCULATOR ──
    st.markdown("""
    <div style="margin-bottom:1.5rem;">
        <div style="font-size:1rem; color:#6a7c5e; letter-spacing:0.15em; text-transform:uppercase; margin-bottom:0.5rem;">Quick Tool</div>
        <h3 style="font-family:'DM Serif Display',serif; font-weight:400; color:#dde8d0; margin:0 0 0.5rem; font-size:1.6rem;">BMI Calculator</h3>
        <p style="color:#6a7c5e; font-size:1.05rem; margin:0;">BMI (Body Mass Index) is a simple way to check if your weight is healthy for your height. Our tool uses this to check your heart.</p>
    </div>
    """, unsafe_allow_html=True)

    bmi_col, result_col = st.columns([1, 1], gap="large")
    with bmi_col:
        b1, b2 = st.columns(2)
        with b1:
            bmi_h = st.number_input("Your Height (cm)", 100, 250, 170, key="bmi_h")
        with b2:
            bmi_w = st.number_input("Your Weight (kg)", 30, 200, 70, key="bmi_w")

        if bmi_h > 0 and bmi_w > 0:
            bmi = bmi_w / ((bmi_h / 100) ** 2)
            if bmi < 18.5:
                cat, color, advice = "Underweight", "#38bdf8", "You may need to gain some weight. Talk to your doctor about a healthy plan."
            elif bmi < 25:
                cat, color, advice = "Healthy Weight ✓", "#6abf82", "Great! Your weight is in the healthy range. Keep it up."
            elif bmi < 30:
                cat, color, advice = "Overweight", "#d4a84b", "Losing even 5–10% of body weight can noticeably lower your heart risk."
            else:
                cat, color, advice = "Obese", "#e06060", "This range carries higher heart risk. Small, consistent changes make a big difference."

            with result_col:
                st.markdown(f"""
                <div style="padding:1.5rem; background:rgba(21,26,21,0.8); border:1px solid rgba(255,255,255,0.05); border-top:3px solid {color}; border-radius:10px; margin-top:1.8rem;">
                    <div style="font-size:1rem; color:#6a7c5e; letter-spacing:0.1em; text-transform:uppercase; margin-bottom:0.4rem;">Your BMI</div>
                    <div style="font-family:'DM Serif Display',serif; font-size:3rem; color:{color}; line-height:1; margin-bottom:0.4rem;">{bmi:.1f}</div>
                    <div style="font-size:1rem; font-weight:600; color:{color}; margin-bottom:0.75rem;">{cat}</div>
                    <div style="font-size:1rem; color:#6a7c5e; line-height:1.6; border-top:1px solid rgba(255,255,255,0.04); padding-top:0.75rem;">{advice}</div>
                </div>
                """, unsafe_allow_html=True)

                # BMI scale visual
                st.markdown("""
                <div style="margin-top:1rem;">
                    <div style="display:flex; height:6px; border-radius:3px; overflow:hidden; margin-bottom:0.4rem;">
                        <div style="flex:1.85; background:#38bdf8;"></div>
                        <div style="flex:0.65; background:#6abf82;"></div>
                        <div style="flex:0.5; background:#d4a84b;"></div>
                        <div style="flex:1; background:#e06060;"></div>
                    </div>
                    <div style="display:flex; justify-content:space-between; font-size:1rem; color:#3d4d38;">
                        <span>Under 18.5</span><span>18.5–24.9</span><span>25–29.9</span><span>30+</span>
                    </div>
                </div>
                """, unsafe_allow_html=True)

    st.markdown("<hr>", unsafe_allow_html=True)

    # ── WHAT AFFECTS YOUR HEART ──
    st.markdown("""
    <div style="text-align:center; margin-bottom:2rem;">
        <div style="font-size:1rem; color:#6a7c5e; letter-spacing:0.15em; text-transform:uppercase; margin-bottom:0.5rem;">What We Look At</div>
        <h3 style="font-family:'DM Serif Display',serif; font-weight:400; color:#dde8d0; margin:0; font-size:1.8rem;">11 Factors That Affect Your Heart</h3>
        <p style="color:#6a7c5e; margin-top:0.5rem; font-size:1.05rem;">These are the signals our AI uses to calculate your risk.</p>
    </div>
    """, unsafe_allow_html=True)

    features = [
        ("🎂", "Age",              "As you get older, your risk naturally goes up, especially after age 45.",          "#b4d28c"),
        ("⚧",  "Gender",              "Men and women face different heart risks because of how our bodies naturally work.",    "#d4a84b"),
        ("⚖️", "Height & Weight",  "These help us find your BMI, which shows if extra weight is putting stress on your heart.", "#6abf82"),
        ("💉", "Systolic BP",      "The top number in your blood pressure test. This is very important. Normal is under 120.", "#b4d28c"),
        ("💉", "Diastolic BP",     "The bottom number in your blood pressure test. Normal is under 80.",  "#d4a84b"),
        ("🧈", "Cholesterol",      "Too much fat in your blood can block your body's pipes over time. You check this with a blood test.",   "#6abf82"),
        ("🍬", "Blood Sugar",      "High sugar in your blood can hurt your heart. If you catch it early, it is easy to handle.",         "#b4d28c"),
        ("🚬", "Smoking",          "Smoking is very bad for your heart. It hurts your body and raises your blood pressure.",          "#d4a84b"),
        ("🍷", "Alcohol",          "Drinking alcohol often can raise your blood pressure and make your heart work too hard over time.",          "#6abf82"),
        ("🏃", "Exercise",         "Moving your body is one of the best things you can do. Just 30 minutes of walking everyday helps a lot.",   "#b4d28c"),
        ("📏", "Pulse Pressure",   "The gap between your two blood pressure numbers. If it is high, your blood pipes might be getting stiff.", "#d4a84b"),
    ]

    cols = st.columns(3)
    for i, (icon, name, desc, color) in enumerate(features):
        with cols[i % 3]:
            st.markdown(f"""
            <div style="padding:1rem 1.1rem; background:rgba(21,26,21,0.5); border:1px solid rgba(255,255,255,0.04); border-left:2px solid {color}; border-radius:6px; margin-bottom:0.75rem; display:flex; gap:0.75rem; align-items:flex-start;">
                <div style="font-size:1.1rem; flex-shrink:0;">{icon}</div>
                <div>
                    <div style="font-size:1rem; font-weight:600; color:#dde8d0; margin-bottom:0.2rem;">{name}</div>
                    <div style="font-size:1.1rem; color:#6a7c5e; line-height:1.55;">{desc}</div>
                </div>
            </div>
            """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)
    st.info("⚕️  **Note:** VascuSense is a helpful tool, but it is not a doctor. Always talk to your real doctor for medical advice.")
