import streamlit as st

def show_about():
    st.markdown("""
    <div style="padding: 2.5rem 0 2rem;">
        <div style="font-size:1rem; color:#6a7c5e; letter-spacing:0.18em; text-transform:uppercase; margin-bottom:0.6rem;">About This App</div>
        <h1 style="font-family:'DM Serif Display',serif; font-size:2.6rem; font-weight:400; color:#dde8d0; margin:0 0 0.75rem; letter-spacing:-0.01em;">
            Built With <em style="color:#b4d28c;">Care.</em>
        </h1>
        <p style="color:#6a7c5e; font-size:1.1rem; font-weight:300; max-width:560px; line-height:1.65; margin:0;">
            Everything you need to know about how VascuSense works, what it can and can't do, and who built it.
        </p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("<hr>", unsafe_allow_html=True)

    # ── HOW THE AI WORKS ──
    st.markdown("""
    <h3 style="font-family:'DM Serif Display',serif; font-weight:400; color:#dde8d0; font-size:1.4rem; margin:0 0 1.2rem;">How the AI Works — In Plain English</h3>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns(2, gap="large")

    with col1:
        for title, desc in [
            ("🧠 How does the tool work?",
             "VascuSense uses a type of math that has been trusted in medicine for a long time. Unlike newer smart tools that are hard to understand, our tool can clearly show how it makes decisions, which is very important for health."),
            ("📚 What did it learn from?",
             "The tool learned from 70,000 private patient health records. It learned to find patterns — for example, seeing that people with both high blood pressure AND high cholesterol have a higher risk of heart problems."),
            ("🎯 How accurate is it?",
             "It is correct about 73% of the time — meaning out of 100 people, it gets 73 right. That is not perfect, but it is a helpful warning. Always check with a real doctor."),
            ("⚖️ Is it fair to everyone?",
             "We test the tool on men, women, and different age groups to make sure it works fairly for everyone."),
        ]:
            st.markdown(f"""
            <div style="padding:1.1rem; background:rgba(21,26,21,0.6); border:1px solid rgba(255,255,255,0.05); border-radius:7px; margin-bottom:0.8rem;">
                <div style="font-size:1.05rem; font-weight:600; color:#dde8d0; margin-bottom:0.4rem;">{title}</div>
                <div style="font-size:1.1rem; color:#6a7c5e; line-height:1.65;">{desc}</div>
            </div>
            """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <h4 style="font-family:'DM Serif Display',serif; font-weight:400; color:#dde8d0; font-size:1.1rem; margin:0 0 1rem;">🔒 Your Privacy</h4>
        """, unsafe_allow_html=True)

        for icon, title, desc in [
            ("🗑️", "Your data is never stored",
             "When you use the tool, your numbers are used quickly and then deleted. Nothing is saved when you leave."),
            ("👤", "No account needed",
             "We never ask for your name or email. No one knows who you are."),
            ("🚫", "No tracking",
             "We do not use trackers or cookies that follow you on the internet."),
            ("🔐", "Processed locally",
             "Your health data never leaves your computer or phone. It is used right away and then thrown away."),
        ]:
            st.markdown(f"""
            <div style="display:flex; gap:0.9rem; padding:1rem; background:rgba(21,26,21,0.6); border:1px solid rgba(255,255,255,0.05); border-radius:7px; margin-bottom:0.7rem;">
                <div style="font-size:1.2rem; flex-shrink:0;">{icon}</div>
                <div>
                    <div style="font-size:1rem; font-weight:600; color:#dde8d0; margin-bottom:0.25rem;">{title}</div>
                    <div style="font-size:1.1rem; color:#6a7c5e; line-height:1.55;">{desc}</div>
                </div>
            </div>
            """, unsafe_allow_html=True)

        st.markdown("""
        <div style="padding:1rem; background:rgba(180,210,140,0.06); border:1px solid rgba(180,210,140,0.15); border-radius:7px; font-size:1.1rem; color:#6a7c5e; line-height:1.6;">
            <strong style="color:#b4d28c;">Performance Summary</strong><br>
            <span style="font-family:'DM Mono',monospace; color:#dde8d0; font-size:1rem;">
            Accuracy: 73.1% &nbsp;·&nbsp; Recall: 74.2%<br>
            Precision: 71.5% &nbsp;·&nbsp; AUC: 0.79
            </span>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("<hr>", unsafe_allow_html=True)

    # ── WHAT IT CAN & CAN'T DO ──
    st.markdown("""
    <h3 style="font-family:'DM Serif Display',serif; font-weight:400; color:#dde8d0; font-size:1.4rem; margin:0 0 1.2rem;">What VascuSense Can and Can't Do</h3>
    """, unsafe_allow_html=True)

    can_col, cant_col = st.columns(2, gap="large")
    with can_col:
        st.markdown("""
        <div style="padding:1.4rem; background:rgba(106,191,130,0.04); border:1px solid rgba(106,191,130,0.15); border-radius:10px;">
            <h5 style="color:#6abf82; font-weight:600; margin:0 0 1rem; font-size:1.05rem; text-transform:uppercase; letter-spacing:0.08em;">✅ It CAN</h5>
        """, unsafe_allow_html=True)
        for item in [
            "Give you a rough idea of your heart disease risk level",
            "Help you understand which of your habits and numbers matter most",
            "Prompt you to have a conversation with your doctor",
            "Help you track heart-healthy daily habits",
            "Explain what symptoms might mean in plain language",
            "Calculate your BMI and blood pressure category instantly",
        ]:
            st.markdown(f'<div style="font-size:1.1rem; color:#6a7c5e; display:flex; gap:0.6rem; padding:0.35rem 0; border-bottom:1px solid rgba(255,255,255,0.03);"><span style="color:#6abf82; flex-shrink:0;">✓</span><span>{item}</span></div>', unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)

    with cant_col:
        st.markdown("""
        <div style="padding:1.4rem; background:rgba(224,96,96,0.04); border:1px solid rgba(224,96,96,0.12); border-radius:10px;">
            <h5 style="color:#e06060; font-weight:600; margin:0 0 1rem; font-size:1.05rem; text-transform:uppercase; letter-spacing:0.08em;">❌ It CANNOT</h5>
        """, unsafe_allow_html=True)
        for item in [
            "Diagnose heart disease — only a doctor can do that",
            "Tell you if you're having a heart attack right now",
            "Replace a medical examination or ECG",
            "Account for your family history or genetics",
            "Detect specific conditions like arrhythmia or valve problems",
            "Give you a guaranteed answer — it's a probability estimate only",
        ]:
            st.markdown(f'<div style="font-size:1.1rem; color:#6a7c5e; display:flex; gap:0.6rem; padding:0.35rem 0; border-bottom:1px solid rgba(255,255,255,0.03);"><span style="color:#e06060; flex-shrink:0;">✗</span><span>{item}</span></div>', unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)

    st.markdown("<hr>", unsafe_allow_html=True)


    # ── DEVELOPER ──
    st.markdown("""
    <div style="text-align:center; padding:2rem 0 1rem;">
        <div style="font-size:1rem; color:#3d4d38; letter-spacing:0.15em; text-transform:uppercase; margin-bottom:1.5rem;">Built by</div>
        <div style="display:inline-block; padding:1.5rem 3rem; background:rgba(21,26,21,0.8); border:1px solid rgba(180,210,140,0.1); border-radius:50px;">
            <div style="font-family:'DM Serif Display',serif; font-size:1.8rem; color:#dde8d0; margin-bottom:0.3rem;">KHUSHI PATEL</div>
            <div style="font-size:1rem; color:#b4d28c; letter-spacing:0.18em; text-transform:uppercase;">23010101202</div>
        </div>
        <div style="margin-top:1.2rem; font-size:1rem; color:#3d4d38;">
            v2.5.0 · VascuSense Heart Health Platform · 2026
        </div>
    </div>
    """, unsafe_allow_html=True)
