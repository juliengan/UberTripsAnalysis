import streamlit as st
import numpy as np; np.random.seed(0)
import seaborn as sns; #sns.set_theme()
import pandas as pd
import altair as alt
import matplotlib.pyplot as plt
import time
from PIL import Image
import datetime
import streamlit.components.v1 as components
import os

###############################################  F  U  N  C  T  I  O  N  S  ##########################
def load_data(URL):
    data=pd.read_csv(URL)
    return data

def get_dom(dt):
    return dt.day 

def get_weekday(dt):
    return dt.weekday()

def get_hour(dt):
    return dt.hour

def count_rows(rows): 
    return len(rows)

#Streamlit dashboard of the datasets of the first lab

#L O A D I N G   B A R
@st.cache
def load_bar():
    latest_iteration = st.empty()
    bar = st.progress(0)
    for i in range(100):
    # Update the progress bar with each iteration.
        latest_iteration.text(f'Loading')
        bar.progress(i + 1)
        time.sleep(0.1)


#D E C O R A T O R S
#log execution time
@st.cache(suppress_st_warning=True) 
def log(func):
    def wrapper(*args,**kwargs):
        with open("logs.txt","a") as f:
            before = time.time()
            func()
            f.write("Called function with " + str(time.time() - before) + " seconds " + "\n")
            #f.write("Called function with " + " ".join([str(arg) for arg in args]) + " at " + str(datetime.datetime.now()) + "\n")
        val = func(*args,**kwargs)
        return val
    return wrapper

@log
def run(a,b,c=9):
    print(a+b+c )

#######################################  Data visualizations  ##############################################
@log
def point_cloud():
    pointcloud = st.expander("Point Cloud")
    df = pd.DataFrame(
        np.random.randn(200, 3),
        columns=['a', 'b', 'c'])

    c = alt.Chart(df).mark_circle().encode(
        x='a', y='b', size='c', color='c', tooltip=['a', 'b', 'c'])
    pointcloud.write(c)
    pointcloud.markdown('**Point cloud is still in construction...**')

#@timer
def dataset_print():
    expander = st.expander("Whole Dataset")
    expander.write(data)
@log
def heatmap():
    seaborn = st.expander("Heatmap")

    dt_grouped = data.groupby(['weekday','Hour']).apply(count_rows).unstack(level=0)

    fig, ax = plt.subplots()
    ax = sns.heatmap(dt_grouped)
    plt.title('Heatmap')
    seaborn.pyplot(fig)

@log
def histogram_dom():
    histo = st.expander("Histogram - Day of the month")
    fig2, ax2 = plt.subplots()
    plt.title('Histogram')
    ax2 = plt.hist(data['dom'], range = (0.5, 30.5), bins = 30, rwidth = 0.8)
    plt.title("Frequency by DoM - ")
    plt.xlabel("Date of the month")
    plt.ylabel("Frequency")
    histo.pyplot(fig2)

@log
def histogram_hour():
    histo = st.expander("Histogram - Hour of the day")
    fig3, hours = plt.subplots()
    plt.title('Histogram')
    hours = plt.hist(data['Hour'], range = (0.5, 24), bins = 24)
    plt.title("Frequency by Hour - ")
    plt.xlabel("Hour of the day")
    plt.ylabel("Frequency")
    histo.pyplot(fig3)

@log
def histogram_weekdays():
    weekdays = st.expander("Histogram - Weekdays")
    fig4, weekdaysax = plt.subplots()
    plt.title('Weekdays')
    weekdaysax = plt.hist(data['weekday'], range = (-0.5, 6.5), bins = 7, rwidth = 0.8)
    plt.title("Frequency by Weekday - ")
    plt.xlabel("Weekday")
    plt.ylabel("Frequency")
    weekdays.pyplot(fig4)


@log
def map():
    mapexp = st.expander("Map")
    map_data = pd.DataFrame(np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],columns=['lat', 'lon'])
    mapexp.map(map_data)
    mapexp.write("The map is still in construction...")

@log
def dataframe_print():
    chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['a', 'b', 'c'])
    #st.line_chart(chart_data)

@log
def twiny():
    twiny = st.expander("Twiny figure")
    ig,axes=plt.subplots()
    ig.set_size_inches(20, 20)
    axes.plot(data['Lon'],data['Lat'])
    x1, x2 = axes.get_xlim() 
    axes.set_xlabel("Lon",fontsize=12)
    axes.set_ylabel("Lat",fontsize=12)

    #twin_axes=axes.twiny()
    twiny.pyplot(ig)

############################################################################################"




#run(1,3,c=9) 
#load_bar()


st.title('LAB3 - Julie NGAN')
st.write('Here you can consult the trips and see information about the schedule and longitude/latitude from this list')

''''_RELEASE = False

if not _RELEASE:
    _component_func = components.declare_component(
        "my_component",
        url="http://localhost:3001",
    )
else:
    parent_dir = os.path.dirname(os.path.abspath(__file__))
    build_dir = os.path.join(parent_dir, "frontend/build")
    _component_func = components.declare_component("my_component", path=build_dir)

#bi directional component
def my_component(name, key=None):
    component_value = _component_func(name=name, key=key, default=0)
    return component_value


if not _RELEASE:
    import streamlit as st
    st.subheader("Say Hello !")
    num_clicks = my_component("Beautiful")
    st.markdown("You've clicked %s times!" % int(num_clicks))
    st.markdown("---")
    st.subheader("Component with variable args")
    name_input = st.text_input("Enter a name", value="Jeanne")
    num_clicks = my_component(name_input, key="foo")
    st.markdown("You've clicked %s times!" % int(num_clicks))'''




