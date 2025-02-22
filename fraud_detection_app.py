# Importing necessary libraries
import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Function to check if a transaction is fraudulent based on a single feature
def check_transaction_single_feature(value, threshold=1.0):
    """
    Checks if a transaction is fraudulent based on a single feature.
    """
    return value > threshold  # Fraudulent if the value exceeds the threshold

# Streamlit app definition
def main():
    # Set the title of the Streamlit app
    st.title("Transaction Fraud Detection")
    
    # Provide a brief description
    st.markdown("""
        This app detects if a transaction is fraudulent based on a single feature (V4).
        Input the feature value to check if the transaction is authentic or fraudulent.
    """)
    
    # Input feature value
    st.subheader("Enter the transaction detail")
    value = st.number_input("Enter value for feature 'V4':", min_value=-10.0, max_value=10.0, value=0.0, step=0.1)

    # Check transaction
    is_fraudulent = check_transaction_single_feature(value, threshold=1.0)

    # Display the result
    st.subheader("Transaction Result")
    if is_fraudulent:
        st.error("The transaction is FRAUDULENT.")
    else:
        st.success("The transaction is AUTHENTIC.")

    # Option to visualize some example data
    st.subheader("Example Data Visualization")
    if st.checkbox("Show example histogram for 'V4' feature"):
        # Example data for visualization
        example_data = np.random.normal(loc=0, scale=2, size=500)  # Random normal data
        plt.figure(figsize=(8, 5))
        sns.histplot(example_data, bins=30, kde=True, color="blue", label="V4 Distribution")
        plt.axvline(x=1.0, color='red', linestyle='--', label='Threshold')
        plt.title("Histogram of Feature 'V4'")
        plt.xlabel("V4 Value")
        plt.ylabel("Frequency")
        plt.legend()
        st.pyplot(plt)

if __name__ == "__main__":
    main()
