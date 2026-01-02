# Streamlit Dashboard for GDERIS
import streamlit as st

def main():
    st.title("Global Development & Economic Risk Intelligence System")
    st.sidebar.header("Navigation")
    st.sidebar.markdown("- Development Analysis\n- Risk Analysis\n- Forecasting")

if __name__ == "__main__":
    main()