dfdash = pd.DataFrame({
'trips': ["Uber Trips in January, 2014", "NY Trips the 15th of January, 2015"],
})


#S I D E   B A R / M E N U
title = st.sidebar.title('Menu 🍔')
st.sidebar.write(dfdash)
option = st.sidebar.selectbox(
'Choose the trips',
dfdash['trips'])

chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['a', 'b', 'c'])

#st.sidebar.line_chart(chart_data)



st.write('You selected:', option)


if st.sidebar.checkbox('Subscribe'):
    #chart_data = pd.DataFrame(np.random.randn(20, 3),
    #columns=['a', 'b', 'c'])
    #st.write("")
    user_input = st.sidebar.text_area("Enter your email address", "gerard@hotmail.com")
    left_column, right_column = st.columns(2)
    pressed = st.sidebar.button('Enter')
    if pressed:
        st.sidebar.write("Well received!")

if option == "Uber Trips in January, 2014":
    #image = Image.open("uber.png")
    #st.image(image, width=None)
    data=load_data("uber-raw-data-apr14.csv")
    
#D A T A   T R A N S F O R M A T I O N
#def data_transformation(data):
    data['Date/Time'] = pd.to_datetime(data['Date/Time'])

    data['dom'] = data['Date/Time'].map(get_dom)
    data['weekday'] = data['Date/Time'].map(get_weekday)
    data['Hour'] = data['Date/Time'].map(get_hour)

        #hours = plt.hist(data['Hour'], range = (0.5, 24), bins = 24)
    


if option == "NY Trips the 15th of January, 2015":
   # image = Image.open('NY trips.jpg')
   # st.image(image, width=None)
    data=load_data("ny-trips-data.csv")

    #D A T A   T R A N S F O R M A T I O N
    data['tpep_pickup_datetime'] = pd.to_datetime(data['tpep_pickup_datetime'])

    data['tpep_dropoff_datetime'] = pd.to_datetime(data['tpep_dropoff_datetime'])

    data['dom'] = data['tpep_pickup_datetime'].map(get_dom)
    data['weekday'] = data['tpep_pickup_datetime'].map(get_weekday)
    data['Hour'] = data['tpep_pickup_datetime'].map(get_hour)



############## Expanders ##################

dataset_print()
point_cloud()
heatmap()
histogram_dom()
histogram_hour()
histogram_weekdays()
map()
dataframe_print()
#twiny()

##############################################


components.html(
    """
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">
    <script src="https://code.jquery.com/jquery-3.2.1.slim.min.js" integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN" crossorigin="anonymous"></script>
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js" integrity="sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl" crossorigin="anonymous"></script>
    <div id="accordion">
      <div class="card">
        <div class="card-header" id="headingOne">
          <h5 class="mb-0">
            <button class="btn btn-link" data-toggle="collapse" data-target="#collapseOne" aria-expanded="true" aria-controls="collapseOne">
            Shakespeare 📚
            </button>
          </h5>
        </div>
        <div id="collapseOne" class="collapse show" aria-labelledby="headingOne" data-parent="#accordion">
          <div class="card-body">
            <iframe src="https://informationisbeautiful.net/visualizations/words-shakespeare-invented/" title="Shakespeare's invented words" ,width=1024,height=768)
          </div>
        </div>
      </div>

      <div class="card">
        <div class="card-header" id="headingTwo">
          <h5 class="mb-0">
            <button class="btn btn-link collapsed" data-toggle="collapse" data-target="#collapseTwo" aria-expanded="false" aria-controls="collapseTwo">
            Point Cloud
            </button>
          </h5>
        </div>
        <div id="collapseTwo" class="collapse" aria-labelledby="headingTwo" data-parent="#accordion">
          <div class="card-body">
            <iframe src="https://informationisbeautiful.net/visualizations/words-shakespeare-invented/" title="Shakespeare's invented words" ,width=1024,height=768)
          </div>
        </div>
      </div>


    </div>
    """,
    height=600
)

components.iframe("https://informationisbeautiful.net/visualizations/words-shakespeare-invented/", width=1024,height=768)

components.iframe("https://pudding.cool/2021/04/music-bubble/", width=1024,height=768)







components.html(
'''<div class="footer container-xl width-full p-responsive" role="contentinfo">
  <div class="position-relative d-flex flex-row-reverse flex-lg-row flex-wrap flex-lg-nowrap flex-justify-center flex-lg-justify-between pt-6 pb-2 mt-6 f6 color-text-secondary border-top color-border-secondary ">
    <ul class="list-style-none d-flex flex-wrap col-12 col-lg-5 flex-justify-center flex-lg-justify-between mb-2 mb-lg-0">
      <li class="mr-3 mr-lg-0">2021 Julie Ngan, LAB3</li>
      <li class="mr-3 mr-lg-0">Streamlit, caching and components</li>

    </ul>

    
  </div>
  <div class="d-flex flex-justify-center pb-6">
    <span class="f6 color-text-tertiary"></span>
  </div>
</div>'''
)



