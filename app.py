import streamlit as st
import base64

st.set_page_config(page_title="TECHLAH PRO - Life Hub Tech", page_icon="🔧", layout="wide")

# --- STYLE - MATCHES YOUR AI STUDIO SCREENSHOT 100% ---
st.markdown("""
<style>
.stApp {background:#F8FAFC;}
.top-bar {background:#FFF8E1; padding:10px 14px; border-radius:10px; font-weight:800; font-size:14px; border:1px solid #FFE082; display:flex; justify-content:space-between; align-items:center;}
.momo-pill {background:#121212; color:#FFD600; padding:7px 14px; border-radius:8px; font-weight:800;}
.bundle-card {background: radial-gradient(circle at top, #1E293B 0%, #0F172A 100%); padding:28px; border-radius:22px; margin:16px 0; border:1px solid #334155;}
.btn-primary {background:#6366F1; color:white; padding:14px; border-radius:12px; width:100%; border:none; font-weight:800; font-size:16px;}
.btn-secondary {background:rgba(255,255,255,0.08); color:white; padding:12px; border-radius:12px; width:100%; border:1px solid rgba(255,255,255,0.2); margin-top:10px;}
.floating {position:fixed; bottom:18px; left:50%; transform:translateX(-50%); background:#111827; color:#FBBF24; padding:12px 28px; border-radius:999px; font-weight:900; z-index:9999; box-shadow:0 10px 30px rgba(0,0,0,0.4);}
.check-card {background:white; border:1px solid #E2E8F0; border-radius:16px; padding:16px;}
</style>
""", unsafe_allow_html=True)

# TOP BAR
st.markdown('<div class="top-bar"><span>📞 Help: 0793098222 / 0784848729</span><span class="momo-pill">📱 Pay MoMo: 0793098222 (put reason)</span><span style="text-decoration:underline; font-weight:600; cursor:pointer;">Payment Details</span></div>', unsafe_allow_html=True)

# HEADER
h1, h2, h3 = st.columns([0.08, 0.62, 0.30])
with h1:
    st.markdown("### 🔧")
with h2:
    st.markdown("## TECHLAH <span style='background:#EEF2FF; color:#6366F1; padding:4px 10px; border-radius:8px; font-size:14px;'>PRO</span> 📞<br><span style='font-size:16px; color:#64748B;'>Life Hub Tech</span>", unsafe_allow_html=True)
with h3:
    c1, c2, c3 = st.columns([1,1,0.5])
    c1.button("USD\n($)", use_container_width=True)
    c2.button("UGX\n(Shs)", use_container_width=True)
    c3.button("🔖")

# TABS
tabs = st.tabs(["$9 Checklists", "Diagnoser", "Coding Club", "Services"])

