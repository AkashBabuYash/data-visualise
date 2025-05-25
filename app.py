import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st
import seaborn as sns


st.markdown("<h1 style='text-align: right; margin-top: 20px;'>Data Visualistation</h1>", unsafe_allow_html=True)
st.sidebar.title("Navigation")


uploadfile = st.sidebar.file_uploader("Upload your CSV or Excel file", type=["csv", "xlsx"])

df = None
if uploadfile is not None:
    if uploadfile.name.endswith(".csv"):
        df = pd.read_csv(uploadfile)
    elif uploadfile.name.endswith(".xlsx"):
        df = pd.read_excel(uploadfile)
    
    st.write("### Data Preview")
    st.dataframe(df.head(24))
      
   
    
    
    st.write("### Dataset Information")
    st.write(df.info())
    
    
    st.write("### Summary Statistics")
    st.write(df.describe())
    
    st.write("### Missing Values")
    st.write(df.isnull().sum())
    
    
    selected_column = st.sidebar.selectbox("Select a Column for Analysis", df.columns)
    
    st.write("### Data Visualizations")
    plot_type = st.selectbox("Select Plot Type", ["Histogram","Pie Chart","Box Plot", "Scatter Plot", "Correlation Heatmap", "Bar Chart"])
    
    if plot_type == "Histogram":
        plt.figure(figsize=(8, 5))
        sns.histplot(df[selected_column], bins=30, kde=True)
        st.pyplot(plt)
    
    elif plot_type == "Box Plot":
        plt.figure(figsize=(8, 5))
        sns.boxplot(x=df[selected_column])
        st.pyplot(plt)
    elif plot_type == "Pie Chart":
        if df[selected_column].dtype == "object":
            pie_data = df[selected_column].value_counts()
        else:
            pie_data = pd.cut(df[selected_column], bins=5).value_counts()
        
        plt.figure(figsize=(8, 5))
        plt.pie(pie_data, labels=pie_data.index, autopct="%1.1f%%", startangle=90, colors=sns.color_palette("pastel"))
        plt.axis("equal")  
        st.pyplot(plt)
    
    elif plot_type == "Scatter Plot":
        col2 = st.selectbox("Select Second Column", df.columns)
        plt.figure(figsize=(8, 5))
        sns.scatterplot(x=df[selected_column], y=df[col2])
        st.pyplot(plt)
    
    elif plot_type == "Correlation Heatmap":
        plt.figure(figsize=(10, 6))
        sns.heatmap(df.corr(), annot=True, cmap="coolwarm")
        st.pyplot(plt)
    
    elif plot_type == "Bar Chart":
        plt.figure(figsize=(8, 5))
        sns.countplot(x=df[selected_column])
        st.pyplot(plt)
    
else:
    st.write("Upload a dataset to begin analysis!")
