
from epyk.core.Page import Report

import config

rptObj = Report()

rptObj.ui.charts.sparkline("box", [1, 2, 3, 4, 5, 4, 3, 2, 1])

rptObj.ui.charts.sparkline("bar", [1, 2, 3, 4, 5, 4, 3, 2, 10])

rptObj.outs.browser.codepen(path=config.OUTPUT_PATHS)
