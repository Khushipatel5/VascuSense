import os
import streamlit as st
# import joblib

st.markdown("""
<style>

/* ---------- HERO TITLE ---------- */
.hero-title {
    font-size: 4rem;
    line-height: 1.1;
    margin-bottom: 1rem;
    text-align: left;
    background: linear-gradient(to right, #00f2ff, #bc13fe);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    text-shadow: 0 0 40px rgba(188, 19, 254, 0.3);
}


/* ---------- GLASS CARD ---------- */
.glass-card {
    background: rgba(17, 25, 40, 0.75);
    backdrop-filter: blur(16px) saturate(180%);
    border: 1px solid rgba(255, 255, 255, 0.125);
    border-radius: 16px;
    padding: 2rem;
    margin-bottom: 1.5rem;
    box-shadow: 0 8px 32px rgba(0, 0, 0, 0.37);
    transition: 0.3s;
}

.glass-card:hover {
    transform: translateY(-5px);
    box-shadow: 0 12px 40px rgba(0, 242, 255, 0.1);
}


/* ---------- INPUT BOXES ---------- */
.stTextInput input,
.stNumberInput input,
.stSelectbox div[data-baseweb="select"] {

    background: rgba(255,255,255,0.05) !important;
    border: 1px solid rgba(255,255,255,0.125) !important;
    color: white !important;
    border-radius: 8px !important;
    transition: 0.3s;
}

.stTextInput input:focus,
.stNumberInput input:focus,
.stSelectbox div[data-baseweb="select"]:focus-within {

    background: rgba(255,255,255,0.1) !important;
    border-color: #00f2ff !important;
    box-shadow: 0 0 12px rgba(0,242,255,0.3);
}


/* ---------- BUTTON ---------- */
.stButton > button {

    background: linear-gradient(90deg,#bc13fe,#00f2ff) !important;
    color: black !important;
    font-weight: 800 !important;
    border-radius: 50px !important;
    padding: 0.6rem 2rem !important;
    text-transform: uppercase;
    letter-spacing: 0.1em;
    transition: 0.3s;
    box-shadow: 0 0 20px rgba(0,242,255,0.4);
}

.stButton > button:hover {
    transform: scale(1.05);
    box-shadow: 0 0 40px rgba(0,242,255,0.6);
    color: white !important;
}


/* ---------- RESULT BOX ---------- */
.result-high {
    border-color: #ff0a54 !important;
    box-shadow: 0 0 40px rgba(255,10,84,0.4);
}

.result-safe {
    border-color: #0aff60 !important;
    box-shadow: 0 0 40px rgba(10,255,96,0.4);
}

</style>
""", unsafe_allow_html=True)

# ---------------- CONFIGURATION ---------------- #
st.set_page_config(
    page_title="VascuSense",
    page_icon="🧬",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ---------------- SESSION STATE INIT ---------------- #
if "page" not in st.session_state:
    st.session_state.page = "Dashboard"

# ---------------- VISUAL IDENTITY ---------------- #
st.markdown("""<style>
    /* Global Button Width Fix */
    .stButton > button {
        width: 100%;
    }

    /* ---------------- SIDEBAR NAVIGATION STYLES ---------------- */
    
    /* Inactive Sidebar Buttons */
    section[data-testid="stSidebar"] .stButton > button {
        background: rgba(255, 255, 255, 0.02) !important;
        border: 1px solid rgba(255, 255, 255, 0.05) !important;
        color: #94a3b8 !important; /* Muted text */
        font-weight: 500 !important;
        text-transform: none !important; /* Normal case for nicer reading */
        letter-spacing: 0.05em !important;
        padding: 0.75rem 1.5rem !important;
        border-radius: 12px !important;
        text-align: left !important;
        justify-content: flex-start !important; /* Align text left */
        box-shadow: none !important;
        transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1) !important;
    }

    /* Hover State for Sidebar Buttons */
    section[data-testid="stSidebar"] .stButton > button:hover {
        background: rgba(255, 255, 255, 0.08) !important;
        border-color: rgba(0, 242, 255, 0.5) !important;
        color: white !important;
        transform: translateX(6px) !important; /* Slide effect */
        box-shadow: -4px 0 15px rgba(0, 242, 255, 0.1) !important;
    }

    /* Active State (Disabled Button in Sidebar) */
    section[data-testid="stSidebar"] .stButton > button:disabled {
        background: linear-gradient(90deg, rgba(0, 242, 255, 0.15) 0%, transparent 100%) !important;
        border: 1px solid #00f2ff !important;
        color: #00f2ff !important;
        opacity: 1 !important; /* Prevent default disabled fade */
        font-weight: 700 !important;
        box-shadow: 0 4px 20px rgba(0, 0, 0, 0.2) !important;
        transform: none !important;
        cursor: default !important;
    }
    
    /* Focused State (Tapped) */
    section[data-testid="stSidebar"] .stButton > button:focus {
        background: rgba(0, 242, 255, 0.1) !important;
        border-color: #00f2ff !important;
        color: #00f2ff !important;
        box-shadow: 0 0 15px rgba(0, 242, 255, 0.3) !important;
    }

    /* Active State (Pressed) */
    section[data-testid="stSidebar"] .stButton > button:active {
        background: rgba(0, 242, 255, 0.2) !important;
        border-color: #00f2ff !important;
        color: white !important;
        transform: scale(0.98) translateX(6px) !important;
    }

</style>""", unsafe_allow_html=True)

# ---------------- DATA / MODEL ---------------- #
@st.cache_resource
def load_engine():
    try:
        current_dir = os.path.dirname(os.path.abspath(__file__))
        model_path = os.path.join(current_dir, "model.pkl")
        scaler_path = os.path.join(current_dir, "scaler.pkl")
        
        model = joblib.load(model_path)
        scaler = joblib.load(scaler_path)
        return model, scaler
    except:
        return None, None

model, scaler = load_engine()

# ---------------- SIDEBAR NAV ---------------- #
with st.sidebar:

    st.markdown("## 🧬 VascuSense")

    def nav_button(label):
        if st.session_state.page == label:
            st.button(label, disabled=True, key=label)
        else:
            if st.button(label, key=label):
                st.session_state.page = label
                st.rerun()

    nav_button("Dashboard")
    nav_button("Risk Scanner")
    nav_button("Analytics Hub")
    nav_button("Knowledge Base")

page = st.session_state.page

# ---------------- DASHBOARD ---------------- #
if page == "Dashboard":
    from dashboard import show_dashboard
    show_dashboard()
    
# ---------------- RISK SCANNER ---------------- #

elif page == "Risk Scanner":
    from risk_scanner import show_risk_scanner
    show_risk_scanner(model, scaler)

# ---------------- ANALYTICS ---------------- #
elif page == "Analytics Hub":
    from analysis import show_analysis
    show_analysis()

# ---------------- KNOWLEDGE ---------------- #
elif page == "Knowledge Base":
    from guidelines import show_guidelines
    show_guidelines()
