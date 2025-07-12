import streamlit as st
import os
import pandas as pd
import re
from datetime import datetime

def sanitize_key(name):
    return re.sub(r'\W+', '_', name)

st.set_page_config(page_title="Home", layout="wide")
col1, col2, col3 = st.columns([1, 2, 1]) 

with col2:
    # Title  
 st.markdown("""
    <div style='text-align: center; padding: 10px 0 20px 0;'>
        <h1 style='color:#1f77b4;'>🧪 FORANDROID </h1>
        <h4 style='margin-top: -10px;'>Android Leak Analysis & Forensics Dashboard</h4>
    </div>
 """, unsafe_allow_html=True)

 st.markdown("""
    <style>
        [data-testid="stSidebarNav"]::before {
            content: "🧪 FORANDROID ";
            margin-left: 20px;
            margin-top: 20px;
            font-size: 20px;
            position: relative;
            top: 10px;
            color: #1f77b4;
            display: block;
        }
    </style>
 """, unsafe_allow_html=True)

 st.title("🗂️ Case Management")

 # Tabs-New Case / Load Case
 tab1, tab2 , tab3 , tab4 , tab5 , tab6 = st.tabs(["➕ Create New Case", "📁 Load Existing Case" , "➕ Flag Suspicious IP's" , "🌐 Enrich suspicious IPs" , "🛡️ Port Scan" , "📊 Timeline Generator "])

 #-------------------------------------enter new case-----------------------------
 with tab1:
    st.subheader("Enter Case Details")

    case_name = st.text_input("Case Name")
    investigator = st.text_input("Investigator Name")
    contact = st.text_input("Contact Email")
    date = st.date_input("Investigation Date", value=datetime.today())
    notes = st.text_area("Case Notes (optional)")

    if st.button("Create Case"):
        if not case_name:
            st.warning("Case name is required.")
        else:
            # Create case directory
            base_dir = r"D:\Projects\android-leak-tool\my_android_logs\CASE_FILES_raw_logs"
            case_folder = os.path.join(base_dir, case_name.replace(" ", "_"))
            os.makedirs(case_folder, exist_ok=True)

            # Save metadata
            metadata = {
                "investigator": investigator,
                "contact": contact,
                "date": str(date),
                "notes": notes,
                "created": str(datetime.now())
            }

            with open(os.path.join(case_folder, "metadata.txt"), "w") as f:
                for key, value in metadata.items():
                    f.write(f"{key}: {value}\n")

            st.success(f"✅ Case '{case_name}' created.")
            st.session_state.case_path = case_folder
            st.switch_page("pages/log_input.py") 

 #----------------------------------------------- load existing case -------------------------------------------
 with tab2:
    st.subheader("Select Existing Case")
    base_dir = r"D:\Projects\android-leak-tool\my_android_logs\CASE_FILES_raw_logs"

    if not os.path.exists(base_dir):
        st.info("No case directory found yet.")
    else:
        cases = [d for d in os.listdir(base_dir) if os.path.isdir(os.path.join(base_dir, d))]
        if not cases:
            st.warning("No cases found.")
        else:
            selected = st.selectbox("Select a case", cases , key="select_case_tab2")
            col1 , spacer , col2 , col3 = st.columns([1,2,1,1])
            with col1:
             if st.button("Load Case"):
                st.success(f"Loaded case: {selected}")
                case_path = os.path.join(base_dir, selected)                
                st.session_state.case_path = case_path
                st.switch_page("pages/load_doc.py")
               
            with col2:
                if st.button("Add Data To Existing Case"):
                 st.session_state.case_path = os.path.join(base_dir, selected)
                 st.session_state.trigger_parse = "add_data"

            with col3:
              if st.button("Parse"):
                 st.session_state.case_path = os.path.join(base_dir, selected)
                 st.session_state.trigger_parse = "parse"



            if st.session_state.get("trigger_parse", "") == "add_data":
                st.session_state.trigger_parse = False   
                st.switch_page("pages/log_input.py")

            if st.session_state.get("trigger_parse", "False") == "parse":
                st.session_state.trigger_parse = False
                st.switch_page("pages/parse_logs.py")        

 #--------------------------------tab3 
 with tab3:
     st.subheader("Select Case")
     base_dir = r"D:\Projects\android-leak-tool\my_android_logs\CASE_FILES_raw_logs"

     if not os.path.exists(base_dir):
        st.info("No case directory found yet.")
     else:
        cases2 = [d for d in os.listdir(base_dir) if os.path.isdir(os.path.join(base_dir, d))]
        if not cases2:
            st.warning("No cases found.")
        else:
             selected2 = st.selectbox("Select a case to get the suspicious IPs", cases2 ,key="select_case_tab3")
             if st.button("NEXT : Flag Sus IPs"):
                case_path = os.path.join(base_dir, selected2)
                st.session_state.resolved_case_path = os.path.join(base_dir , selected2)
                st.session_state.trigger_parse = True

             if st.session_state.get("trigger_parse" , False):
                 st.session_state.trigger_parse = False
                 st.switch_page("pages/flag_suspicious_ips.py")

 #-----------------------tab4
 with tab4:
     st.subheader("Select Case To Get Data About Suspicious IPs")
     base_dir = r"D:\Projects\android-leak-tool\my_android_logs\CASE_FILES_raw_logs"       
    
     if not os.path.exists(base_dir):
        st.info("No case directory found yet")
     else:
        cases3 = [d for d in os.listdir(base_dir) if os.path.isdir(os.path.join(base_dir, d))]
        if not cases3:
            st.warning("No cases found.")
        else:
            selected3 = st.selectbox("Select the case for which you want the IPs data" , cases3 , key="select_case_tab4")  
            if st.button(" NEXT: Get Data"):
                case_path = os.path.join(base_dir , selected3)
                st.session_state.resolved_case_path = os.path.join(base_dir , selected3)
                st.session_state.trigger_parse = True

            if st.session_state.get("trigger_parse" , False):
                st.session_state.trigger_parse = False
                st.switch_page("pages/enrich_ips.py")

 #--------------------------tab 5
 with tab5:
      st.subheader("Select Case To Scan PORTS of suspicious ip's")    
      base_dir = r"D:\Projects\android-leak-tool\my_android_logs\CASE_FILES_raw_logs" 

      if not os.path.exists(base_dir):
          st.info("No Case directory found yet")
      else:
          case4 = [d for d in os.listdir(base_dir) if os.path.isdir(os.path.join(base_dir , d))]
          if not case4:
              st.warning("No cases found")
          else:
              sel4 = st.selectbox("select case to scan ports" , case4 , key="select_case_tab5")
              if st.button("NEXT: scan"):
                  case_path=os.path.join(base_dir,sel4)
                  st.session_state.case_path = os.path.join(base_dir, sel4)
                  st.session_state.trigger_parse ="scan"

              if st.session_state.get("trigger_parse", "") == "scan":
                st.session_state.trigger_parse = False   
                st.switch_page("pages/scan_ports.py")
                
