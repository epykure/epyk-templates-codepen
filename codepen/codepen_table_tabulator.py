
from epyk.core.Page import Report
from epyk.tests import data_urls

import config

rptObj = Report()

data_rest_2 = rptObj.py.requests.csv(data_urls.AIRLINE_SAFETY, store_location=config.OUTPUT_TEMPS)

t1 = rptObj.ui.tables.tabulators.table(data_rest_2)
t1.config.paginationSize = 10

rptObj.outs.browser.codepen(path=config.OUTPUT_PATHS)
