import pandas as pd
import streamlit as st
from streamlit_option_menu import option_menu
pd.set_option('display.max_columns', None)
import plotly.express as px
import warnings
warnings.filterwarnings("ignore")
import plotly.graph_objects as go
import seaborn as sns
import matplotlib.pyplot as plt
from PIL import Image


# Streamlit part

st.set_page_config(layout= "wide")
st.title(":blue[AIRBNB -- ANALYSIS]")
st.write("")

def datafr():
    df= pd.read_csv("F:\Desktop\Airbnb\sample_airbnb.csv")
    return df

df= datafr()

with st.sidebar:
    select= option_menu("Main Menu", ["Home", "Data Exploration", "About"])

if select == "Home":

 
    st.header(":blue[About Airbnb]")
    st.write("")
    st.write('''***Airbnb is an online platform that links property owners looking to rent out their spaces with travelers seeking temporary accommodations. 
            It provides hosts with a convenient way to generate income from their properties, while guests often discover that Airbnb rentals are more affordable and offer a more personalized experience compared to hotels.***''')
    st.write("")
    st.write('''***Airbnb, founded in 2008, has become a global pioneer in the hospitality industry through its innovative online platform.
              It allows hosts to list a wide array of accommodations for short-term rentals, ranging from apartments and houses to unique properties like castles and treehouses. 
              Travelers can explore these listings via Airbnb's user-friendly mobile app and website, which offer detailed photos, reviews, and direct booking capabilities.
              Operating in over 220 countries and regions, Airbnb has expanded the concept of lodging, providing guests with diverse and personalized travel experiences.
              Despite encountering regulatory challenges in some markets, the platform has significantly impacted the sharing economy and travel trends by empowering individuals to monetize their properties and enabling travelers to discover unique stays worldwide..***''')
    
    st.header(":blue[Background of Airbnb]")
    st.write("")
    st.write('''***Airbnb was born in 2007 when two Hosts welcomed three guests to their
              San Francisco home, and has since grown to over 4 million Hosts who have
                welcomed over 1.5 billion guest arrivals in almost every country across the globe.***''')


