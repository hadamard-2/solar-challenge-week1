import streamlit as st
import pandas as pd
import plotly.express as px
from utils import load_data, calculate_summary_stats

st.set_page_config(
    page_title="Solar Data Discovery Dashboard",
    page_icon="☀️",
    layout="wide"
)

def main():
    st.title("☀️ Solar Data Discovery Dashboard")
    st.subheader("Comparing Solar Potential Across Countries")

    # Load data
    try:
        df = load_data()
        
        # Sidebar for controls
        st.sidebar.header("Controls")
        selected_countries = st.sidebar.multiselect(
            "Select Countries",
            options=["Benin", "Sierra Leone", "Togo"],
            default=["Benin", "Sierra Leone", "Togo"]
        )

        selected_metric = st.sidebar.selectbox(
            "Select Solar Metric",
            options=["GHI", "DNI", "DHI"],
            index=0
        )

        # Filter data based on selection
        filtered_df = df[df["Country"].isin(selected_countries)][["Country", "Timestamp", selected_metric]]

        # Main content area
        col1, col2 = st.columns([2, 1])

        with col1:
            st.subheader(f"{selected_metric} Distribution by Country")
            fig = px.box(
                filtered_df,
                x="Country",
                y=selected_metric,
                color="Country",
                title=f"Distribution of {selected_metric} Values"
            )
            st.plotly_chart(fig, use_container_width=True)

        with col2:
            st.subheader("Summary Statistics")
            summary_stats = calculate_summary_stats(filtered_df, selected_metric)
            st.dataframe(
                summary_stats,
                hide_index=False,
                use_container_width=True
            )

        # Time series visualization
        st.subheader(f"{selected_metric} Time Series")
        fig_ts = px.line(
            filtered_df,
            x="Timestamp",
            y=selected_metric,
            color="Country",
            title=f"{selected_metric} Values Over Time"
        )
        st.plotly_chart(fig_ts, use_container_width=True)

    except Exception as e:
        st.error(f"Error loading data: {str(e)}")
        
if __name__ == "__main__":
    main()