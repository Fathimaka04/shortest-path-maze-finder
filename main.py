"""
Shortest Path Finding in a Maze - Streamlit Application
Phase 1: Environment & Project Verification
"""

import sys
import streamlit as st

# Configure browser window tab
st.set_page_config(
    page_title="Shortest Path Finder - Maze Project",
    page_icon="🧩",
    layout="wide"
)

def main():
    st.title("🧩 Shortest Path Finding in a Maze")
    st.caption("A Comparative Analysis of BFS, Dijkstra's, A*, and Bellman-Ford Algorithms")
    
    st.divider()
    
    st.subheader("Phase 1: System Environment Status")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.info(f"**Python Version:** {sys.version.split()[0]}")
        st.success("**Streamlit Status:** Functional & Running")
        
    with col2:
        try:
            import matplotlib
            import pandas
            st.success(f"**Matplotlib Version:** {matplotlib.__version__}")
            st.success(f"**Pandas Version:** {pandas.__version__}")
        except ImportError as e:
            st.error(f"Missing dependency: {e}")

if __name__ == "__main__":
    main()