with tabs[0]:
    # BUNDLE CARD - EXACT FROM SCREENSHOT
    st.markdown("""
    <div class="bundle-card">
        <button class="btn-primary">👁️ Inspect Complete Bundle</button>
        <button class="btn-secondary">View Official Repair Flyer</button>
        <div style="margin-top:18px; color:#FBBF24; font-weight:800;">📞 Call/Pay MoMo: &nbsp; 0793098222</div>
    </div>
    """, unsafe_allow_html=True)

    # OFFICIAL FLYER VIEWER
    with st.expander("📄 View Official Repair Flyer (Click to Open)"):
        st.info("Your official flyer with all 8 machines + MoMo details. Save this image and upload to WhatsApp!")
        # This will show after you upload flyer.png to GitHub
        try:
            st.image("techlah_pro_flyer.webp", caption="TECHLAH PRO Repair Checklists - Pay MoMo 0793098222")
        except:
            st.write("Upload the flyer image I generated to your GitHub as `techlah_pro_flyer.webp` and it will show here.")
            st.write("For now, use the image I sent you in chat as your flyer!")

    st.markdown("<br>", unsafe_allow_html=True)
    search = st.text_input("", placeholder="🔍 Search failure (e.g., 'no power', 'generator won't start')", label_visibility="collapsed")

    col_d1, col_d2 = st.columns([0.2, 0.8])
    with col_d1:
        st.write("Difficulty:")
    with col_d2:
        difficulty = st.selectbox("", ["All Skill Levels", "Beginner", "Intermediate", "Pro"], label_visibility="collapsed")

    ca, cb = st.columns(2)
    with ca:
        show_all = st.button("🛠️ All Machines & Tools", type="primary", use_container_width=True)
    with cb:
        show_ict = st.button("💻 ICT & Computers", use_container_width=True)

    st.caption("Showing 8 failure checklists. Each includes interactive step validation & tools needed.")

    # --- THE 8 CHECKLISTS - ALL ADDED ---
    ALL_CHECKLISTS = [
        {"cat":"All", "title":"Generator - No Power Output", "key":"gen_no_power", "level":"Intermediate", "symptom":"no power generator won't start", "tools":"Multimeter, Spark plug wrench, Oil", "steps":["Unplug all loads & safety OFF","Check oil level - must be to max","Check fuel & air filter - clean if dirty","Remove spark plug - clean & test spark","Check AVR & circuit breaker","Test output with multimeter"]},
        {"cat":"All", "title":"Sewing Machine - Thread Bunching / Breaking", "key":"sew_thread", "level":"Beginner", "symptom":"no power thread jam", "tools":"New needle, Screwdriver, Oil", "steps":["Re-thread top & bobbin correctly","Install new needle size 14/90","Clean bobbin case lint","Adjust top tension to 4","Oil moving parts 1 drop","Test on waste fabric"]},
        {"cat":"All", "title":"Fridge - Not Cooling / Leaking", "key":"fridge_cool", "level":"Intermediate", "symptom":"no cooling fridge", "tools":"Coil brush, Thermometer", "steps":["Clean condenser coils behind","Check door seal with paper test","Set thermostat to 3-4","Check fan is running inside","Defrost 24hrs if iced","If still warm - gas check needed"]},
        {"cat":"ICT", "title":"Laptop - No Power / Slow / Black Screen", "key":"laptop_power", "level":"Beginner", "symptom":"no power laptop black screen", "tools":"RAM, Screwdriver", "steps":["Remove battery & hold power 30s","Reseat RAM - clean gold pins","Clean dust from fan","Check charger voltage 19V","Boot in safe mode","Check HDD health"]},
        {"cat":"All", "title":"Washing Machine - Not Spinning / Draining", "key":"wash_spin", "level":"Intermediate", "symptom":"generator won't spin washing", "tools":"Filter tray, Pliers", "steps":["Clean drain filter bottom front","Check belt behind panel","Check door lock clicks","Balance load evenly","Clean inlet filter","Reset - unplug 5 mins"]},
        {"cat":"ICT", "title":"Printer - Paper Jam & Ink Error", "key":"printer_jam", "level":"Beginner", "symptom":"no power printer paper jam", "tools":"Paper, Ink", "steps":["Pull paper gently - check no torn bits","Clean rollers with damp cloth","Check ink levels - refill","Restart print spooler","Update driver from HP/Canon site","Align print heads"]},
        {"cat":"All", "title":"Motorcycle (Boda) - Won't Start / Overheat", "key":"boda_start", "level":"Pro", "symptom":"no power boda won't start", "tools":"Spark plug, Oil", "steps":["Check spark plug - clean gap","Check fuel flow from tank","Check battery 12.5V+","Clean carburetor","Check oil level","Check valve clearance"]},
        {"cat":"All", "title":"Car - Hard Start / Overheating", "key":"car_start", "level":"Pro", "symptom":"no power car overheating", "tools":"Coolant, Multimeter", "steps":["Check coolant level cold","Check battery terminals tight","Check radiator fan runs","Check oil & coolant mix?","Check thermostat","Check serpentine belt"]},
    ]

    # Filter logic
    filtered = ALL_CHECKLISTS
    if search:
        filtered = [x for x in filtered if search.lower() in x["title"].lower() or search.lower() in x["symptom"].lower()]
    if difficulty!= "All Skill Levels":
        filtered = [x for x in filtered if x["level"] == difficulty]
    if show_ict:
        filtered = [x for x in filtered if x["cat"] == "ICT"]

    # DISPLAY
    for item in filtered:
        with st.container(border=True):
            c1, c2 = st.columns([3,1])
            with c1:
                st.markdown(f"**{item['title']}**")
                st.caption(f"{item['level']} • {item['tools']}")
            with c2:
                st.markdown(f"**$9**\nUGX 35k")

            with st.expander(f"✅ Interactive Checklist - {item['title']}"):
                for idx, step in enumerate(item["steps"]):
                    st.checkbox(f"Step {idx+1}: {step}", key=f"{item['key']}_{idx}")
                st.success("Completed? Take photo of fixed machine for your portfolio!")

            if st.button(f"🔓 Unlock Full PDF - {item['title'][:20]}", key=f"buy_{item['key']}", type="primary", use_container_width=True):
                st.balloons()
                st.markdown(f"""
                **To get full PDF with images:**
                1. MoMo: **0793098222** (Pretty Mumbere)
                2. Reason: **{item['title']}**
                3. Amount: **35,000 Shs**
                4. WhatsApp receipt to **0793098222**
                """)

    st.markdown('<div class="floating">🟠 📞 Help & Pay: 0793098222</div>', unsafe_allow_html=True)

with tabs[1]:
    st.header("🩺 Diagnoser - AI Repair Helper")
    fail = st.text_area("Describe what machine is doing (e.g. 'Generator hums but no output')")
    if st.button("Diagnose", type="primary"):
        st.success(f"For '{fail}', we recommend: Generator No Power checklist + Electrical tools. Go to $9 Checklists tab!")
        st.write("Common causes: Oil low, spark plug, AVR failure.")

with tabs[2]:
    st.header("💻 Coding Club - Life Hub Tech")
    st.write("Join Pretty's classes in Kampala - Learn to build TECHLAH-like apps!")
    st.markdown("- Web Dev (HTML, CSS)\n- Python & AI\n- Repair Tech + Coding")
    if st.button("Join WhatsApp Coding Group"):
        st.info("WhatsApp: 0793098222 - Say 'CODING CLUB'")

with tabs[3]:
    st.header("🔧 Services - Life Hub Tech")
    st.write("On-site repairs in Kampala | Remote support | Templates")
    st.write("📍 Kampala, Uganda | 📞 0793098222 / 0784848729")
