# Solar Data Discovery Dashboard

This directory contains scripts for the Solar Data Discovery interactive dashboard.

## Structure

- `app/main.py`: Main Streamlit application script
- `app/utils.py`: Utility functions for data processing and visualization

## Features

- Interactive country selection
- Multiple solar metric visualizations (GHI, DNI, DHI)
- Summary statistics
- Time series analysis
- Box plots for distribution analysis

## Running the Dashboard

1. Ensure you are in the project root directory
2. Activate your virtual environment
3. Install requirements:
   ```bash
   pip install -r requirements.txt
   ```
4. Run the Streamlit app:
   ```bash
   streamlit run app/main.py
   ```

## Dashboard Components

- **Country Selector**: Choose one or more countries to compare
- **Metric Selector**: Switch between GHI, DNI, and DHI measurements
- **Distribution Plot**: Box plot showing data distribution by country
- **Summary Statistics**: Key metrics table with mean, median, and standard deviation
- **Time Series**: Interactive plot showing metric changes over time