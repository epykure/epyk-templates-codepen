
from epyk.core.Page import Report

import config

rptObj = Report()

# Add different type of inputs
rptObj.ui.input()
rptObj.ui.inputs.search()
rptObj.ui.inputs.password()
rptObj.ui.inputs.textarea()
rptObj.ui.inputs.d_search("")
rptObj.ui.inputs.d_int()

# Add a button with a click event
b = rptObj.ui.button("add tag")

rptObj.outs.browser.codepen(path=config.OUTPUT_PATHS)