
from epyk.core.Page import Report

import config

rptObj = Report()

l = rptObj.ui.links.link('data', 'www.google.fr', icon="fas fa-align-center", options={"target": "_blank"})

rptObj.ui.layouts.new_line()

# Add a badge
b = rptObj.ui.images.badge("new", background_color='red', color="white")
l.append_child(b)

# force new mepty line between two components on the page
rptObj.ui.layouts.new_line()

# Add a front end data link
rptObj.ui.links.data("test#data", value="this is a test")

rptObj.outs.browser.codepen(path=config.OUTPUT_PATHS)