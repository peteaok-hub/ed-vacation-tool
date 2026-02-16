import streamlit as st
import pandas as pd
import altair as alt

# --- PAGE CONFIGURATION ---
st.set_page_config(
    page_title="Ed Guevara | Asset Strategy", 
    page_icon="🏛️", 
    layout="centered"
)

# --- BRANDING: MATCHING EDGUEVARA.COM ---
st.markdown("""
    <style>
    /* Hide Default Streamlit Elements */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
    /* BLACK & GOLD THEME OVERRIDES */
    .stApp {
        background-color: #ffffff; /* Clean White Background for contrast */
    }
    
    /* Custom Button Style */
    .stButton>button {
        width: 100%;
        border-radius: 5px;
        height: 3.5em;
        font-weight: bold;
        font-size: 18px;
        background-color: #000000; /* Infinite Flow Black */
        color: #C5A059; /* Approximate Gold from your site */
        border: 2px solid #C5A059;
    }
    .stButton>button:hover {
        background-color: #C5A059;
        color: black;
        border: 2px solid black;
    }

    /* Cards */
    .metric-card {
        background-color: #f8f9fa;
        padding: 20px;
        border-radius: 8px;
        border-left: 5px solid #C5A059;
        box-shadow: 2px 2px 10px rgba(0,0,0,0.1);
        margin-bottom: 20px;
    }
    
    h1, h2, h3 {
        font-family: 'Helvetica', sans-serif;
        color: #1a1a1a;
    }
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
    st.title("VACATION ASSET STRATEGY")
    st.write("Real estate is not just about property; it's about potential.")
    
    st.markdown("""
    <div class="metric-card">
    <h3>The Problem: Rental Wealth Transfer</h3>
    Most high-net-worth families unknowingly transfer <b>$100,000+</b> of wealth to hotel corporations (Marriott, Hilton) over their lifetime, with <b>zero equity</b> retained.
    </div>
    """, unsafe_allow_html=True)
    
    st.write("I built this tool to analyze the **Cost of Inaction**.")
    st.success("👉 Navigate to the **Inflation Calculator** to run your audit.")

# --- PAGE 2: CALCULATOR ---
elif page == "📉 Inflation Calculator":
    st.header("📉 AUDIT: COST OF INACTION")
    st.write("Projecting the 20-year liability of renting vs. owning.")
    
    # Inputs
    col1, col2 = st.columns(2)
    with col1:
        hotel_spend = st.number_input("Annual Hotel Spend ($)", value=4000, step=500)
    with col2:
        years = st.slider("Investment Horizon (Years)", 5, 30, 20)
    
    inflation = 0.04 # 4% Hotel Inflation Rate
    
    # Fast Calculation
    years_list = list(range(1, years + 1))
    cumulative_spend = []
    current_cost = hotel_spend
    running_total = 0
    
    for _ in years_list:
        running_total += current_cost
        cumulative_spend.append(running_total)
        current_cost = current_cost * (1 + inflation)
    
    df = pd.DataFrame({"Year": years_list, "Total Liability": cumulative_spend})
    
    # Chart
    chart = alt.Chart(df).mark_area(
        color='#1a1a1a', # Black
        opacity=0.8
    ).encode(
        x='Year',
        y='Total Liability',
        tooltip=['Year', 'Total Liability']
    ).properties(height=320)
    
    st.altair_chart(chart, use_container_width=True)
    
    final_loss = cumulative_spend[-1]
    
    st.markdown(f"""
    <div class="metric-card" style="border-left: 5px solid red;">
    <h3>Total Wealth Transferred: ${int(final_loss):,}</h3>
    This is capital leaving your family portfolio forever.
    </div>
    """, unsafe_allow_html=True)

# --- PAGE 3: INVENTORY ---
elif page == "💎 Asset Inventory":
    st.header("💎 ASSET CLASS COMPARISON")
    
    tab1, tab2 = st.tabs(["❌ The Liability (Rent)", "✅ The Asset (Own)"])
    
    with tab1:
        st.error("Standard Hotel Room")
        st.write("• **Zero Equity**")
        st.write("• 325 Sq Ft")
        st.write("• No Kitchen")
        st.caption("Avg Cost: $350/night (and rising)")
        
    with tab2:
        st.success("Presidential Reserve")
        st.write("• **Deeded Real Estate Interest**")
        st.write("• 1,200+ Sq Ft")
        st.write("• Full Gourmet Kitchen")
        st.caption("Maintenance Cost: ~$85/night (Fixed)")

# --- PAGE 4: CONTACT ---
elif page == "📞 Text Ed":
    st.header("EXECUTE STRATEGY")
    st.write("Text me the number from your Audit.")
    
    st.markdown("""
    <div class="metric-card">
    <b>Ed Guevara</b><br>
    <i>Infinite Flow Investments</i><br>
    <br>
    📱 <b>(555) 123-4567</b><br>
    📧 ed@edguevara.com
    </div>
    """, unsafe_allow_html=True)