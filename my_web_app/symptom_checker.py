import streamlit as st

def show_symptom_checker():
    st.markdown("""
    <div style="padding: 2.5rem 0 2rem;">
        <div style="font-size:1rem; color:#6a7c5e; letter-spacing:0.18em; text-transform:uppercase; margin-bottom:0.6rem;">Know the Signs</div>
        <h1 style="font-family:'DM Serif Display',serif; font-size:2.6rem; font-weight:400; color:#dde8d0; margin:0 0 0.75rem; letter-spacing:-0.01em;">
            Symptom <em style="color:#b4d28c;">Checker</em>
        </h1>
        <p style="color:#6a7c5e; font-size:1.1rem; font-weight:300; max-width:580px; line-height:1.65; margin:0;">
            Not sure if the way you feel is related to your heart? This tool helps you learn about common heart signs in easy words — and tells you when to get help.
        </p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div style="padding:1rem 1.2rem; background:rgba(224,96,96,0.06); border:1px solid rgba(224,96,96,0.15); border-radius:8px; margin-bottom:2rem;">
        <span style="font-size:1.1rem; color:#e06060; font-weight:600;">🚨 Emergency: </span>
        <span style="font-size:1.1rem; color:#6a7c5e;">If you suddenly have chest pain, can't breathe, feel your arm going numb, or think you are having a heart attack — <strong style="color:#dde8d0;">call for an ambulance (999/911/112) right now.</strong> Do not wait. Do not use this tool.</span>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("<hr>", unsafe_allow_html=True)

    # ── INTERACTIVE SYMPTOM CHECKER ──
    st.markdown("""
    <h3 style="font-family:'DM Serif Display',serif; font-weight:400; color:#dde8d0; font-size:1.5rem; margin:0 0 0.5rem;">What are you experiencing?</h3>
    <p style="color:#6a7c5e; font-size:1rem; margin-bottom:1.5rem;">Check all that apply. We'll tell you what it might mean and what to do.</p>
    """, unsafe_allow_html=True)

    col_a, col_b = st.columns(2, gap="large")

    with col_a:
        st.markdown('<div style="font-size:1rem; color:#b4d28c; letter-spacing:0.1em; text-transform:uppercase; margin-bottom:0.75rem; font-weight:500;">Physical Symptoms</div>', unsafe_allow_html=True)
        chest_pain     = st.checkbox("Chest pain, tightness, or pressure")
        chest_pain_exer= st.checkbox("Chest discomfort when exercising or climbing stairs")
        shortness      = st.checkbox("Shortness of breath (even at rest or lying down)")
        palpitations   = st.checkbox("Heart racing, fluttering, or skipping beats")
        dizziness      = st.checkbox("Dizziness or feeling faint")
        swollen_legs   = st.checkbox("Swollen ankles or feet")
        fatigue        = st.checkbox("Unusual tiredness — exhausted doing small things")

    with col_b:
        st.markdown('<div style="font-size:1rem; color:#d4a84b; letter-spacing:0.1em; text-transform:uppercase; margin-bottom:0.75rem; font-weight:500;">Less Obvious Signs</div>', unsafe_allow_html=True)
        jaw_pain       = st.checkbox("Pain spreading to the jaw, neck, back, or left arm")
        cold_sweat     = st.checkbox("Breaking out in a cold sweat for no clear reason")
        nausea         = st.checkbox("Nausea or feeling sick without obvious cause")
        sleep_trouble  = st.checkbox("Waking up gasping or feeling breathless at night")
        snoring        = st.checkbox("Loud snoring or told you stop breathing in sleep")
        headaches      = st.checkbox("Frequent headaches, especially at the back of the head")
        vision_blur    = st.checkbox("Blurred vision or seeing spots")

    st.markdown("<div style='height:1rem'></div>", unsafe_allow_html=True)
    check_btn = st.button("🔍   ANALYSE MY SYMPTOMS", use_container_width=False)

    symptoms_selected = [
        chest_pain, chest_pain_exer, shortness, palpitations, dizziness,
        swollen_legs, fatigue, jaw_pain, cold_sweat, nausea,
        sleep_trouble, snoring, headaches, vision_blur
    ]
    total = sum(symptoms_selected)

    if check_btn:
        # ── EMERGENCY COMBO ──
        if chest_pain and (jaw_pain or shortness or cold_sweat or nausea):
            st.markdown("""
            <div style="padding:2rem; background:rgba(224,96,96,0.08); border:2px solid #e06060; border-radius:12px; text-align:center; margin:1rem 0;">
                <div style="font-size:2rem; margin-bottom:0.5rem;">🚨</div>
                <h3 style="font-family:'DM Serif Display',serif; color:#e06060; font-size:1.5rem; margin:0 0 0.75rem;">Call Emergency Services Now</h3>
                <p style="color:#dde8d0; font-size:1.1rem; line-height:1.65; max-width:500px; margin:0 auto;">
                    The combination of symptoms you've selected — especially chest pain with jaw/arm pain, breathlessness, sweating, or nausea — are classic warning signs of a heart attack.
                    <strong>Do not wait. Call 112 or 911 right now.</strong> Every minute matters.
                </p>
            </div>
            """, unsafe_allow_html=True)
            return

        # ── RESULT CARDS ──
        if total == 0:
            st.markdown("""
            <div style="padding:1.5rem; background:rgba(106,191,130,0.06); border:1px solid rgba(106,191,130,0.2); border-radius:10px; text-align:center;">
                <div style="font-size:1.5rem; margin-bottom:0.5rem;">✅</div>
                <div style="font-size:1rem; font-weight:600; color:#6abf82; margin-bottom:0.4rem;">No symptoms selected</div>
                <div style="font-size:1rem; color:#6a7c5e; line-height:1.6;">Great! No heart symptoms checked. Remember, some heart conditions are "silent" — so regular checkups are still important, especially after age 40.</div>
            </div>
            """, unsafe_allow_html=True)
            return

        st.markdown(f"""
        <div style="font-size:1rem; color:#6a7c5e; margin-bottom:1.5rem;">
            You selected <strong style="color:#dde8d0;">{total} symptom{'s' if total > 1 else ''}</strong>. Here's what they might mean:
        </div>
        """, unsafe_allow_html=True)

        symptom_info = []

        if chest_pain:
            symptom_info.append(("🫀", "Chest Pain or Tightness", "#e06060", "HIGH",
                "Chest pain is the most well-known heart symptom. It can feel like pressure, squeezing, burning, or heaviness. It might come and go, or it might be constant.",
                "See a doctor as soon as possible — today if you can. If it comes on suddenly or is severe, call emergency services."))

        if chest_pain_exer:
            symptom_info.append(("⚡", "Chest Discomfort During Activity", "#e0804a", "HIGH",
                "If your chest hurts or feels tight only when you walk, climb stairs, or exercise, this can be a sign that your heart isn't getting enough blood during exertion. This is called angina.",
                "This is an important symptom. Book a doctor's appointment this week for a heart check. Avoid heavy exertion until then."))

        if shortness:
            symptom_info.append(("💨", "Shortness of Breath", "#e0804a", "MODERATE-HIGH",
                "Feeling out of breath when doing small things — or when lying flat — can mean your heart is struggling to pump well, causing fluid to collect in your lungs.",
                "If it happens at rest or wakes you up at night, see a doctor soon. If sudden and severe, call emergency services."))

        if palpitations:
            symptom_info.append(("💓", "Heart Racing or Fluttering", "#d4a84b", "MODERATE",
                "Feeling your heart skip, race, or flutter can be harmless (caused by coffee, stress, or worry), but it could also mean a problem with your heart's rhythm.",
                "If it happens often, lasts a long time, or comes with dizziness or fainting — get checked. An ECG (electrocardiogram) can read your heart rhythm."))

        if dizziness:
            symptom_info.append(("😵", "Dizziness or Feeling Faint", "#d4a84b", "MODERATE",
                "Lightheadedness can happen for many reasons — dehydration, low blood sugar, standing up too fast. But it can also mean your blood pressure is too high or too low.",
                "Check your blood pressure. If dizziness is frequent or you've actually fainted, see a doctor."))

        if swollen_legs:
            symptom_info.append(("🦵", "Swollen Ankles or Feet", "#d4a84b", "MODERATE",
                "When the heart isn't pumping well, fluid can back up and cause swelling in your lower legs, ankles, and feet — especially by the end of the day.",
                "If the swelling is new, persistent, or getting worse — especially with breathlessness — see a doctor."))

        if fatigue:
            symptom_info.append(("😴", "Unusual Tiredness", "#d4a84b", "MODERATE",
                "Feeling exhausted doing things that used to be easy — like walking to the shop or climbing stairs — can be a sign your heart is working harder than it should.",
                "Especially important in women, who often experience fatigue as a major heart symptom. Mention it to your doctor."))

        if jaw_pain:
            symptom_info.append(("😬", "Pain Spreading to Jaw, Neck, or Arm", "#e06060", "HIGH",
                "Pain that radiates from the chest to the left arm, jaw, neck, or back is a classic sign of a heart attack — especially combined with other symptoms.",
                "If this is happening right now with chest discomfort: call emergency services immediately."))

        if cold_sweat:
            symptom_info.append(("🥶", "Unexplained Cold Sweats", "#e0804a", "MODERATE-HIGH",
                "Starting to sweat while cold, without working out or having a fever — especially with chest pain — is a major warning sign of a heart attack.",
                "If combined with chest pain or breathlessness: call emergency services. Otherwise, see a doctor soon."))

        if nausea:
            symptom_info.append(("🤢", "Unexplained Nausea", "#d4a84b", "MODERATE",
                "Feeling sick to your stomach isn't usually linked to the heart, but it can be — especially during a heart attack. Women often feel sick instead of having typical chest pain.",
                "If it comes with chest tightness, breathlessness, or sweating — take it seriously and seek emergency help."))

        if sleep_trouble:
            symptom_info.append(("🌙", "Breathless When Lying Down or at Night", "#e0804a", "MODERATE-HIGH",
                "Waking up gasping for air or needing extra pillows to breathe at night can mean fluid is building up in your lungs — a sign that your heart is struggling.",
                "See a doctor soon, especially if this is a new or worsening symptom."))

        if snoring:
            symptom_info.append(("😤", "Loud Snoring / Sleep Apnea", "#d4a84b", "MODERATE",
                "Obstructive sleep apnea (where you stop breathing briefly during sleep) directly strains the heart and raises blood pressure. It's a major, often undiagnosed, cardiovascular risk factor.",
                "Ask your doctor about a sleep study. If diagnosed, treatment (like a CPAP machine) significantly lowers heart risk."))

        if headaches:
            symptom_info.append(("🤕", "Frequent Headaches at the Back of the Head", "#d4a84b", "LOW-MODERATE",
                "Persistent headaches — especially at the back or sides of the head — can be linked to high blood pressure. High BP often has no other symptoms, which is why it's called the 'silent killer'.",
                "Check your blood pressure. If it's consistently above 140/90, see your doctor."))

        if vision_blur:
            symptom_info.append(("👁️", "Blurred Vision or Seeing Spots", "#d4a84b", "MODERATE",
                "High blood pressure can damage the blood vessels in your eyes, causing visual changes. It can also be a sign of a TIA (mini-stroke).",
                "If vision changes are sudden or severe, seek emergency care. Otherwise, get your blood pressure and eyes checked."))

        for icon, title, color, urgency, what_it_means, what_to_do in symptom_info:
            st.markdown(f"""
            <div style="padding:1.4rem; background:rgba(21,26,21,0.8); border:1px solid rgba(255,255,255,0.05); border-left:3px solid {color}; border-radius:8px; margin-bottom:1rem;">
                <div style="display:flex; justify-content:space-between; align-items:flex-start; margin-bottom:0.6rem;">
                    <div style="display:flex; align-items:center; gap:0.6rem;">
                        <span style="font-size:1.2rem;">{icon}</span>
                        <span style="font-size:1rem; font-weight:600; color:#dde8d0;">{title}</span>
                    </div>
                    <div style="font-size:1rem; color:{color}; background:rgba(255,255,255,0.04); border:1px solid {color}30; padding:2px 8px; border-radius:4px; white-space:nowrap; font-weight:600; letter-spacing:0.06em;">{urgency}</div>
                </div>
                <div style="font-size:1.1rem; color:#6a7c5e; line-height:1.6; margin-bottom:0.75rem;"><strong style="color:#dde8d0;">What it might mean:</strong> {what_it_means}</div>
                <div style="font-size:1.1rem; color:#b4d28c; line-height:1.55; background:rgba(180,210,140,0.04); padding:0.6rem 0.75rem; border-radius:6px;"><strong>What to do:</strong> {what_to_do}</div>
            </div>
            """, unsafe_allow_html=True)

        # Overall urgency summary
        high_count = sum(1 for _, _, _, u, _, _ in symptom_info if "HIGH" in u)
        if high_count >= 2:
            urgency_color, urgency_label, urgency_text = "#e06060", "Seek Care Today", "You have multiple high-urgency symptoms. Please contact your doctor today or go to an urgent care clinic."
        elif high_count == 1 or total >= 4:
            urgency_color, urgency_label, urgency_text = "#d4a84b", "See a Doctor Soon", "Your symptoms are worth having checked out. Book an appointment within the next few days."
        else:
            urgency_color, urgency_label, urgency_text = "#6abf82", "Worth Monitoring", "Your symptoms are worth keeping an eye on. Mention them at your next routine checkup."

        st.markdown(f"""
        <div style="margin-top:1.5rem; padding:1.2rem 1.5rem; background:rgba(21,26,21,0.9); border:1px solid {urgency_color}30; border-radius:10px; display:flex; align-items:center; gap:1.2rem;">
            <div style="flex-shrink:0; width:10px; height:10px; background:{urgency_color}; border-radius:50%;"></div>
            <div>
                <div style="font-size:1rem; font-weight:600; color:{urgency_color}; margin-bottom:0.2rem;">{urgency_label}</div>
                <div style="font-size:1.1rem; color:#6a7c5e;">{urgency_text}</div>
            </div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("<hr>", unsafe_allow_html=True)

    # ── SYMPTOMS REFERENCE TABLE ──
    st.markdown("""
    <h3 style="font-family:'DM Serif Display',serif; font-weight:400; color:#dde8d0; font-size:1.4rem; margin:0 0 0.5rem;">Heart Attack Symptoms: Men vs Women</h3>
    <p style="color:#6a7c5e; font-size:1rem; margin-bottom:1.5rem;">Women's heart attacks are often missed because the symptoms are different from what most people expect. Know the difference.</p>
    """, unsafe_allow_html=True)

    col_m, col_w = st.columns(2, gap="large")
    with col_m:
        st.markdown("""
        <div style="padding:1.4rem; background:rgba(56,189,248,0.04); border:1px solid rgba(56,189,248,0.15); border-radius:10px;">
            <h4 style="font-family:'DM Serif Display',serif; color:#38bdf8; font-size:1.1rem; font-weight:400; margin:0 0 1rem;">👨 Typical (Usually Men)</h4>
            <div style="display:flex; flex-direction:column; gap:0.6rem;">
        """, unsafe_allow_html=True)
        for s in ["Crushing chest pain or pressure", "Pain down the left arm", "Shortness of breath", "Sweating", "Nausea"]:
            st.markdown(f'<div style="font-size:1rem; color:#6a7c5e; display:flex; gap:0.6rem;">→ <span>{s}</span></div>', unsafe_allow_html=True)
        st.markdown("</div></div>", unsafe_allow_html=True)

    with col_w:
        st.markdown("""
        <div style="padding:1.4rem; background:rgba(244,114,182,0.04); border:1px solid rgba(244,114,182,0.15); border-radius:10px;">
            <h4 style="font-family:'DM Serif Display',serif; color:#f472b6; font-size:1.1rem; font-weight:400; margin:0 0 1rem;">👩 Often Different in Women</h4>
            <div style="display:flex; flex-direction:column; gap:0.6rem;">
        """, unsafe_allow_html=True)
        for s in ["Unusual or extreme fatigue", "Jaw, neck, or upper back pain", "Nausea or stomach upset", "Shortness of breath (without chest pain)", "Feeling of dread or anxiety"]:
            st.markdown(f'<div style="font-size:1rem; color:#6a7c5e; display:flex; gap:0.6rem;">→ <span>{s}</span></div>', unsafe_allow_html=True)
        st.markdown("</div></div>", unsafe_allow_html=True)

    st.markdown("""
    <div style="margin-top:1rem; padding:1rem; background:rgba(212,168,75,0.05); border:1px solid rgba(212,168,75,0.15); border-radius:8px; font-size:1.1rem; color:#6a7c5e; line-height:1.6;">
        ⚠️ <strong style="color:#dde8d0;">Important:</strong> Women's heart attacks are frequently dismissed or delayed in treatment because symptoms don't match the classic picture. If something feels wrong — even without chest pain — trust your body and seek help.
    </div>
    """, unsafe_allow_html=True)
