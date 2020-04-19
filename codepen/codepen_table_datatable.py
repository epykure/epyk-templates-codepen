
from epyk.core.Page import Report
from epyk.tests import data_urls

import config

rptObj = Report()

data_rest_2 = rptObj.py.requests.csv(data_urls.AIRLINE_SAFETY, store_location=r"C:\tmps")

t2 = rptObj.ui.tables.datatables.table(data_rest_2)
t2.config.colReorder.activate()

rptObj.outs.browser.codepen(path=config.OUTPUT_PATHS, open_browser=True)
