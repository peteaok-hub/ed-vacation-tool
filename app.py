import streamlit as st
import pandas as pd
import altair as alt

# --- PAGE CONFIGURATION ---
st.set_page_config(
    page_title="Ed Guevara | Asset Strategy", 
    page_icon="🏛️", 
    layout="centered",
    initial_sidebar_state="expanded" # FORCE OPEN
)

# --- BRANDING: LUXURY BLACK & GOLD THEME ---
st.markdown("""
    <style>
    /* 1. FORCE TEXT COLOR (Global Black Text) */
    html, body, [class*="css"] {
        font-family: 'Helvetica', sans-serif;
        color: #1a1a1a !important; 
    }
    
    /* 2. REMOVE THE SIDEBAR ARROW (Prevent accidental closing) */
    [data-testid="stSidebarCollapsedControl"] {
        display: none !important;
    }
    
    /* 3. ENSURE MOBILE HAMBURGER MENU IS VISIBLE (Black) */
    [data-testid="baseButton-header"] {
        color: #000000 !important;
    }
    
    /* 4. BACKGROUND SETTINGS */
    .stApp {
        background-color: #ffffff;
    }
    
    /* 5. HEADERS */
    h1, h2, h3 {
        color: #000000 !important;
        font-weight: 700 !important;
        text-transform: uppercase;
    }
    
    /* 6. SIDEBAR STYLING */
    section[data-testid="stSidebar"] {
        background-color: #111111; /* Dark Sidebar */
        width: 300px !important; /* Force Width */
    }
    /* Force White Text INSIDE Sidebar only */
    section[data-testid="stSidebar"] * {
        color: #ffffff !important;
    }
    
    /* 7. METRIC CARDS */
    .metric-card {
        background-color: #f8f9fa;
        padding: 25px;
        border-radius: 8px;
        border-left: 6px solid #C5A059;
        box-shadow: 0px 4px 10px rgba(0,0,0,0.05);
        margin-bottom: 20px;
        color: #333333;
    }
    
    /* Hide Default Elements */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    </style>
    """, unsafe_allow_html=True)

# --- SIDEBAR NAV ---
with st.sidebar:
    st.title("ED GUEVARA")
    st.caption("VISION. STRATEGY. EXECUTION.")
    st.markdown("---")
    
    page = st.radio("SELECT MODULE:", ["🏛️ The Philosophy", "📉 Inflation Calculator", "💎 Asset Inventory", "📞 Text Ed"])
    
    st.markdown("---")
    st.info("**Infinite Flow Investments**\n\n*Authorized Asset Strategy Tool*")

# --- PAGE 1: PHILOSOPHY ---
if page == "🏛️ The Philosophy":
    st.title("Vacation Asset Strategy")
    st.write("Real estate is not just about property; it's about potential.")
    
    st.markdown("""
    <div class="metric-card">
    <h3>The Problem: Rental Wealth Transfer</h3>
    Most high-net-worth families unknowingly transfer <b>$100,000+</b> of wealth to hotel corporations over their lifetime, with <b>zero equity</b> retained.
    </div>
    """, unsafe_allow_html=True)
    
    st.write("I built this tool to analyze the **Cost of Inaction**.")
    st.success("👉 Click **Inflation Calculator** on the left to run your audit.")

# --- PAGE 2: CALCULATOR ---
elif page == "📉 Inflation Calculator":
    st.header("📉 Audit: Cost of Inaction")
    st.write("Projecting the 20-year liability of renting vs. owning.")
    
    col1, col2 = st.columns(2)
    with col1:
        hotel_spend = st.number_input("Annual Hotel Spend ($)", value=4000, step=500)
    with col2:
        years = st.slider("Investment Horizon (Years)", 5, 30, 20)
    
    inflation = 0.04 
    years_list = list(range(1, years + 1))
    cumulative_spend = [hotel_spend * ((1 + inflation) ** i) for i in range(years)]
    cumulative_total = [sum(cumulative_spend[:i+1]) for i in range(years)]
    
    df = pd.DataFrame({"Year": years_list, "Total Liability": cumulative_total})
    
    chart = alt.Chart(df).mark_area(color='#1a1a1a', opacity=0.8).encode(
        x='Year', y='Total Liability'
    ).properties(height=320)
    
    st.altair_chart(chart, use_container_width=True)
    st.error(f"Total Wealth Transferred: ${int(cumulative_total[-1]):,}")

# --- PAGE 3: INVENTORY ---
elif page == "💎 Asset Inventory":
    st.header("💎 Asset Class Comparison")
    tab1, tab2 = st.tabs(["❌ The Liability", "✅ The Asset"])
    with tab1:
        st.error("Standard Hotel Room: Zero Equity, No Kitchen.")
    with tab2:
        st.success("Presidential Reserve: Deeded Interest, Full Kitchen.")

# --- PAGE 4: CONTACT ---
elif page == "📞 Text Ed":
    st.header("Execute Strategy")
    st.markdown("""
    <div class="metric-card">
    <b>Ed Guevara</b><br>
    📱 <b>(555) 123-4567</b><br>
    📧 ed@edguevara.com
    </div>
    """, unsafe_allow_html=True)
