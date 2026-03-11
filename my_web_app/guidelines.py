import streamlit as st

def show_guidelines():
    st.markdown("""
    <div style="padding: 2.5rem 0 2rem;">
        <div style="font-size:1rem; color:#6a7c5e; letter-spacing:0.18em; text-transform:uppercase; margin-bottom:0.6rem;">Heart Health Tips</div>
        <h1 style="font-family:'DM Serif Display',serif; font-size:2.6rem; font-weight:400; color:#dde8d0; margin:0 0 0.75rem; letter-spacing:-0.01em;">
            Knowledge <em style="color:#b4d28c;">Base</em>
        </h1>
        <p style="color:#6a7c5e; font-size:1.1rem; font-weight:300; max-width:580px; line-height:1.65; margin:0;">
            Easy, simple steps to protect your heart — explained in simple words. No confusing medical talk.
        </p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("<hr>", unsafe_allow_html=True)

    # ── DAILY HABIT TRACKER ──
    st.markdown("""
    <div style="margin-bottom:1.2rem;">
        <div style="font-size:1rem; color:#6a7c5e; letter-spacing:0.15em; text-transform:uppercase; margin-bottom:0.5rem;">Today's Check-In</div>
        <h3 style="font-family:'DM Serif Display',serif; font-weight:400; color:#dde8d0; margin:0 0 0.4rem; font-size:1.5rem;">Daily Heart Health Habits</h3>
        <p style="color:#6a7c5e; font-size:1rem; margin:0 0 1.2rem;">Tick off what you've done today. Small daily habits add up to big protection over time.</p>
    </div>
    """, unsafe_allow_html=True)

    habits = [
        ("🏃", "Moved my body for at least 20–30 minutes today"),
        ("💧", "Drank at least 6–8 glasses of water"),
        ("🥗", "Ate at least 3 portions of vegetables or fruit"),
        ("🧂", "Avoided heavily salted or processed food"),
        ("😴", "Got 7–8 hours of sleep last night"),
        ("🚭", "Didn't smoke today"),
        ("😌", "Took time to relax or de-stress"),
        ("💊", "Took any prescribed medications"),
    ]

    cols = st.columns(2)
    done_count = 0
    habit_boxes = []
    for i, (icon, label) in enumerate(habits):
        with cols[i % 2]:
            val = st.checkbox(f"{icon}  {label}", key=f"habit_{i}")
            habit_boxes.append(val)
            if val: done_count += 1

    score_pct = int((done_count / len(habits)) * 100)
    if score_pct == 100: score_color, score_msg = "#6abf82", "Perfect day! Your heart thanks you. 🎉"
    elif score_pct >= 62: score_color, score_msg = "#b4d28c", "Good effort! A couple more habits and you're there."
    elif score_pct >= 37: score_color, score_msg = "#d4a84b", "Not bad — try to add one more habit tomorrow."
    else:                 score_color, score_msg = "#e06060", "Let's start small — pick just one habit to do today."

    st.markdown(f"""
    <div style="padding:1rem 1.5rem; background:rgba(21,26,21,0.8); border:1px solid rgba(255,255,255,0.05); border-radius:8px; display:flex; align-items:center; gap:1.5rem; margin-top:1rem;">
        <div style="text-align:center; flex-shrink:0;">
            <div style="font-family:'DM Serif Display',serif; font-size:2rem; color:{score_color}; line-height:1;">{done_count}/{len(habits)}</div>
            <div style="font-size:1rem; color:#6a7c5e; text-transform:uppercase; letter-spacing:0.08em;">Today</div>
        </div>
        <div style="flex:1;">
            <div style="background:rgba(255,255,255,0.04); height:6px; border-radius:3px; overflow:hidden; margin-bottom:0.5rem;">
                <div style="background:{score_color}; width:{score_pct}%; height:100%; border-radius:3px; transition:width 0.3s;"></div>
            </div>
            <div style="font-size:1rem; color:{score_color};">{score_msg}</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("<hr>", unsafe_allow_html=True)

    # ── GUIDELINE CARDS ──
    st.markdown("""
    <div style="text-align:center; margin-bottom:2rem;">
        <div style="font-size:1rem; color:#6a7c5e; letter-spacing:0.15em; text-transform:uppercase; margin-bottom:0.5rem;">8 Things That Matter Most</div>
        <h3 style="font-family:'DM Serif Display',serif; font-weight:400; color:#dde8d0; margin:0; font-size:1.8rem;">Your Heart Health Guide</h3>
    </div>
    """, unsafe_allow_html=True)

    guidelines = [
        {
            "icon": "❤️", "color": "#b4d28c",
            "title": "Keep Your Blood Pressure Down",
            "target": "Goal: Under 120/80",
            "simple": "High blood pressure is the biggest cause of heart problems — and most people don't even know they have it because there are no clear signs. The only way to know is to check it.",
            "tips": [
                "Eat less salt — it's hiding in bread, sauces, crisps, and ready meals",
                "Even a 10-minute daily walk helps lower your blood pressure",
                "Stress keeps your BP elevated — find 10 minutes a day to breathe slowly",
                "Limit alcohol — even 2 drinks a day raises BP over time",
                "Check your BP at home or a pharmacy — it only takes 2 minutes",
            ]
        },
        {
            "icon": "🧈", "color": "#d4a84b",
            "title": "Manage Your Cholesterol",
            "target": "Goal: Low 'bad' fat in blood",
            "simple": "Cholesterol is fat in your blood that can build up inside your body's pipes like sludge. Over time, this can block blood and cause a heart attack.",
            "tips": [
                "Swap butter and red meat for olive oil, oily fish, and nuts",
                "Eat more fibre — oats, beans, and lentils actively reduce LDL",
                "Fried food and pastries contain trans fats that raise bad cholesterol",
                "Exercise raises your 'good' cholesterol (HDL) and lowers the bad",
                "Get a blood cholesterol test at least once every 5 years from age 35",
            ]
        },
        {
            "icon": "🚶", "color": "#6abf82",
            "title": "Move Your Body More",
            "target": "Aim for: 30 minutes of movement, most days",
            "simple": "Your heart is a muscle. Like any muscle, it gets stronger when you use it. You don't need a gym — a fast walk, dancing at home, or riding a bike all help.",
            "tips": [
                "3 x 10-minute walks throughout the day is as good as one 30-minute walk",
                "Take the stairs instead of the lift whenever you can",
                "If you sit a lot at work, stand up and move every 30–45 minutes",
                "Find an activity you enjoy — you'll actually stick to it",
                "Even gardening, swimming, or dancing counts as heart-healthy exercise",
            ]
        },
        {
            "icon": "🥗", "color": "#b4d28c",
            "title": "Eat for Your Heart",
            "target": "Focus on: More plants, less processed food",
            "simple": "You don't need to be on a strict diet. Just eat more real food (vegetables, fruit, whole grains, fish) and less junk food (chips, soda, fast food).",
            "tips": [
                "Fill half your plate with vegetables or salad at every meal",
                "Eat oily fish (salmon, mackerel, sardines) 2–3 times a week",
                "Switch white bread and rice for wholegrain versions",
                "Snack on nuts and fruit instead of biscuits and crisps",
                "Limit red meat to 1–2 times a week — choose chicken or fish instead",
            ]
        },
        {
            "icon": "😴", "color": "#d4a84b",
            "title": "Sleep Well",
            "target": "Aim for: 7–9 hours every night",
            "simple": "When you sleep, your blood pressure goes down and your heart rests. Less than 6 hours of sleep a night raises your heart risk by a lot.",
            "tips": [
                "Go to bed and wake up at the same time every day — even weekends",
                "Keep your bedroom cool, dark, and quiet",
                "Avoid phones and screens for 30 minutes before bed",
                "If you snore loudly or wake up tired, ask your doctor about sleep apnea",
                "Avoid heavy meals or alcohol within 2 hours of bedtime",
            ]
        },
        {
            "icon": "🚭", "color": "#6abf82",
            "title": "Quit Smoking",
            "target": "Goal: Being completely smoke-free",
            "simple": "Smoking is very bad for your heart. Every cigarette hurts the pipes that carry blood to your heart. The good news is that quitting works fast. Within 1 day, your heart rate goes down.",
            "tips": [
                "Within 1 year of quitting, your heart disease risk drops by 50%",
                "Nicotine patches or gum double your chances of quitting successfully",
                "Ask your doctor about prescription quit-smoking medication",
                "Avoid the situations where you usually smoke — at first especially",
                "E-cigarettes are not harmless, but far less dangerous than smoking",
            ]
        },
        {
            "icon": "🧘", "color": "#b4d28c",
            "title": "Manage Stress",
            "target": "Goal: Daily relaxation as a habit, not a luxury",
            "simple": "Stress puts your body in 'emergency mode', keeping your blood pressure and heart rate high. Long-term stress is as bad for your heart as bad fats in your blood.",
            "tips": [
                "Try deep breathing: 4 seconds in, hold 4, out for 6 — do this 5 times",
                "Regular walks, especially in nature, are proven to lower stress",
                "Talk to someone you trust — social connection protects the heart",
                "Cut back on news and social media if they make you anxious",
                "If stress is overwhelming, speaking to a therapist is a sign of strength",
            ]
        },
        {
            "icon": "🩸", "color": "#d4a84b",
            "title": "Watch Your Blood Sugar",
            "target": "Aim for: Fasting blood sugar under 100 mg/dL",
            "simple": "High blood sugar hurts your blood pipes slowly over many years. Most people with early diabetes do not know it — but you can fix it by living healthier.",
            "tips": [
                "Cut sugary drinks — one can of fizzy drink has 9 teaspoons of sugar",
                "Eat meals with protein and fibre to avoid blood sugar spikes",
                "Regular exercise makes your body use sugar more efficiently",
                "Get a blood sugar test at least every 3 years from age 40",
                "Losing even 5% of body weight significantly lowers diabetes risk",
            ]
        },
    ]

    g_cols = st.columns(2, gap="large")
    for i, g in enumerate(guidelines):
        with g_cols[i % 2]:
            tips_html = "".join([
                f'<div style="display:flex; gap:0.5rem; font-size:1.1rem; color:#6a7c5e; padding:0.35rem 0; border-bottom:1px solid rgba(255,255,255,0.03); line-height:1.45;"><span style="color:{g["color"]}; flex-shrink:0;">✓</span><span>{t}</span></div>'
                for t in g["tips"]
            ])
            st.markdown(f"""
            <div style="padding:1.4rem; background:rgba(21,26,21,0.7); border:1px solid rgba(255,255,255,0.05); border-left:3px solid {g['color']}; border-radius:8px; margin-bottom:1.2rem;">
                <div style="display:flex; align-items:center; gap:10px; margin-bottom:0.5rem;">
                    <span style="font-size:1.3rem;">{g['icon']}</span>
                    <h4 style="font-family:'DM Serif Display',serif; font-weight:400; color:#dde8d0; margin:0; font-size:1.1rem;">{g['title']}</h4>
                </div>
                <div style="display:inline-block; font-size:1rem; color:{g['color']}; background:rgba(180,210,140,0.05); border:1px solid {g['color']}25; padding:3px 10px; border-radius:4px; margin-bottom:0.85rem; font-weight:500;">{g['target']}</div>
                <p style="color:#94a3a0; font-size:1rem; line-height:1.65; margin:0 0 0.85rem;">{g['simple']}</p>
                <div style="font-size:1rem; color:#6a7c5e; text-transform:uppercase; letter-spacing:0.08em; margin-bottom:0.5rem; font-weight:600;">Practical Tips</div>
                {tips_html}
            </div>
            """, unsafe_allow_html=True)

    st.markdown("<hr>", unsafe_allow_html=True)

    # ── EMERGENCY SECTION ──
    st.markdown("""
    <div style="padding:2rem; background:rgba(224,96,96,0.04); border:1px solid rgba(224,96,96,0.15); border-radius:10px; margin-bottom:2rem;">
        <div style="display:flex; gap:1.5rem;">
            <div style="font-size:2.5rem; flex-shrink:0; line-height:1;">🚨</div>
            <div>
                <h4 style="font-family:'DM Serif Display',serif; font-weight:400; color:#e06060; margin:0 0 0.75rem; font-size:1.3rem;">Heart Attack Warning Signs — Call 999/911 Immediately</h4>
                <p style="color:#6a7c5e; font-size:1rem; line-height:1.75; margin:0;">
                    A heart attack is a life-or-death emergency. <strong style="color:#dde8d0;">Don't wait to see if it gets better. Call for help right away.</strong><br><br>
                    <strong style="color:#dde8d0;">🫀 Chest pain or pressure</strong> — feels like something heavy sitting on your chest, or like squeezing or burning. It might last a few minutes or come and go.<br>
                    <strong style="color:#dde8d0;">💪 Pain spreading</strong> — goes to your left arm, both arms, jaw, neck, back, or stomach.<br>
                    <strong style="color:#dde8d0;">💨 Sudden breathlessness</strong> — can't catch your breath, even without chest pain.<br>
                    <strong style="color:#dde8d0;">😰 Cold sweats, dizziness, or nausea</strong> — starting to sweat while cold, feeling sick in your stomach, or suddenly feeling faint.<br>
                    <strong style="color:#dde8d0;">👩 Women's signs</strong> — women often feel very tired, have jaw/back pain, or feel sick instead of normal chest pain. Take these seriously too.
                    <br><br>
                    <em style="color:#3d4d38; font-size:1.1rem;">Note: VascuSense tells you about your long-term risk. It cannot detect whether you are having a heart attack right now.</em>
                </p>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)
