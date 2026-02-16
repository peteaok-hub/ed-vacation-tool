import streamlit as st
import pandas as pd
import altair as alt

# --- PAGE CONFIGURATION (Mobile Optimized) ---
st.set_page_config(
    page_title="Ed Guevara | Vacation Strategies", 
    page_icon="🏛️", 
    layout="centered",
    initial_sidebar_state="expanded" # Force Sidebar Open on Load
)

# --- CSS STYLING ---
st.markdown("""
    <style>
    /* 1. FORCE SIDEBAR ARROW VISIBILITY (Black Button / White Arrow) */
    [data-testid="stSidebarCollapsedControl"] {
        background-color: #000000 !important;
        color: #ffffff !important;
        border: 2px solid #C5A059 !important; /* Gold Border */
        border-radius: 50% !important;
        display: block !important;
    }
    [data-testid="stSidebarCollapsedControl"] svg {
        fill: #ffffff !important;
        stroke: #ffffff !important;
    }
    
    /* 2. HIDE STREAMLIT BRANDING */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
    /* 3. CUSTOM BUTTONS */
    .stButton>button {
        width: 100%;
        border-radius: 20px;
        font-weight: bold;
        height: 3em;
        background-color: #005596; /* Wyndham Blue Accent */
        color: white;
        border: none;
    }
    </style>
    """, unsafe_allow_html=True)

# --- SIDEBAR (Navigation) ---
with st.sidebar:
    st.image("https://placekitten.com/200/200", width=150) # REPLACE WITH YOUR PHOTO
    st.title("Ed Guevara")
    st.info("Real Estate Investor\n20-Year Club Owner")
    
    page = st.radio("Go to:", ["🏠 The Strategy", "📉 Inflation Calculator", "💎 VIP Inventory", "📞 Contact Ed"])
    
    st.warning("⚠️ **Disclaimer:** This is a personal asset management tool. Not an official Wyndham site.")

# --- PAGE 1: THE STRATEGY ---
if page == "🏠 The Strategy":
    st.title("Stop Renting. Start Owning.")
    st.write("Most people treat vacations as an *expense*. I treat them as an *asset*.")
    
    st.markdown("### Why I Built This Tool")
    st.write("""
    I've been a Real Estate Investor for 12 years and an Owner for 20. 
    I built this software to track the **math** behind vacation ownership.
    
    **The 3 Rules of Vacation Wealth:**
    1. Never rent what you can own.
    2. Inflation is guaranteed; hotel prices will double every 10-15 years.
    3. Points are a currency—use them wisely.
    """)
    
    st.success("👉 Go to the **'Inflation Calculator'** tab to see your numbers.")

# --- PAGE 2: CALCULATOR ---
elif page == "📉 Inflation Calculator":
    st.header("📉 The Cost of Doing Nothing")
    st.write("If you don't upgrade today, you are committing to renting hotels for the rest of your life. Let's see the damage.")
    
    # Inputs
    col1, col2 = st.columns(2)
    with col1:
        hotel_spend = st.number_input("Yearly Hotel Spend ($)", value=3000, step=500)
    with col2:
        years = st.slider("Years Remaining", 5, 30, 20)
    
    inflation_rate = 0.04 # 4% Historical Average
    
    # Logic
    data = []
    current_cost = hotel_spend
    cumulative_spend = 0
    
    for i in range(1, years + 1):
        cumulative_spend += current_cost
        data.append({"Year": i, "Total Wasted": cumulative_spend})
        current_cost = current_cost * (1 + inflation_rate)
    
    df = pd.DataFrame(data)
    
    # Visualization (Red Area Chart)
    chart = alt.Chart(df).mark_area(color='#ff4b4b', opacity=0.6).encode(
        x='Year',
        y='Total Wasted',
        tooltip=['Year', 'Total Wasted']
    ).properties(height=300)
    
    st.altair_chart(chart, use_container_width=True)
    
    final_waste = df.iloc[-1]['Total Wasted']
    st.error(f"💀 **Total Wealth Transferred to Hotels:** ${int(final_waste):,}")
    
    st.info("💡 ** Insight:** You are going to spend this money anyway. The only question is: Do you want a stack of receipts, or a deed?")

# --- PAGE 3: INVENTORY ---
elif page == "💎 VIP Inventory":
    st.header("💎 The Asset Class")
    st.write("This is what your maintenance fees buy you vs. what cash buys you.")
    
    tab1, tab2 = st.tabs(["❌ The Renter ($300/nt)", "✅ The Owner ($85/nt)"])
    
    with tab1:
        st.error("Standard Hotel Room")
        st.write("* 325 Sq Ft")
        st.write("* No Kitchen (Eating out 3x/day)")
        st.write("* View of the HVAC unit")
        
    with tab2:
        st.success("Presidential Reserve")
        st.write("* 1,200+ Sq Ft")
        st.write("* Full Gourmet Kitchen")
        st.write("* Jacuzzi Tub & Balcony")
        st.write("* **Deeded Equity**")

# --- PAGE 4: CONTACT ---
elif page == "📞 Contact Ed":
    st.header("Let's Run Your Numbers")
    
    contact_form = """
    <form action="https://formsubmit.co/YOUR_EMAIL_HERE" method="POST">
        <input type="text" name="name" placeholder="Your Name" required style="width: 100%; margin-bottom: 10px; padding: 10px; border-radius: 5px; border: 1px solid #ccc;">
        <input type="email" name="email" placeholder="Your Email" required style="width: 100%; margin-bottom: 10px; padding: 10px; border-radius: 5px; border: 1px solid #ccc;">
        <textarea name="message" placeholder="What is your biggest vacation frustration?" style="width: 100%; margin-bottom: 10px; padding: 10px; border-radius: 5px; border: 1px solid #ccc;"></textarea>
        <button type="submit" style="width: 100%; background-color: #005596; color: white; padding: 10px; border: none; border-radius: 5px; cursor: pointer; font-weight: bold;">SEND TO ED</button>
    </form>
    """
    st.markdown(contact_form, unsafe_allow_html=True)
    
    st.write("---")
    st.write("**Ed Guevara**")
    st.write("📧 ed@edguevara.com")
    st.write("📱 (555) 123-4567")
