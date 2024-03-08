import streamlit as st
import pandas as pd
import numpy as np
#data visualization with matplotlib and seaborn
import matplotlib.pyplot as plt
import seaborn as sns

df=pd.DataFrame(np.random.randn(20,3),columns=['Line-1','Line-2','Line-3'])

st.subheader("Line Chart")
st.line_chart(df)

st.subheader("Area Chart")
st.area_chart(df)

st.subheader("Bar Chart")
st.bar_chart(df)

st.header(">Data Visualization With Matplotlib")
st.subheader("Loading the Dataframe")
df=pd.read_csv(r"C:\Users\KIIT\Desktop\Streamlit\plot\iris.csv")
st.dataframe(df)
st.subheader("Simple Distribution Plot")
fig=plt.figure(figsize=(15,8))
df["species"].value_counts().plot(kind="bar") #counting the no of different species
st.pyplot(fig)

#using seaborn
fig=plt.figure(figsize=(15,8))
sns.distplot(df['sepal_length'])
st.pyplot(fig)


st.header("working with multiple graphs")
col1,col2=st.columns(2)
with col1:
    col1.header="KDE=False"
    col1.write("KDE = False")
    fig1=plt.figure()
    sns.distplot(df['sepal_length'],kde=False)
    st.pyplot(fig1)

with col2:
    col2.header="Histogram=False"
    col2.write("Histogram = False")
    fig2=plt.figure()
    sns.distplot(df['sepal_length'],hist=False)
    st.pyplot(fig2)

st.header("Changing the style of the graph")
col1,col2=st.columns(2)
with col1:
    fig1=plt.figure()
    sns.set_style("darkgrid")
    sns.set_context("notebook")
    sns.distplot(df['petal_length'],hist=False)
    st.pyplot(fig1)

with col2:
    fig2=plt.figure()
    sns.set_theme(context="poster",style="darkgrid")
    sns.distplot(df['petal_length'],hist=False)
    st.pyplot(fig2)


st.header("Exploring different graphs")
st.subheader("Scatter Plot")
fig,ax=plt.subplots(figsize=(15,8))
ax.scatter(*np.random.random(size=(2,100)))
st.pyplot(fig)




st.subheader("Count Plot")
fig=plt.figure(figsize=(15,8))
sns.countplot(data=df,x='species')
st.pyplot(fig)




st.subheader("Box Plot")
fig=plt.figure(figsize=(15,8))
sns.boxplot(data=df,x="species",y="petal_length")
st.pyplot(fig)




st.subheader("Violen Plot")
fig=plt.figure(figsize=(15,8))
sns.violinplot(data=df,x="species",y="petal_length")
st.pyplot(fig)