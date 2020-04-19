
from epyk.core.Page import Report

import config

rptObj = Report()

# Create icon object from font awesome
rptObj.ui.icons.capture()

rptObj.ui.icons.table(tooltip="helper")

rptObj.ui.icons.awesome("fas fa-stopwatch", tooltip="helper")

rptObj.ui.icon("fab fa-css3-alt")

rptObj.ui.images.badge("5", "Label", icon="fas fa-align-center")

rptObj.ui.images.badge("New")

rptObj.outs.browser.codepen(path=config.OUTPUT_PATHS)