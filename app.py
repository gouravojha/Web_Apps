import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Agg')
import seaborn as sns



def main():
      st.title("Data Analysis and Data Visualization")
      st.text("Using Machine Learning and Streamlit")
      activity = ['Data Analysis','Data Visualization','Model Building','About']
      choice = st.sidebar.selectbox("Select your Activity",activity)

      if choice  == 'Data Analysis':
            st.subheader("Explore your Data")

            data = st.file_uploader("Upload Dataset",type=["csv","txt","xls","xlsx"])
            if data is not None:
                  df = pd.read_csv(data)
                  st.dataframe(df.head())

                  if st.checkbox("Show shape"):
                        st.write(df.shape)

                  if st.checkbox("Show Columns"):
                        all_columns = df.columns.to_list()
                        st.write(all_columns)

                  if st.checkbox("Select columns to Show"):
                        selected_columns = st.multiselect("Select Columns",all_columns)
                        new_df = df[selected_columns]
                        st.dataframe(new_df)

                  if st.checkbox("Show Summary"):
                        st.write(df.describe())

                  if st.checkbox("Show Value Count"):
                        st.write(df.iloc[:,1].value_counts())










            

      elif choice  == 'Data Visualization':
            st.subheader("Visualize your Data")

            data = st.file_uploader("Upload Dataset",type=["csv","txt","xls","xlsx"])
            if data is not None:
                  df = pd.read_csv(data)
                  st.dataframe(df.head())

            if st.checkbox("Heat Map Chart"):
                  st.write(sns.heatmap(df.corr(),annot = True))
                  st.pyplot()

            if st.checkbox("Pie Chart"):
                  all_columns = df.columns.to_list()
                  column_to_plot = st.selectbox("Select 1 column to plot",all_columns)
                  pie_plot = df[column_to_plot].value_counts().plot.pie(autopct = "%1.1f%%")
                  st.write(pie_plot)
                  st.pyplot()


            

      elif choice  == 'Model Building':
            st.subheader("Model your Data with ML")

      elif choice  == 'About':
            st.subheader("About")      
            




if  __name__ == '__main__':
      main()
      
      