#-------------------------tab 6
with tab6:
    st.subheader("Generate Timeline")

    st.markdown("### Select Input Mode:")
    input_mode = st.radio(
        "Choose data source",
        options=["Use existing case folder", "Upload individual log files"],
        key="timeline_input_mode"
    )

    base_dir = r"D:\Projects\android-leak-tool\my_android_logs\CASE_FILES_raw_logs"
    
    # --------------------------------
    # MODE 1: Use Existing Case Folder
    # --------------------------------
    if input_mode == "Use existing case folder":
        if not os.path.exists(base_dir):
            st.info("No Case directory found yet.")
        else:
            case5 = [d for d in os.listdir(base_dir) if os.path.isdir(os.path.join(base_dir, d))]
            if not case5:
                st.warning("⚠️ No cases found.")
            else:
                sel_case = st.selectbox("Select case folder", case5, key="select_tab6")
                if st.button("NEXT: Generate Timeline"):
                    case_path = os.path.join(base_dir, sel_case)
                    st.session_state.case_path = case_path
                    st.session_state.upload_mode = False
                    st.session_state.trigger_parse = "timeline"
                    st.switch_page("pages/timeline_viewer.py")

    # --------------------------------
    # MODE 2: Upload Files
    # --------------------------------
    elif input_mode == "Upload individual log files":
        uploaded_dns = st.file_uploader("Upload resolved_dns_log.csv", type=["csv", "xlsx"], key="dns_tab6")
        uploaded_ips = st.file_uploader("Upload ranked_suspicious_ips.csv", type=["csv", "xlsx"], key="ips_tab6")
        uploaded_logs = st.file_uploader("Upload app_logcat.csv (optional)", type=["csv", "xlsx"], key="log_tab6")

        if st.button("NEXT: Generate Timeline"):
            if uploaded_dns and uploaded_ips:
                st.session_state.upload_mode = True
                st.session_state.uploaded_dns = uploaded_dns
                st.session_state.uploaded_ips = uploaded_ips
                st.session_state.uploaded_logs = uploaded_logs
                st.session_state.trigger_parse = "timeline"
                st.switch_page("pages/timeline_viewer.py")
            else:
                st.error("Please upload at least the DNS and Suspicious IP logs.")



