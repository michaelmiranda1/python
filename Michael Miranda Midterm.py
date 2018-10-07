
# coding: utf-8

# '''
# PART TWO:
# 
# Students choice!
# 
# Create a new Jupyter notebook.
# In that notebook, I would like for you to choose a plotting library (matplotlib, bokeh, holoviews, or seaborn)
# and either a data set from the example data sets included with that library or another data set you may find
# of particular interest. 
# 
# In one or more cells, write a short report about the data set, using Markdown and LaTeX markup as necessary to describe the data, and what a reader might glean from it.
# 
# In additional cells, write a short Python program to read in the data set and produce one or more plots from the data.
# 
# '''

# In[ ]:


import numpy as np
import holoviews as hv
hv.extension('bokeh')
import bokeh.sampledata
bokeh.sampledata.download()


# This data set has information of four stocks of Apple(AAPL) Google(GOOG), IBM(IBM) and Microsoft(MSFT). This is targeted of getting the information from the date and the adjusted close price. The first graph gives us an indication of the trend over time on how the adjusted close price moved in relation to time since 2000. These are compared to each other. This data would give the reader an indication and an outlook to compare and contrast each other in relation to related to tech stocks. This would try to give a relatable forecast to try to make the best investment for future assets based on historical data. 
# 
# The tech industry could also provide some data if there is some mutually exclusive data that correlates with each other. Some data will have trends that all stocks will go in an upward motion as an industry as a whole. The data can give an indication as to see if some stocks have a correlation with each other. 
# 
# The one month average graph's can give an indication as an analytical tool used to identify current price trends and the potential for a change in an established trend.
# 
# The moving average (MA) is a simple technical analysis tool that smooths out price data by creating a constantly updated average price. The average is taken over a specific period of time, like 10 days, 20 minutes, 30 weeks or any time period the trader chooses. There are advantages to using a moving average in your trading, as well as options on what type of moving average to use. Moving average strategies are also popular and can be tailored to any time frame, suiting both long-term investors and short-term traders.
# 
# A moving average simplifies price data by smoothing it out and creating one flowing line. This makes seeing the trend easier. Exponential moving averages react quicker to price changes than simple moving averages. In some cases, this may be good, and in others, it may cause false signals. Moving averages with a shorter look back period (20 days, for example) will also respond quicker to price changes than an average with a longer look back period (200 days).
# 
# Moving average crossovers are a popular strategy for both entries and exits. MAs can also highlight areas of potential support or resistance. While this may appear predictive, moving averages are always based on historical data and simply show the average price over a certain time period.
# 

# In[5]:


import numpy as np

from bokeh.layouts import gridplot
from bokeh.plotting import figure, show, output_file
from bokeh.sampledata.stocks import AAPL, GOOG, IBM, MSFT

def datetime(x):
    return np.array(x, dtype=np.datetime64)

p1 = figure(x_axis_type="datetime", title="Stock Closing Prices")
p1.grid.grid_line_alpha=0.3
p1.xaxis.axis_label = 'Date'
p1.yaxis.axis_label = 'Price'

p1.line(datetime(AAPL['date']), AAPL['adj_close'], color='#A6CEE3', legend='AAPL')
p1.line(datetime(GOOG['date']), GOOG['adj_close'], color='#B2DF8A', legend='GOOG')
p1.line(datetime(IBM['date']), IBM['adj_close'], color='#33A02C', legend='IBM')
p1.line(datetime(MSFT['date']), MSFT['adj_close'], color='#FB9A99', legend='MSFT')
p1.legend.location = "top_left"

aapl = np.array(AAPL['adj_close'])
aapl_dates = np.array(AAPL['date'], dtype=np.datetime64)

window_size = 30
window = np.ones(window_size)/float(window_size)
aapl_avg = np.convolve(aapl, window, 'same')

p2 = figure(x_axis_type="datetime", title="AAPL One-Month Average")
p2.grid.grid_line_alpha = 0
p2.xaxis.axis_label = 'Date'
p2.yaxis.axis_label = 'Price'
p2.ygrid.band_fill_color = "olive"
p2.ygrid.band_fill_alpha = 0.1

p2.circle(aapl_dates, aapl, size=4, legend='close',
          color='darkgrey', alpha=0.2)

p2.line(aapl_dates, aapl_avg, legend='avg', color='navy')
p2.legend.location = "top_left"


goog = np.array(GOOG['adj_close'])
goog_dates = np.array(GOOG['date'], dtype=np.datetime64)

window_size = 30
window = np.ones(window_size)/float(window_size)
goog_avg = np.convolve(goog, window, 'same')

p3 = figure(x_axis_type="datetime", title="GOOG One-Month Average")
p3.grid.grid_line_alpha = 0
p3.xaxis.axis_label = 'Date'
p3.yaxis.axis_label = 'Price'
p3.ygrid.band_fill_color = "olive"
p3.ygrid.band_fill_alpha = 0.1

p3.circle(goog_dates, goog, size=4, legend='close',
          color='pink', alpha=0.2)

p3.line(goog_dates, goog_avg, legend='avg', color='orange')
p3.legend.location = "top_left"


ibm = np.array(IBM['adj_close'])
ibm_dates = np.array(IBM['date'], dtype=np.datetime64)

window_size = 30
window = np.ones(window_size)/float(window_size)
ibm_avg = np.convolve(ibm, window, 'same')

p4 = figure(x_axis_type="datetime", title="IBM One-Month Average")
p4.grid.grid_line_alpha = 0
p4.xaxis.axis_label = 'Date'
p4.yaxis.axis_label = 'Price'
p4.ygrid.band_fill_color = "cyan"
p4.ygrid.band_fill_alpha = 0.1

p4.circle(ibm_dates, ibm, size=4, legend='close',
          color='green', alpha=0.2)

p4.line(ibm_dates, ibm_avg, legend='avg', color='red')
p4.legend.location = "top_left"

msft = np.array(MSFT['adj_close'])
msft_dates = np.array(MSFT['date'], dtype=np.datetime64)

window_size = 30
window = np.ones(window_size)/float(window_size)
msft_avg = np.convolve(msft, window, 'same')

p5 = figure(x_axis_type="datetime", title="MSFT One-Month Average")
p5.grid.grid_line_alpha = 0
p5.xaxis.axis_label = 'Date'
p5.yaxis.axis_label = 'Price'
p5.ygrid.band_fill_color = "yellow"
p5.ygrid.band_fill_alpha = 0.1

p5.circle(msft_dates, msft, size=4, legend='close',
          color='black', alpha=0.2)

p5.line(msft_dates, msft_avg, legend='avg', color='indigo')
p5.legend.location = "top_left"

output_file("stocks.html", title="stocks.py example")

show(gridplot([[p1,p2,p3,p4,p5]], plot_width=400, plot_height=400))  # open a browser

