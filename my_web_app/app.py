import os
import streamlit as st
import joblib

st.set_page_config(
    page_title="VascuSense — Heart Health",
    page_icon="🫀",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=DM+Serif+Display:ital@0;1&family=DM+Sans:opsz,wght@9..40,300;9..40,400;9..40,500;9..40,600&family=DM+Mono:wght@400;500&display=swap');

:root {
    --bg:         #090c09;
    --surface:    #101410;
    --surface-2:  #151a15;
    --surface-3:  #1c231c;
    --border:     rgba(255,255,255,0.055);
    --border-hi:  rgba(180,210,140,0.2);
    --accent:     #b4d28c;
    --accent-dim: rgba(180,210,140,0.1);
    --gold:       #d4a84b;
    --gold-dim:   rgba(212,168,75,0.1);
    --danger:     #e06060;
    --warning:    #d4924a;
    --safe:       #6abf82;
    --text:       #dde8d0;
    --sub:        #6a7c5e;
    --muted:      #2e3d28;
}

*, *::before, *::after { box-sizing: border-box; }
html, body, [class*="css"] {
    font-family: 'DM Sans', sans-serif !important;
    background: var(--bg) !important;
    color: var(--text) !important;
}

section[data-testid="stSidebar"] {
    background: var(--surface) !important;
    border-right: 1px solid var(--border) !important;
}
section[data-testid="stSidebar"] > div { padding: 0 !important; }

section[data-testid="stSidebar"] .stButton > button {
    background: transparent !important;
    border: none !important;
    border-left: 2px solid transparent !important;
    border-radius: 0 !important;
    color: var(--sub) !important;
    font-family: 'DM Sans', sans-serif !important;
    font-size: 1rem !important;
    font-weight: 400 !important;
    letter-spacing: 0.02em !important;
    padding: 0.7rem 1.5rem !important;
    text-align: left !important;
    justify-content: flex-start !important;
    box-shadow: none !important;
    width: 100% !important;
    transition: all 0.15s !important;
}
section[data-testid="stSidebar"] .stButton > button:hover {
    background: var(--accent-dim) !important;
    color: var(--accent) !important;
    border-left: 2px solid var(--muted) !important;
    transform: none !important; box-shadow: none !important;
}
section[data-testid="stSidebar"] .stButton > button:disabled {
    background: var(--accent-dim) !important;
    color: var(--accent) !important;
    border-left: 2px solid var(--accent) !important;
    opacity: 1 !important; font-weight: 500 !important;
    cursor: default !important; box-shadow: none !important;
}

.stButton > button {
    background: var(--accent) !important;
    color: #080c08 !important;
    font-family: 'DM Sans', sans-serif !important;
    font-weight: 600 !important;
    font-size: 1.1rem !important;
    letter-spacing: 0.1em !important;
    text-transform: uppercase !important;
    border-radius: 5px !important;
    padding: 0.65rem 1.6rem !important;
    border: none !important;
    box-shadow: 0 2px 16px rgba(180,210,140,0.2) !important;
    transition: all 0.2s !important;
    width: 100%;
}
.stButton > button:hover {
    background: #c8e8a0 !important;
    transform: translateY(-1px) !important;
    box-shadow: 0 6px 24px rgba(180,210,140,0.3) !important;
}

.stNumberInput input, .stTextInput input {
    background: var(--surface-2) !important;
    border: 1px solid var(--border) !important;
    color: var(--text) !important;
    border-radius: 5px !important;
    font-family: 'DM Sans', sans-serif !important;
    font-size: 1.05rem !important;
}
.stNumberInput input:focus, .stTextInput input:focus {
    border-color: var(--accent) !important;
    box-shadow: 0 0 0 2px rgba(180,210,140,0.08) !important;
}
.stSelectbox > div > div {
    background: var(--surface-2) !important;
    border-color: var(--border) !important;
    color: var(--text) !important;
    border-radius: 5px !important;
}

.stSlider [data-baseweb="slider"] [role="slider"] {
    background: var(--accent) !important;
    border-color: var(--accent) !important;
}

.stInfo { background: var(--accent-dim) !important; border: 1px solid var(--border-hi) !important; border-radius: 6px !important; }
.stSuccess { background: rgba(106,191,130,0.06) !important; border-color: rgba(106,191,130,0.2) !important; }
.stError { background: rgba(224,96,96,0.06) !important; border-color: rgba(224,96,96,0.2) !important; }
.stWarning { background: rgba(212,146,74,0.06) !important; border-color: rgba(212,146,74,0.2) !important; }

[data-testid="metric-container"] {
    background: var(--surface-2) !important;
    border: 1px solid var(--border) !important;
    border-radius: 8px !important;
    padding: 1rem 1.2rem !important;
}
[data-testid="metric-container"] label {
    color: var(--sub) !important; font-size: 1rem !important;
    text-transform: uppercase !important; letter-spacing: 0.1em !important;
}
[data-testid="metric-container"] [data-testid="stMetricValue"] {
    color: var(--text) !important; font-family: 'DM Serif Display', serif !important; font-size: 1.8rem !important;
}

h1, h2, h3, h4 { font-family: 'DM Serif Display', serif !important; color: var(--text) !important; font-weight: 400 !important; }
hr { border-color: var(--border) !important; margin: 2rem 0 !important; }
code { font-family: 'DM Mono', monospace !important; background: var(--surface-2) !important; border: 1px solid var(--border) !important; border-radius: 3px !important; padding: 1px 5px !important; color: var(--accent) !important; font-size: 0.85em !important; }
.stCaption { color: var(--sub) !important; font-size: 1.1rem !important; letter-spacing: 0.04em !important; }

.stTabs [data-baseweb="tab-list"] { background: var(--surface-2) !important; border-radius: 6px !important; padding: 3px !important; border: 1px solid var(--border) !important; }
.stTabs [data-baseweb="tab"] { color: var(--sub) !important; font-family: 'DM Sans', sans-serif !important; background: transparent !important; border-radius: 4px !important; font-size: 1rem !important; }
.stTabs [aria-selected="true"] { background: var(--surface) !important; color: var(--accent) !important; font-weight: 500 !important; }

::-webkit-scrollbar { width: 3px; }
::-webkit-scrollbar-track { background: transparent; }
::-webkit-scrollbar-thumb { background: var(--muted); border-radius: 4px; }
</style>
""", unsafe_allow_html=True)

if "page" not in st.session_state:
    st.session_state.page = "Dashboard"

@st.cache_resource
def load_engine():
    try:
        current_dir = os.path.dirname(os.path.abspath(__file__))
        model = joblib.load(os.path.join(current_dir, "model.pkl"))
        scaler = joblib.load(os.path.join(current_dir, "scaler.pkl"))
        return model, scaler
    except:
        return None, None

model, scaler = load_engine()

with st.sidebar:
    st.markdown("""
    <div style="padding: 2rem 1.5rem 2rem; border-bottom: 1px solid rgba(255,255,255,0.05);">
        <div style="display:flex; align-items:center; gap:10px; margin-bottom:0.4rem;">
            <div style="width:32px; height:32px; background:linear-gradient(135deg,#b4d28c,#d4a84b); border-radius:8px; display:flex; align-items:center; justify-content:center; font-size:1rem; flex-shrink:0;">🫀</div>
            <span style="font-family:'DM Serif Display',serif; font-size:1.35rem; color:#dde8d0; letter-spacing:-0.01em;">VascuSense</span>
        </div>
        <div style="font-size:1rem; color:#6a7c5e; letter-spacing:0.15em; text-transform:uppercase; padding-left:42px;">Heart Health Platform</div>
    </div>
    <div style="height:0.75rem;"></div>
    """, unsafe_allow_html=True)

    def nav_button(label, icon):
        if st.session_state.page == label:
            st.button(f"{icon}   {label}", disabled=True, key=label)
        else:
            if st.button(f"{icon}   {label}", key=label):
                st.session_state.page = label
                st.rerun()

    nav_button("Dashboard",        "◈")
    nav_button("Risk Scanner",     "◎")
    nav_button("Symptom Checker",  "◐")
    nav_button("Analytics Hub",    "◇")
    nav_button("Knowledge Base",   "◉")
    nav_button("About",            "○")

    st.markdown("""
    <div style="margin-top:3rem; padding: 0 1.5rem; font-size:1rem; color:#2e3d28; letter-spacing:0.06em;">
        v2.5.0 · 2026-02-11
    </div>
    """, unsafe_allow_html=True)

page = st.session_state.page

if page == "Dashboard":
    from dashboard import show_dashboard
    show_dashboard()
elif page == "Risk Scanner":
    from risk_scanner import show_risk_scanner
    show_risk_scanner(model, scaler)
elif page == "Symptom Checker":
    from symptom_checker import show_symptom_checker
    show_symptom_checker()
elif page == "Analytics Hub":
    from analysis import show_analysis
    show_analysis()
elif page == "Knowledge Base":
    from guidelines import show_guidelines
    show_guidelines()
elif page == "About":
    from about import show_about
    show_about()
