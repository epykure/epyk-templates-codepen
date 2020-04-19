

from epyk.core.Page import Report

import config

rptObj = Report()

# Create a number component
rptObj.ui.texts.number(12345697, options={"decPlaces": 5, "decSeparator": "."})

rptObj.outs.browser.codepen(path=config.OUTPUT_PATHS)
