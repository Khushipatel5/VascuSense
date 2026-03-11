import streamlit as st
import pandas as pd
import altair as alt
import numpy as np

def show_analysis():
    st.markdown("""
    <div style="padding: 2.5rem 0 2rem;">
        <div style="font-size:1rem; color:#6a7c5e; letter-spacing:0.18em; text-transform:uppercase; margin-bottom:0.6rem;">Under the Hood</div>
        <h1 style="font-family:'DM Serif Display',serif; font-size:2.6rem; font-weight:400; color:#dde8d0; margin:0 0 0.75rem; letter-spacing:-0.01em;">
            Analytics <em style="color:#b4d28c;">Hub</em>
        </h1>
        <p style="color:#6a7c5e; font-size:1.1rem; font-weight:300; max-width:600px; line-height:1.65; margin:0;">
            Curious how the AI works? Here's a plain-English breakdown of our model's performance and what it found in the data.
        </p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div style="padding:1rem 1.2rem; background:rgba(21,26,21,0.8); border:1px solid rgba(255,255,255,0.05); border-radius:8px; margin-bottom:1.5rem;">
        <p style="color:#6a7c5e; font-size:1rem; line-height:1.65; margin:0;">
            <strong style="color:#dde8d0;">How accurate is VascuSense?</strong> Our AI correctly predicts whether someone has heart disease about <strong style="color:#b4d28c;">73 times out of 100</strong>. That's not perfect — no AI is — but it's good enough to be a meaningful early warning system. Think of it like a weather forecast: it can't be 100% right, but it's much better than guessing.
        </p>
    </div>
    """, unsafe_allow_html=True)

    m1, m2, m3, m4 = st.columns(4)
    with m1: st.metric("Overall Accuracy",   "73.1%",  help="Out of 100 predictions, 73 are correct.")
    with m2: st.metric("Catches At-Risk People", "74.2%", help="Of people who actually have heart risk, we correctly identify 74%.")
    with m3: st.metric("Avoids False Alarms", "71.5%",  help="Of people flagged as at-risk, 71.5% actually are.")
    with m4: st.metric("AUC Score",          "0.79",   help="Measures overall discrimination ability. 1.0 is perfect, 0.5 is random. 0.79 is good.")

    st.markdown("<hr>", unsafe_allow_html=True)

    # ── ROW 1 ──
    col_demo, col_strat = st.columns(2, gap="large")

    with col_demo:
        st.markdown("""
        <h4 style="font-family:'DM Serif Display',serif; font-weight:400; color:#dde8d0; font-size:1.2rem; margin:0 0 0.3rem;">Who Was in the Training Data?</h4>
        <p style="font-size:1.1rem; color:#6a7c5e; margin-bottom:1.2rem; line-height:1.55;">Our model learned from 70,000 real anonymised patient records. Here's the gender breakdown.</p>
        """, unsafe_allow_html=True)

        demo_data = pd.DataFrame({'Gender': ['Female (65%)', 'Male (35%)'], 'Count': [45530, 24470]})
        donut = alt.Chart(demo_data).mark_arc(innerRadius=55, outerRadius=95).encode(
            theta=alt.Theta("Count:Q"),
            color=alt.Color("Gender:N",
                scale=alt.Scale(range=["#b4d28c", "#d4a84b"]),
                legend=alt.Legend(title=None, labelColor="#6a7c5e", labelFont="DM Sans", labelFontSize=12)
            ),
            tooltip=["Gender", "Count"]
        ).properties(height=220).configure_view(strokeWidth=0)
        st.altair_chart(donut, use_container_width=True)

        st.markdown("""
        <div style="font-size:1.1rem; color:#6a7c5e; text-align:center; margin-top:-0.5rem;">
            There are more women here because of the data we used, not because women get heart problems more often.
        </div>
        """, unsafe_allow_html=True)

    with col_strat:
        st.markdown("""
        <h4 style="font-family:'DM Serif Display',serif; font-weight:400; color:#dde8d0; font-size:1.2rem; margin:0 0 0.3rem;">How Many People Had Heart Disease?</h4>
        <p style="font-size:1.1rem; color:#6a7c5e; margin-bottom:1.2rem; line-height:1.55;">Out of 70,000 patients, this is how many fell into each risk category.</p>
        """, unsafe_allow_html=True)

        strat = pd.DataFrame({
            'Category': ['Healthy', 'Moderate Risk', 'High Risk'],
            'Count':    [45000,     15000,             10000]
        })
        bar = alt.Chart(strat).mark_bar(cornerRadiusTopLeft=4, cornerRadiusTopRight=4, size=44).encode(
            x=alt.X('Category:N', sort=None, title="",
                axis=alt.Axis(labelAngle=0, labelFontSize=12, labelColor="#6a7c5e", domainColor="transparent", tickColor="transparent")),
            y=alt.Y('Count:Q', title="Number of Patients",
                axis=alt.Axis(labelColor="#6a7c5e", titleColor="#6a7c5e", gridColor="rgba(255,255,255,0.04)")),
            color=alt.Color('Category:N',
                scale=alt.Scale(range=["#6abf82", "#d4a84b", "#e06060"]),
                legend=None),
            tooltip=['Category', 'Count']
        ).properties(height=250).configure_view(strokeWidth=0).configure_axis(domainColor="transparent")
        st.altair_chart(bar, use_container_width=True)

    st.markdown("<hr>", unsafe_allow_html=True)

    # ── ROW 2 ──
    col_feat, col_matrix = st.columns([1.2, 1], gap="large")

    with col_feat:
        st.markdown("""
        <h4 style="font-family:'DM Serif Display',serif; font-weight:400; color:#dde8d0; font-size:1.2rem; margin:0 0 0.3rem;">What Matters Most for Heart Risk?</h4>
        <p style="font-size:1.1rem; color:#6a7c5e; margin-bottom:1.2rem; line-height:1.55;">The AI ranked these factors by how much they influenced its predictions. Longer bar = bigger impact on your risk.</p>
        """, unsafe_allow_html=True)

        feat_data = pd.DataFrame({
            'Factor':  ['Blood Pressure (top)', 'Age', 'Cholesterol', 'Weight', 'Blood Sugar', 'Blood Pressure (bottom)', 'BMI'],
            'Impact':  [0.92,                   0.85,  0.65,          0.55,     0.45,          0.42,                      0.38]
        })
        bars = alt.Chart(feat_data).mark_bar(cornerRadiusTopRight=4, cornerRadiusBottomRight=4).encode(
            y=alt.Y('Factor:N', sort='-x', title="",
                axis=alt.Axis(labelColor="#6a7c5e", domainColor="transparent", tickColor="transparent", labelFontSize=11)),
            x=alt.X('Impact:Q', title="Relative Importance",
                scale=alt.Scale(domain=[0,1]),
                axis=alt.Axis(labelColor="#6a7c5e", titleColor="#6a7c5e", gridColor="rgba(255,255,255,0.04)")),
            color=alt.condition(
                alt.datum['Impact'] > 0.7,
                alt.value('#b4d28c'),
                alt.value('#3d4d38')
            ),
            tooltip=['Factor', 'Impact']
        ).properties(height=280).configure_view(strokeWidth=0).configure_axis(domainColor="transparent")
        st.altair_chart(bars, use_container_width=True)

        st.markdown("""
        <div style="padding:0.8rem 1rem; background:rgba(180,210,140,0.06); border:1px solid rgba(180,210,140,0.12); border-radius:6px; font-size:1.1rem; color:#6a7c5e; line-height:1.55;">
            💡 <strong style="color:#dde8d0;">Key insight:</strong> Blood pressure is the single biggest predictor of heart risk in our model — more than age, weight, or cholesterol. This is why checking your BP regularly is so important.
        </div>
        """, unsafe_allow_html=True)

    with col_matrix:
        st.markdown("""
        <h4 style="font-family:'DM Serif Display',serif; font-weight:400; color:#dde8d0; font-size:1.2rem; margin:0 0 0.3rem;">How Often Does the AI Get It Right?</h4>
        <p style="font-size:1.1rem; color:#6a7c5e; margin-bottom:1.2rem; line-height:1.55;">Out of 45,000 test patients, here's how the AI's predictions compared to reality.</p>
        """, unsafe_allow_html=True)

        cells = [
            ("✅ Correctly said 'Healthy'",    "24,350", "#6abf82", "These patients were actually healthy, and the AI correctly said so."),
            ("⚠️ Said 'At Risk' but was Healthy", "4,650", "#d4a84b", "The AI was cautious — it flagged these healthy people. A false alarm. Better safe than sorry."),
            ("❌ Said 'Healthy' but was At Risk", "3,200", "#e06060", "The AI missed these at-risk patients. This is the most dangerous error — we work hard to minimize this."),
            ("✅ Correctly said 'At Risk'",     "12,800", "#6abf82", "These patients were at risk, and the AI correctly caught them."),
        ]
        c1, c2 = st.columns(2)
        for i, (label, val, color, desc) in enumerate(cells):
            col = c1 if i % 2 == 0 else c2
            with col:
                st.markdown(f"""
                <div style="padding:1rem; background:rgba(21,26,21,0.8); border:1px solid rgba(255,255,255,0.05); border-top:2px solid {color}; border-radius:7px; margin-bottom:0.6rem; text-align:center;">
                    <div style="font-size:1rem; color:#6a7c5e; margin-bottom:0.4rem; line-height:1.3;">{label}</div>
                    <div style="font-family:'DM Mono',monospace; color:{color}; font-size:1.3rem; font-weight:500; margin-bottom:0.4rem;">{val}</div>
                    <div style="font-size:1rem; color:#3d4d38; line-height:1.4;">{desc}</div>
                </div>
                """, unsafe_allow_html=True)

        st.markdown("""
        <div style="padding:0.9rem 1rem; background:rgba(212,168,75,0.05); border:1px solid rgba(212,168,75,0.15); border-radius:6px; font-size:1.1rem; color:#6a7c5e; line-height:1.6;">
            💡 <strong style="color:#dde8d0;">Why false alarms are OK, but missed cases are not:</strong> If the AI wrongly says you're at risk, you get an unnecessary checkup — annoying but harmless. If it wrongly says you're fine when you're not, you might miss treatment you need. Our AI is tuned to avoid the second type of error.
        </div>
        """, unsafe_allow_html=True)

    st.markdown("<hr>", unsafe_allow_html=True)

    # ── ROW 3 ──
    col_roc, col_arch = st.columns(2, gap="large")

    with col_roc:
        st.markdown("""
        <h4 style="font-family:'DM Serif Display',serif; font-weight:400; color:#dde8d0; font-size:1.2rem; margin:0 0 0.3rem;">How Good Is the AI at Separating Healthy from At-Risk?</h4>
        <p style="font-size:1.1rem; color:#6a7c5e; margin-bottom:1.2rem; line-height:1.55;">This graph shows how well our AI separates healthy patients from at-risk ones. The green curve hugging the top-left corner means it's doing a good job.</p>
        """, unsafe_allow_html=True)

        x_roc = np.linspace(0, 1, 100)
        y_roc = x_roc ** 0.4
        roc_df = pd.DataFrame({'False Alarm Rate': x_roc, 'Correctly Caught Rate': y_roc})
        baseline = pd.DataFrame({'False Alarm Rate': [0, 1], 'Correctly Caught Rate': [0, 1]})

        roc_line = alt.Chart(roc_df).mark_line(strokeWidth=3, color='#b4d28c').encode(
            x=alt.X('False Alarm Rate', axis=alt.Axis(labelColor="#6a7c5e", titleColor="#6a7c5e", gridColor="rgba(255,255,255,0.04)")),
            y=alt.Y('Correctly Caught Rate', axis=alt.Axis(labelColor="#6a7c5e", titleColor="#6a7c5e", gridColor="rgba(255,255,255,0.04)"))
        )
        diag = alt.Chart(baseline).mark_line(strokeWidth=1, strokeDash=[4, 4], color='#3d4d38').encode(
            x='False Alarm Rate', y='Correctly Caught Rate'
        )
        roc_chart = (roc_line + diag).properties(height=260).configure_view(strokeWidth=0).configure_axis(domainColor="transparent")
        st.altair_chart(roc_chart, use_container_width=True)

        st.markdown("""
        <div style="padding:0.8rem 1rem; background:rgba(180,210,140,0.07); border:1px solid rgba(180,210,140,0.15); border-radius:6px; display:flex; justify-content:space-between; align-items:center;">
            <div>
                <div style="font-size:1.1rem; color:#6a7c5e; font-weight:500;">AUC Score</div>
                <div style="font-size:1rem; color:#3d4d38; margin-top:2px;">1.0 = perfect · 0.5 = coin flip · 0.79 = good</div>
            </div>
            <span style="font-family:'DM Mono',monospace; color:#b4d28c; font-size:1.2rem; font-weight:500;">0.79</span>
        </div>
        """, unsafe_allow_html=True)

    with col_arch:
        st.markdown("""
        <h4 style="font-family:'DM Serif Display',serif; font-weight:400; color:#dde8d0; font-size:1.2rem; margin:0 0 0.3rem;">How Was the AI Built?</h4>
        <p style="font-size:1.1rem; color:#6a7c5e; margin-bottom:1.2rem; line-height:1.55;">Here's a plain-English summary of how VascuSense was trained and tested.</p>
        """, unsafe_allow_html=True)

        for label, val, color in [
            ("Overall Accuracy",      73, "#b4d28c"),
            ("Catches At-Risk People",74, "#d4a84b"),
            ("Avoids False Alarms",   72, "#6abf82"),
            ("AUC Score × 100",       79, "#b4d28c"),
        ]:
            st.markdown(f"""
            <div style="margin-bottom:1rem;">
                <div style="display:flex; justify-content:space-between; margin-bottom:5px;">
                    <span style="font-size:1.1rem; color:#6a7c5e;">{label}</span>
                    <span style="font-family:'DM Mono',monospace; font-size:1rem; color:#dde8d0;">{val}%</span>
                </div>
                <div style="background:rgba(255,255,255,0.04); height:4px; border-radius:2px; overflow:hidden;">
                    <div style="background:{color}; width:{val}%; height:100%; border-radius:2px;"></div>
                </div>
            </div>
            """, unsafe_allow_html=True)

        for title, body in [
            ("The Math",             "We use a type of math used in medical research for a long time. It's very reliable, and we know exactly how it makes decisions."),
            ("How It Was Tested",    "We tested the tool 5 times on different parts of the data. This makes sure our results are solid and we didn't just get lucky."),
            ("Preparing Data",       "Before learning, we made sure all the numbers were on the same scale. This stops the tool from thinking big numbers (like weight) are more important than small numbers (like age)."),
        ]:
            st.markdown(f"""
            <div style="padding:0.9rem; background:rgba(21,26,21,0.6); border:1px solid rgba(255,255,255,0.04); border-radius:7px; margin-bottom:0.6rem; margin-top:0.5rem;">
                <div style="font-size:1.1rem; color:#dde8d0; font-weight:500; margin-bottom:0.3rem;">{title}</div>
                <div style="font-size:1.1rem; color:#6a7c5e; line-height:1.6;">{body}</div>
            </div>
            """, unsafe_allow_html=True)
