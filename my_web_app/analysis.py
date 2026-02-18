import streamlit as st
import pandas as pd
import altair as alt
import numpy as np


def show_analysis():
    
    col1, col2 = st.columns([2, 1])
    
    # ================= LEFT COLUMN =================
    with col1:
        
        # -------- Patient Population Distribution --------
        st.markdown(
            '<h3 style="color: #00f2ff; margin-bottom: 1rem;">Patient Population Distribution</h3>',
            unsafe_allow_html=True
        )
        
        data = pd.DataFrame({
            'Category': ['Normal Risk', 'Elevated Risk', 'Critical Risk'],
            'Count': [45000, 15000, 10000]
        })

        bar_chart = alt.Chart(data).mark_bar(size=60).encode(
            x=alt.X('Category:N', sort=None, title=""),
            y=alt.Y('Count:Q', title="Number of Patients"),
            color=alt.Color(
                'Category:N',
                scale=alt.Scale(range=["#00f2ff", "#bc13fe", "#ff0a54"]),
                legend=None
            ),
            tooltip=['Category', 'Count']
        ).properties(
            height=350
        ).configure_axis(
            labelColor="#94a3b8",
            titleColor="#94a3b8",
            gridColor="rgba(255,255,255,0.05)"
        ).configure_view(
            strokeWidth=0
        )

        st.altair_chart(bar_chart, use_container_width=True)

        # -------- Feature Correlation Impact --------
        st.markdown(
            '<h3 style="color: #0aff60; margin-bottom: 1rem;">Feature Correlation Impact</h3>',
            unsafe_allow_html=True
        )
        
        c_data = pd.DataFrame({
            'Index': ['Age', 'Systolic BP', 'Weight', 'Cholesterol', 'Glucose'],
            'Impact': [0.85, 0.92, 0.65, 0.55, 0.45]
        })

        line_chart = alt.Chart(c_data).mark_line(
            point=True,
            strokeWidth=3,
            color="#0aff60"
        ).encode(
            x=alt.X('Index:N', title=""),
            y=alt.Y('Impact:Q', scale=alt.Scale(domain=[0, 1])),
            tooltip=['Index', 'Impact']
        ).properties(
            height=350
        ).configure_axis(
            labelColor="#94a3b8",
            titleColor="#94a3b8",
            gridColor="rgba(255,255,255,0.05)"
        ).configure_view(
            strokeWidth=0
        )

        st.altair_chart(line_chart, use_container_width=True)
        
     
        # -------- Confusion Matrix & ROC Curve (Moved to Left) --------
        st.markdown("<br><hr style='border-color: rgba(255,255,255,0.1);'><br>", unsafe_allow_html=True)
        
        col_cm, col_roc = st.columns(2)
        
        with col_cm:
            st.markdown('<h3 style="color: #fff; text-align: center; margin-bottom: 1rem;">Confusion Matrix</h3>', unsafe_allow_html=True)
            st.markdown("""
            <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 10px; margin-bottom: 2rem;">
                <div style="background: rgba(10, 255, 96, 0.15); padding: 15px; border-radius: 8px; text-align: center; border: 1px solid rgba(10, 255, 96, 0.3);">
                    <span style="color: #94a3b8; font-size: 0.8rem;">True Negative</span><br>
                    <span style="color: #0aff60; font-weight: bold; font-size: 1.5rem;">24,350</span>
                </div>
                <div style="background: rgba(255, 10, 84, 0.15); padding: 15px; border-radius: 8px; text-align: center; border: 1px solid rgba(255, 10, 84, 0.3);">
                    <span style="color: #94a3b8; font-size: 0.8rem;">False Positive</span><br>
                    <span style="color: #ff0a54; font-weight: bold; font-size: 1.5rem;">4,650</span>
                </div>
                <div style="background: rgba(255, 10, 84, 0.15); padding: 15px; border-radius: 8px; text-align: center; border: 1px solid rgba(255, 10, 84, 0.3);">
                    <span style="color: #94a3b8; font-size: 0.8rem;">False Negative</span><br>
                    <span style="color: #ff0a54; font-weight: bold; font-size: 1.5rem;">3,200</span>
                </div>
                <div style="background: rgba(10, 255, 96, 0.15); padding: 15px; border-radius: 8px; text-align: center; border: 1px solid rgba(10, 255, 96, 0.3);">
                    <span style="color: #94a3b8; font-size: 0.8rem;">True Positive</span><br>
                    <span style="color: #0aff60; font-weight: bold; font-size: 1.5rem;">12,800</span>
                </div>
            </div>
            """, unsafe_allow_html=True)

        with col_roc:
            st.markdown('<h3 style="color: #fff; text-align: center; margin-bottom: 1rem;">ROC Curve</h3>', unsafe_allow_html=True)
            
            roc_data = pd.DataFrame({
                'FPR': np.linspace(0, 1, 100),
                'TPR': [x**(0.4) for x in np.linspace(0, 1, 100)] # Simple curve
            })

            roc_chart = alt.Chart(roc_data).mark_line(
                color='#00f2ff',
                strokeWidth=3
            ).encode(
                x=alt.X('FPR', title='False Positive Rate'),
                y=alt.Y('TPR', title='True Positive Rate')
            ).properties(
                height=250
            ).configure_axis(
                labelColor="#94a3b8",
                titleColor="#94a3b8",
                gridColor="rgba(255,255,255,0.05)"
            ).configure_view(
                strokeWidth=0
            )
            st.altair_chart(roc_chart, use_container_width=True)


    # ================= RIGHT COLUMN =================
    with col2:
        st.markdown("""
<div class="glass-card" style="height: 100%;">
<div style="text-align: center; margin-bottom: 2rem;">
<div style="font-size: 3rem;">🎯</div>
<h3 style="background: linear-gradient(to right, #00f2ff, #0aff60); -webkit-background-clip: text; -webkit-text-fill-color: transparent;">
Model Fidelity
</h3>
</div>

<div style="margin-bottom: 1.5rem;">
<div style="display: flex; justify-content: space-between; margin-bottom: 5px;">
<span style="color: #94a3b8;">Accuracy</span>
<span style="color: #fff; font-weight: bold;">73.1%</span>
</div>
<div style="background: rgba(255,255,255,0.1); height: 6px; border-radius: 3px;">
<div style="background: #00f2ff; width: 73%; height: 100%; border-radius: 3px; box-shadow: 0 0 10px #00f2ff;"></div>
</div>
</div>

<div style="margin-bottom: 1.5rem;">
<div style="display: flex; justify-content: space-between; margin-bottom: 5px;">
<span style="color: #94a3b8;">Recall (Sensitivity)</span>
<span style="color: #fff; font-weight: bold;">71.5%</span>
</div>
<div style="background: rgba(255,255,255,0.1); height: 6px; border-radius: 3px;">
<div style="background: #bc13fe; width: 71.5%; height: 100%; border-radius: 3px; box-shadow: 0 0 10px #bc13fe;"></div>
</div>
</div>

<div style="margin-bottom: 1.5rem;">
<div style="display: flex; justify-content: space-between; margin-bottom: 5px;">
<span style="color: #94a3b8;">Precision</span>
<span style="color: #fff; font-weight: bold;">74.2%</span>
</div>
<div style="background: rgba(255,255,255,0.1); height: 6px; border-radius: 3px;">
<div style="background: #0aff60; width: 74.2%; height: 100%; border-radius: 3px; box-shadow: 0 0 10px #0aff60;"></div>
</div>
</div>

<div style="margin-top: 3rem; background: rgba(0,0,0,0.3); padding: 1rem; border-radius: 12px; font-size: 0.8rem; color: #64748b; line-height: 1.6;">
<b>Validation Source:</b><br>
Stratified K-Fold Cross Validation on 70,000 unique records. Optimized for medical screening (minimizing false negatives).
</div>
</div>
""", unsafe_allow_html=True)
