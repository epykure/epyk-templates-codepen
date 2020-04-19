
from epyk.core.Page import Report

import config
import random

# Create an empty report in the webpage
rptObj = Report()

# Add another sparkline with as a line type
rptObj.ui.charts.sparkline("line", [random.randint(-100, 100) for i in range(20)])

# Add a line return
rptObj.ui.layouts.new_line()

# Add another sparkline with as a bar type
rptObj.ui.charts.sparkline("bar", [random.randint(-100, 100) for i in range(20)])

# Transpile to Javascriot and create a report in codepen (python will automatically open the default browser)
rptObj.outs.browser.codepen(path=config.OUTPUT_PATHS)