if select == "Data Exploration":
    tab1, tab2, tab3, tab4, tab5= st.tabs(["***PRICE ANALYSIS***","***AVAILABILITY ANALYSIS***","***LOCATION BASED***", "***GEOSPATIAL VISUALIZATION***", "***TOP CHARTS***"])
    with tab1:
        st.title("**PRICE DIFFERENCE**")
        col1,col2= st.columns(2)

        with col1:
            
            
            country= st.selectbox("Select the Country",df["country"].unique())

            df1= df[df["country"] == country]
            df1.reset_index(drop= True, inplace= True)

            room_ty= st.selectbox("Select the Room Type",df1["room_type"].unique())
            
            df2= df1[df1["room_type"] == room_ty]
            df2.reset_index(drop= True, inplace= True)

            df_bar= pd.DataFrame(df2.groupby("property_type")[["price","review_scores","number_of_reviews"]].sum())
            df_bar.reset_index(inplace= True)

            fig_bar= px.bar(df_bar, x='property_type', y= "price", title= "PRICE FOR PROPERTY_TYPES",hover_data=["number_of_reviews","review_scores"],color_discrete_sequence=px.colors.sequential.Magenta, width=600, height=500)
            st.plotly_chart(fig_bar)

        
        with col2:
            
            st.write("")
            st.write("")
            st.write("")
            st.write("")
            st.write("")
     
            proper_ty= st.selectbox("Select the Property_type",df2["property_type"].unique())

            df4= df2[df2["property_type"] == proper_ty]
            df4.reset_index(drop= True, inplace= True)

            df_pie= pd.DataFrame(df4.groupby("host_response_time")[["price","bedrooms"]].sum())
            df_pie.reset_index(inplace= True)

            fig_scatter = px.scatter(df_pie, x="bedrooms", y="price", color="host_response_time",
                         size="price", hover_name="host_response_time",
                         title="Price vs Bedrooms based on Host Response Time",
                         labels={"bedrooms": "Total Bedrooms", "price": "Total Price"},
                         color_discrete_sequence=px.colors.sequential.BuPu_r,
                         width=600, height=500)

            st.plotly_chart(fig_scatter)

        col1,col2= st.columns(2)

        with col1:

            
                # Select host response time
                hostresponsetime = st.selectbox("Select the host_response_time", df4["host_response_time"].unique())

                
                # Filter dataframe
                df5 = df4[df4["host_response_time"] == hostresponsetime]

                # Group and sum data
                df_do_bar = pd.DataFrame(df5.groupby("bed_type")[["minimum_nights", "maximum_nights", "price"]].sum())
                df_do_bar.reset_index(inplace=True)

                # Create an area chart
                fig_do_bar = px.area(df_do_bar, x='bed_type', y=['minimum_nights', 'maximum_nights'], 
                                    title='MINIMUM NIGHTS AND MAXIMUM NIGHTS', hover_data=["price"],
                                    color_discrete_sequence=px.colors.sequential.Rainbow, width=600, height=500)

                # Display the chart in Streamlit
                st.plotly_chart(fig_do_bar)

        with col2:

            st.write("")
            st.write("")
            st.write("")
            st.write("")
            st.write("")

            df_do_bar_2= pd.DataFrame(df5.groupby("bed_type")[["bedrooms","beds","accommodates","price"]].sum())
            df_do_bar_2.reset_index(inplace= True)

            fig_do_bar_2 = px.bar(df_do_bar_2, x='bed_type', y=['bedrooms', 'beds', 'accommodates'], 
            title='BEDROOMS AND BEDS ACCOMMODATES',hover_data="price",
            barmode='group',color_discrete_sequence=px.colors.qualitative.Plotly, width= 600, height= 500)
           
            st.plotly_chart(fig_do_bar_2)

    with tab2:

        def datafr():
            df_a= pd.read_csv("F:\Desktop\Airbnb\sample_airbnb.csv")
            return df_a

        df_a= datafr()

        st.title("**AVAILABILITY ANALYSIS**")
        col1,col2= st.columns(2)

        with col1:
            
            
            country_a= st.selectbox("Select the Country_a",df_a["country"].unique())

            df1_a= df[df["country"] == country_a]
            df1_a.reset_index(drop= True, inplace= True)

            property_ty_a= st.selectbox("Select the Property Type",df1_a["property_type"].unique())
            
            df2_a= df1_a[df1_a["property_type"] == property_ty_a]
            df2_a.reset_index(drop= True, inplace= True)

            # Create a donut chart
            df_a_donut_30 = px.pie(
                df2_a,
                names="room_type",
                values="availability_30",
                hole=0.4,  # Creates the donut effect
                color_discrete_sequence=px.colors.sequential.Peach,  # Change color sequence
                width=600,
                height=500,
                title="Availability_30"
            )

            # Display the chart in Streamlit
            st.plotly_chart(df_a_donut_30)
        
        with col2:
            st.write("")
            st.write("")
            st.write("")
            st.write("")
            st.write("")
            st.write("")
            st.write("")
            st.write("")
            st.write("")
            st.write("")
            

             # Create a donut chart
            fig_donut = px.pie(
                df2_a,
                names="room_type",
                values="availability_60",
                title="Availability_60",
                hole=0.4,  # This creates the donut effect
                color_discrete_sequence=px.colors.sequential.Blues_r,  # Change the color sequence here
                width=600,
                height=500
            )

            # Display the chart in Streamlit
            st.plotly_chart(fig_donut)

        col1,col2= st.columns(2)

        with col1:
            
            df_a_donut_90 = px.pie(df2_a,names="room_type",values="availability_90",color="bed_type",hole=0.4,width=600,height=500,
            title="Availability_90",
            color_discrete_sequence=px.colors.sequential.Aggrnyl_r
        )
        st.plotly_chart(df_a_donut_90)

        with col2:

                df_a_donut_365 = px.pie(df2_a,names="room_type",values="availability_365",color="bed_type",hole=0.4,width=600,height=500,title="Availability_365",
            color_discrete_sequence=px.colors.sequential.Greens_r
        )
        st.plotly_chart(df_a_donut_365)
        
        roomtype_a= st.selectbox("Select the Room Type_a", df2_a["room_type"].unique())

        df3_a= df2_a[df2_a["room_type"] == roomtype_a]

        df_mul_bar_a = pd.DataFrame(df3_a.groupby("host_response_time")[["availability_30", "availability_60", "availability_90", "availability_365", "price"]].sum())
        df_mul_bar_a.reset_index(inplace=True)

        # Create a line chart with points
        fig_df_mul_line_a = px.line(
            df_mul_bar_a,
            x='host_response_time',
            y=['availability_30', 'availability_60', 'availability_90', 'availability_365'],
            title='AVAILABILITY BASED ON HOST RESPONSE TIME',
            hover_data=["price"],
            markers=True,
            color_discrete_sequence=px.colors.sequential.Rainbow_r,
            width=1000
        )

        # Display the chart in Streamlit
        st.plotly_chart(fig_df_mul_line_a)


    with tab3:

        st.title("LOCATION ANALYSIS")
        st.write("")

        def datafr():
            df= pd.read_csv("F:\Desktop\Airbnb\sample_airbnb.csv")
            return df

        df_l= datafr()

        country_l= st.selectbox("Select the Country_l",df_l["country"].unique())

        df1_l= df_l[df_l["country"] == country_l]
        df1_l.reset_index(drop= True, inplace= True)

        proper_ty_l= st.selectbox("Select the Property_type_l",df1_l["property_type"].unique())

        df2_l= df1_l[df1_l["property_type"] == proper_ty_l]
        df2_l.reset_index(drop= True, inplace= True)

        st.write("")

        def select_the_df(sel_val):
            if sel_val == str(df2_l['price'].min())+' '+str('to')+' '+str(differ_max_min*0.30 + df2_l['price'].min())+' '+str("(30% of the Value)"):

                df_val_30= df2_l[df2_l["price"] <= differ_max_min*0.30 + df2_l['price'].min()]
                df_val_30.reset_index(drop= True, inplace= True)
                return df_val_30

            elif sel_val == str(differ_max_min*0.30 + df2_l['price'].min())+' '+str('to')+' '+str(differ_max_min*0.60 + df2_l['price'].min())+' '+str("(30% to 60% of the Value)"):
            
                df_val_60= df2_l[df2_l["price"] >= differ_max_min*0.30 + df2_l['price'].min()]
                df_val_60_1= df_val_60[df_val_60["price"] <= differ_max_min*0.60 + df2_l['price'].min()]
                df_val_60_1.reset_index(drop= True, inplace= True)
                return df_val_60_1
            
            elif sel_val == str(differ_max_min*0.60 + df2_l['price'].min())+' '+str('to')+' '+str(df2_l['price'].max())+' '+str("(60% to 100% of the Value)"):

                df_val_100= df2_l[df2_l["price"] >= differ_max_min*0.60 + df2_l['price'].min()]
                df_val_100.reset_index(drop= True, inplace= True)
                return df_val_100
            
        differ_max_min= df2_l['price'].max()-df2_l['price'].min()

        val_sel= st.radio("Select the Price Range",[str(df2_l['price'].min())+' '+str('to')+' '+str(differ_max_min*0.30 + df2_l['price'].min())+' '+str("(30% of the Value)"),
                                                    
                                                    str(differ_max_min*0.30 + df2_l['price'].min())+' '+str('to')+' '+str(differ_max_min*0.60 + df2_l['price'].min())+' '+str("(30% to 60% of the Value)"),

                                                    str(differ_max_min*0.60 + df2_l['price'].min())+' '+str('to')+' '+str(df2_l['price'].max())+' '+str("(60% to 100% of the Value)")])
                                          
        df_val_sel= select_the_df(val_sel)

        st.dataframe(df_val_sel)

        # checking the correlation

        df_val_sel_corr= df_val_sel.drop(columns=["listing_url","name", "property_type",                 
                                            "room_type", "bed_type","cancellation_policy",
                                            "img_url","host_url","host_name", "host_location",                   
                                            "host_response_time", "host_thumbnail_url",            
                                            "host_response_rate","host_is_superhost","host_has_profile_pic" ,         
                                            "host_picture_url","host_neighbourhood",
                                            "host_identity_verified","host_verifications",
                                            "street", "suburb", "government_area", "market",                        
                                            "country", "country_code","location_type","is_location_exact",
                                            "amenities"]).corr()
        
        st.dataframe(df_val_sel_corr)

        df_val_sel_gr= pd.DataFrame(df_val_sel.groupby("accommodates")[["cleaning_fee","bedrooms","beds","extra_people"]].sum())
        df_val_sel_gr.reset_index(inplace= True)

        fig_1 = px.sunburst(df_val_sel_gr,path=["accommodates", "bedrooms", "beds"],
        values="cleaning_fee",
        title="ACCOMMODATES",
        hover_data=["extra_people"],
        color_discrete_sequence=px.colors.sequential.Rainbow_r,
        width=1000)
        st.plotly_chart(fig_1)
        
        # Select box for Room_Type
        room_ty_l = st.selectbox("Select the Room_Type_l", df_val_sel["room_type"].unique())

        # Filtered dataframe
        df_val_sel_rt = df_val_sel[df_val_sel["room_type"] == room_ty_l]

        fig_2= px.bar(df_val_sel_rt, x= ["street","host_location","host_neighbourhood"],y="market", title="MARKET",
                    hover_data= ["name","host_name","market"], barmode='group',orientation='h', color_discrete_sequence=px.colors.sequential.Viridis,width=1000)
        st.plotly_chart(fig_2)

        fig_3 = px.scatter(
        df_val_sel_rt,
        x="government_area",
        y=["host_is_superhost", "host_neighbourhood", "cancellation_policy"],
        title="GOVERNMENT_AREA",
        hover_data=["guests_included", "location_type"],
        color_discrete_sequence=px.colors.sequential.Viridis,  # Change color sequence
        width=1000)
        st.plotly_chart(fig_3)

    with tab4:

        st.title("GEOSPATIAL VISUALIZATION")
        st.write("")        
        fig_bubble = px.scatter_mapbox(
            df,
            lat='latitude',
            lon='longitude',
            color='price',
            size='accommodates',
            color_continuous_scale='rainbow',
            hover_name='name',
            size_max=15,
            zoom=1,
            mapbox_style="carto-positron",
            title='Geospatial Distribution of Listings',
        )

        fig_bubble.update_layout(width=1150, height=800)
        st.plotly_chart(fig_bubble)

    with tab5:

        country_t= st.selectbox("Select the Country_t",df["country"].unique())

        df1_t= df[df["country"] == country_t]

        property_ty_t= st.selectbox("Select the Property_type_t",df1_t["property_type"].unique())

        df2_t= df1_t[df1_t["property_type"] == property_ty_t]
        df2_t.reset_index(drop= True, inplace= True)

        df2_t_sorted= df2_t.sort_values(by="price")
        df2_t_sorted.reset_index(drop= True, inplace= True)


        df_price= pd.DataFrame(df2_t_sorted.groupby("host_neighbourhood")["price"].agg(["sum","mean"]))
        df_price.reset_index(inplace= True)
        df_price.columns= ["host_neighbourhood", "Total_price", "Avarage_price"]
        
        col1, col2= st.columns(2)

        col1, col2 = st.columns(2)

        with col1:
            fig_price = px.scatter(
                df_price,
                x="Total_price",
                y="host_neighbourhood",
                size="Total_price",
                title="PRICE BASED ON HOST_NEIGHBOURHOOD",
                width=600,
                height=800,
                color="Total_price",
                color_continuous_scale=px.colors.sequential.Viridis
            )
            st.plotly_chart(fig_price)

        with col2:
            fig_price_2 = px.scatter(
                df_price,
                x="Avarage_price",
                y="host_neighbourhood",
                size="Avarage_price",
                title="AVERAGE PRICE BASED ON HOST_NEIGHBOURHOOD",
                width=600,
                height=800,
                color="Avarage_price",
                color_continuous_scale=px.colors.sequential.Viridis
            )
            st.plotly_chart(fig_price_2)

        with col1:

            df_price_1= pd.DataFrame(df2_t_sorted.groupby("host_location")["price"].agg(["sum","mean"]))
            df_price_1.reset_index(inplace= True)
            df_price_1.columns= ["host_location", "Total_price", "Avarage_price"]
            
            fig_price_3 = go.Figure(go.Waterfall(x=df_price_1["host_location"],y=df_price_1["Total_price"],
            orientation='h',
            connector={"line": {"color": "blue"}},
            decreasing={"marker": {"color": "red"}},
            increasing={"marker": {"color": "green"}},
            totals={"marker": {"color": "darkblue"}},
            ))

        fig_price_3.update_layout(
            title="PRICE BASED ON HOST_LOCATION",
            width=600,
            height=800)

        st.plotly_chart(fig_price_3)

        with col2:

           fig_price_4 = go.Figure(go.Waterfall(x=df_price_1["host_location"],
            y=df_price_1["Avarage_price"],
            orientation='h',
            text=df_price_1["Avarage_price"],
            connector={"line": {"color": "rgba(0, 0, 0, 0.6)"}},
            increasing={"marker": {"color": "yellow"}},
            decreasing={"marker": {"color": "red"}},
            totals={"marker": {"color": "pink"}}
           ))

        # Update layout
        fig_price_4.update_layout(
            title="AVERAGE PRICE BASED ON HOST_LOCATION",width=600,height=800,waterfallgap=0.3 )

        # Display the chart in Streamlit
        st.plotly_chart(fig_price_4)


        room_type_t= st.selectbox("Select the Room_Type_t",df2_t_sorted["room_type"].unique())

        df3_t= df2_t_sorted[df2_t_sorted["room_type"] == room_type_t]

        df3_t_sorted_price= df3_t.sort_values(by= "price")

        df3_t_sorted_price.reset_index(drop= True, inplace = True)

        df3_top_50_price= df3_t_sorted_price.head(100)

        fig_top_50_price_1 = px.treemap(df3_top_50_price,path=["name"],values="price",color="price",
        color_continuous_scale="icefire",
        range_color=(0, df3_top_50_price["price"].max()),
        title="MINIMUM NIGHTS, MAXIMUM NIGHTS AND ACCOMMODATES",
        hover_data=["minimum_nights", "maximum_nights", "accommodates"],
        width=1200,
        height=800
    )

        st.plotly_chart(fig_top_50_price_1)

        fig_top_50_price_2 = px.treemap(df3_top_50_price,path=["bed_type", "name"],values="price",color="price",
        color_continuous_scale="Magma",
        title="BEDROOMS, BEDS, ACCOMMODATES AND BED_TYPE",
        hover_data=["accommodates", "bedrooms", "beds", "bed_type"],
        width=1200,
        height=800
    )

        st.plotly_chart(fig_top_50_price_2)

if select == "About":

    st.header(":green[ABOUT THIS PROJECT]")

    st.subheader(":orange[1. Data Collection:]")

    st.write('''***Gather data from Airbnb's public API or other available sources.
        Collect information on listings, hosts, reviews, pricing, and location data.***''')
    
    st.subheader(":orange[2. Data Cleaning and Preprocessing:]")

    st.write('''***Clean and preprocess the data to handle missing values, outliers, and ensure data quality.
        Convert data types, handle duplicates, and standardize formats.***''')
    
    st.subheader(":orange[3. Exploratory Data Analysis (EDA):]")

    st.write('''***Conduct exploratory data analysis to understand the distribution and patterns in the data.
        Explore relationships between variables and identify potential insights.***''')
    
    st.subheader(":orange[4. Visualization:]")

    st.write('''***Create visualizations to represent key metrics and trends.
        Use charts, graphs, and maps to convey information effectively.
        Consider using tools like Matplotlib, Seaborn, or Plotly for visualizations.***''')
    
    st.subheader(":orange[5. Geospatial Analysis:]")

    st.write('''***Utilize geospatial analysis to understand the geographical distribution of listings.
        Map out popular areas, analyze neighborhood characteristics, and visualize pricing variations.***''')
