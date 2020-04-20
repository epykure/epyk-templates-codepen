
from epyk.core.Page import Report

import config

# Create a basic report object
rpt = Report()

# Create a list of badges
rpt.ui.lists.badges([{'label': 'Python', 'value': 12}, {'label': 'R', 'value': 3}])

# Create a bespoke list
p = rpt.ui.lists.points()
for d in [{'label': 'Python', 'url': 'https://www.python.org/'}, {'label': 'R'}]:
  p.add_item(rpt.ui.link(d['label'], d.get('url')))

rpt.outs.browser.codepen(path=config.OUTPUT_PATHS)