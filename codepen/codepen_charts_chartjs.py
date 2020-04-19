
from epyk.core.Page import Report
from epyk.tests import data_urls

import config

rptObj = Report()

data_rest = rptObj.py.requests.csv(data_urls.PLOTLY_APPLE_PRICES, store_location=config.OUTPUT_TEMPS)

ts = rptObj.ui.charts.chartJs.timeseries(data_rest, y_columns=['AAPL.Open'], x_axis="Date")

rptObj.outs.browser.codepen(path=config.OUTPUT_PATHS)