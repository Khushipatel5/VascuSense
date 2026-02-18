
import streamlit as st

def show_guidelines():
    st.markdown('<h2 style="margin-bottom: 2rem;">Clinical Protocol</h2>', unsafe_allow_html=True)
    
    st.markdown("""
<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 1.5rem;">
<!-- Card 1 -->
<div class="glass-card" style="border-top: 4px solid #00f2ff;">
<div style="font-size: 2.5rem; margin-bottom: 1rem;">🫀</div>
<h4 style="color: #fff;">Cardiovascular Health</h4>
<p style="color: #94a3b8; font-size: 0.9rem; line-height: 1.6;">
Maintain systolic BP below 120 mmHg. Limit sodium intake to < 1,500mg daily.
</p>
<div style="margin-top: 1rem; background: rgba(0, 242, 255, 0.1); color: #00f2ff; padding: 5px 10px; border-radius: 4px; font-size: 0.8rem; display: inline-block;">Target: < 120/80</div>
</div>

<!-- Card 2 -->
<div class="glass-card" style="border-top: 4px solid #bc13fe;">
<div style="font-size: 2.5rem; margin-bottom: 1rem;">🧬</div>
<h4 style="color: #fff;">Lipid Management</h4>
<p style="color: #94a3b8; font-size: 0.9rem; line-height: 1.6;">
Monitor LDL levels biannually. Increase Omega-3 fatty acids intake through fish or supplements.
</p>
<div style="margin-top: 1rem; background: rgba(188, 19, 254, 0.1); color: #bc13fe; padding: 5px 10px; border-radius: 4px; font-size: 0.8rem; display: inline-block;">Target: LDL < 100</div>
</div>

<!-- Card 3 -->
<div class="glass-card" style="border-top: 4px solid #0aff60;">
<div style="font-size: 2.5rem; margin-bottom: 1rem;">🏃</div>
<h4 style="color: #fff;">Metabolic Activity</h4>
<p style="color: #94a3b8; font-size: 0.9rem; line-height: 1.6;">
150 minutes of moderate-intensity aerobic activity per week. Focus on zone 2 training.
</p>
<div style="margin-top: 1rem; background: rgba(10, 255, 96, 0.1); color: #0aff60; padding: 5px 10px; border-radius: 4px; font-size: 0.8rem; display: inline-block;">Target: 150 min/wk</div>
</div>
</div>
""", unsafe_allow_html=True)
    
    st.markdown("### ⚠️ Emergency Indicators", unsafe_allow_html=True)
    st.markdown("""
<div class="glass-card" style="border-left: 5px solid #ff0a54;">
<div style="display: flex; align-items: center; gap: 20px;">
<div style="font-size: 3rem; color: #ff0a54;">🚨</div>
<div>
<h4 style="color: #ff0a54; margin: 0;">Immediate Action Required</h4>
<p style="color: #cbd5e1; margin-top: 0.5rem; line-height: 1.6;">
If you experience chest pain, shortness of breath, or numbness in the left arm, seek emergency medical attention immediately. 
These algorithms are for screening only and cannot diagnose acute myocardial infarction.
</p>
</div>
</div>
</div>
""", unsafe_allow_html=True)
