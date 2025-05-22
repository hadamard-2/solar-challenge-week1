import pandas as pd
import streamlit as st

@st.cache_data
def load_data():
    """Load and combine data from all countries."""
    # Load data
    benin = pd.read_csv('./data/benin-malanville_clean.csv')
    sierraleone = pd.read_csv('./data/sierraleone-bumbuna_clean.csv')
    togo = pd.read_csv('./data/togo-dapaong_qc_clean.csv')
    
    # Add country column
    benin['Country'] = 'Benin'
    sierraleone['Country'] = 'Sierra Leone'
    togo['Country'] = 'Togo'
    
    # Combine datasets
    df = pd.concat([benin, sierraleone, togo], ignore_index=True)
    
    # Convert timestamp to datetime
    df['Timestamp'] = pd.to_datetime(df['Timestamp'])
    
    return df

@st.cache_data
def calculate_summary_stats(df, metric):
    """Calculate summary statistics for the selected metric."""
    summary = df.groupby('Country')[metric].agg([
        ('Mean', 'mean'),
        ('Median', 'median'),
        ('Std Dev', 'std')
    ]).round(2)
    
    # Sort by mean value descending
    return summary.sort_values(by='Mean', ascending=False)