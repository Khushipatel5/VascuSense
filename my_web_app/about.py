
import streamlit as st

def show_about():
    st.markdown('<div class="app-title">Protocol & Integrity</div>', unsafe_allow_html=True)
    st.markdown('<div class="app-subtitle-premium" style="margin-bottom: 3rem;">Engineered for Precision Health</div>', unsafe_allow_html=True)

    st.markdown('<div class="animate-reveal">', unsafe_allow_html=True)

    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div class="card" style="height: 100%;">
            <h3 style="color:var(--accent);">🔬 Algorithmic Core</h3>
            <p style="color:var(--sub-text); line-height: 1.8;">
                CardioSentinel utilizes a calibrated Logistic Regression model (C=1.0, L2 penalty). 
                Trained on a balanced dataset of 70,000 anonymized health records, it achieves robust 
                generalization across demographic groups.
            </p>
            <div style="background: rgba(0,0,0,0.3); padding: 10px; border-radius: 8px; font-family: monospace; color: #10b981; margin: 15px 0;">
                Accuracy: 73.1% (±0.4%)<br>
                Precision: 0.74<br>
                Recall: 0.71
            </div>
            <p style="color:var(--sub-text); line-height: 1.8;">
                <b>Feature Engineering:</b> BMI calculation, Pulse Pressure derivation, and categorical encoding 
                ensure maximum signal extraction.
            </p>
        </div>
        """, unsafe_allow_html=True)
        
    with col2:
        st.markdown("""
        <div class="card" style="height: 100%;">
            <h3 style="color:var(--accent-vibrant);">🛡️ Data Privacy & Ethics</h3>
            <ul style="color:var(--text-primary); list-style: none; padding: 0; line-height: 2;">
                <li>🔒 <b>Zero-Persistence:</b> Input data is processed in ephemeral memory and discarded immediately.</li>
                <li>👤 <b>Anonymity:</b> No PII (Personally Identifiable Information) is ever requested or stored.</li>
                <li>⚖️ <b>Bias Audited:</b> Regularly tested against gender and age biases to ensure fairness.</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("""
    <div style="margin-top: 5rem; text-align: center;">
        <h4 style="color:var(--sub-text); margin-bottom: 2rem;">Development Team</h4>
        <div style="display: inline-block; background: var(--nav-bg); padding: 20px 40px; border-radius: 50px; border: 1px solid var(--accent);">
            <span style="font-size: 1.5rem; font-weight: 800; background: var(--title-gradient); -webkit-background-clip: text; -webkit-text-fill-color: transparent;">
                Dhruvi Valera
            </span>
            <br>
            <span style="color:var(--accent-vibrant); font-size: 0.9rem; letter-spacing: 0.2em; text-transform: uppercase;">Lead Engineer</span>
        </div>
        <p style="margin-top: 1rem; color: var(--sub-text); font-size: 0.8rem;">
            v2.4.0-stable • Build 2026-02-11
        </p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)
