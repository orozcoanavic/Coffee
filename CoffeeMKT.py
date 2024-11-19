import streamlit as st
import pandas as pd
import plotly.express as px
from streamlit_option_menu import option_menu



# Cargar los datos
df = pd.read_csv("https://raw.githubusercontent.com/orozcoanavic/clasee/refs/heads/main/Coffee%20Shop%20Sales_update.csv")

with open('/content/waves.css') as f:
    css = f.read()
st.markdown(f'<style>{css}</style>', unsafe_allow_html=True)

st.markdown('<p class="dashboard_title">Coffee Shop Analysis Menu </p>', unsafe_allow_html = True)
st.markdown('<p class="dashboard_subtitle">by Ana Orozco</p>', unsafe_allow_html = True)

# Horizontal Menu
menu_selected = option_menu(
    None,
    ["Home", "Analysis", "Predictions", "Insights"],
    icons=['house', 'graph-up', 'lightning', 'lightbulb'],
    menu_icon="cast",
    default_index=0,
    orientation="horizontal",
    styles={
        "container": {"background-color": "#FFFFFF"},  # Fondo blanco
        "icon": {"color": "#1b594e", "font-size": "20px"},  #íconos
        "nav-link": {
            "font-size": "20px",
            "text-align": "center",
            "margin": "0px",
            "--hover-color": "#7cc3c9"
        },
        "nav-link-selected": {"background-color": "#ebdcef"},  # ítem seleccionado
    }
)

#HOME
if menu_selected=="Home":

    st.markdown("*This will help to create* **MKT Strategies** as well as: ")
    st.markdown("""
    - **Planning**
    - **Forecasting**""")

    st.write("Raw dataset:")
    st.write(df.head())

#ANALYSIS
if menu_selected=="Analysis":
    #1
    st.write("Data set summary:")
    st.write(df.describe().round(2))

    #2
    fig_hist = px.histogram(df, x="transaction_hour", title="Distribution of transaction hour")
    st.plotly_chart(fig_hist)

    #3
    x_column = "unit_price"
    y_column = "transaction_qty"

    fig_scatter = px.scatter(df, x=x_column, y=y_column, title=f"Scatter Plot of {x_column} vs {y_column}")
    st.plotly_chart(fig_scatter)


#PREDICTIONS
if menu_selected=="Predictions":
    st.write("The Predictions page")


    st.subheader("**Data Filters**")

    time_filter = st.selectbox("Select Hour:", options=df['transaction_hour'].unique(), index=0)
    filtered_data = df[df['transaction_hour'] == time_filter]

    quantity_range = st.slider("Select Transaction Quantity Range:", min_value=int(df['transaction_qty'].min()), max_value=int(df['transaction_qty'].max()), value=(int(df['transaction_qty'].min()), int(df['transaction_qty'].max())))
    filtered_data = filtered_data[(filtered_data['transaction_qty'] >= quantity_range[0]) & (filtered_data['transaction_qty'] <= quantity_range[1])]


    st.subheader("Filtered Dataset")
    st.write(filtered_data)

    st.subheader("Histogram of Transaction Quantity")
    fig4 = px.histogram(filtered_data, x='transaction_qty', title="Transaction Quantity Distribution")
    st.plotly_chart(fig4)




if menu_selected=="Insights":
    st.write("The Insights page")

    st.markdown("Key Performance Indicators")

    most_visited_store = df['store_location'].mode()[0]
    st.markdown("- **Most frequent Store:** %s" % most_visited_store)
    fam_prod = df['product_type'].mode()[0]
    st.markdown("- **Top product:** %s" % fam_prod)
