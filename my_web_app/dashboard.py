import streamlit as st
import pandas as pd
import numpy as np

def show_dashboard():
    col_hero, col_anim = st.columns([1.5, 1])
    with col_hero:
        st.markdown('<div class="hero-title" style="text-align: left;">Future of<br>Cardiac Health.</div>', unsafe_allow_html=True)
        st.markdown("""
<p style="font-size: 1.2rem; color: #94a3b8; line-height: 1.6; max-width: 600px;">
Leverage the power of advanced machine learning on 70,000+ clinical records. 
Instant, secure, and precise cardiovascular risk assessment at your fingertips.
</p>
<br>
""", unsafe_allow_html=True)
        if st.button("INITIATE SCAN"):
            st.session_state.page = "Risk Scanner"
            try:
                st.rerun()
            except AttributeError:
                st.experimental_rerun()

    with col_anim:
        chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["A", "B", "C"])
        st.area_chart(chart_data, height=300, color=["#00f2ff", "#bc13fe", "#0aff60"])

    st.markdown("<br><br><h3 style='text-align: center;'>Core Capabilities</h3><br>", unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown("""
<div class="glass-card">
<div style="font-size: 2rem; margin-bottom: 1rem;">⚡</div>
<h4>Real-Time Inference</h4>
<p style="color: #94a3b8;">Sub-millisecond prediction latency using optimized vector calculations.</p>
</div>
""", unsafe_allow_html=True)
    with col2:
        st.markdown("""
<div class="glass-card">
<div style="font-size: 2rem; margin-bottom: 1rem;">🛡️</div>
<h4>Privacy First</h4>
<p style="color: #94a3b8;">Zero-retention architecture ensures your medical data never leaves this session.</p>
</div>
""", unsafe_allow_html=True)
    with col3:
        st.markdown("""
<div class="glass-card">
<div style="font-size: 2rem; margin-bottom: 1rem;">📈</div>
<h4>73% Precision</h4>
<p style="color: #94a3b8;">Benchmarks validated against 70k validated clinical outcomes.</p>
</div>
""", unsafe_allow_html=True)
