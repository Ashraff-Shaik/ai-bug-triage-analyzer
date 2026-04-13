import streamlit as st
import pandas as pd
from src.triage_system import BugTriageSystem

st.set_page_config(page_title="AI Bug Triage", layout="wide")

st.title("🪲 AI Bug Triage + Root Cause Analyzer")

# Initialize system
@st.cache_resource
def load_triage_system():
    return BugTriageSystem()

system = load_triage_system()

# Input
bug_description = st.text_area(
    "Enter bug description:",
    placeholder="e.g., Login page crashes when user resets password",
    height=120
)

if st.button("🚀 Analyze Bug") and bug_description:
    with st.spinner("Analyzing..."):
        result = system.triage(bug_description)
    
    st.subheader("📊 Analysis Results")
    
    col1, col2 = st.columns(2)
    with col1:
        st.metric("Module", result['module'])
    with col2:
        st.metric("Severity", result['severity'])
    
    st.divider()

    # 🔍 Similar Bugs Section
    st.subheader("🔍 Top Similar Bugs")
    
    for i, bug in enumerate(result['similar_bugs'], 1):
        with st.expander(f"🐞 Bug {bug['bug_id']} - {bug['description'][:80]}..."):
            st.write(f"**Module:** {bug['module']}")
            st.write(f"**Severity:** {bug['severity']}")
            st.write(f"**Root Cause:** {bug['root_cause']}")
            st.write(f"**Suggested Fix:** {bug['suggested_fix']}")
            
            # ⭐ Nice touch: similarity score
            if 'similarity_score' in bug:
                st.progress(min(float(bug['similarity_score']), 1.0))

    st.divider()

    # 💡 Explanation
    st.subheader("💡 Root Cause Explanation")
    st.write(result['explanation'])
    
    # 🔧 Fix
    st.subheader("🔧 Suggested Fix")
    st.success(result['suggested_fix'])