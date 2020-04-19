
from epyk.core.Page import Report

import config


rptObj = Report()

rptObj.ui.rich.stars(3, label="feedbacks")
rptObj.ui.rich.stars(3, label="feedbacks", best=10)
rptObj.ui.vignets.bubble({"value": 23, "title": "Title"}, helper="This is a helper")
rptObj.ui.rich.delta({'number': 100, 'prevNumber': 60, 'thresold1': 100, 'thresold2': 50}, helper="test")
rptObj.ui.vignets.text({'title': 'Python', 'number': 100, 'text': 'Content', 'color': 'green', 'url':
                       'https://www.python.org/', 'icon': 'fab fa-python', 'tooltip': 'Python Fondation',
                       'urlTitle': 'WebSite'})
rptObj.ui.rich.light("red", label="label", tooltip="Tooltip", helper="Helper")

# Sliders
rptObj.ui.slider([1, 2, 3, 4, 5, 6, 7])
rptObj.ui.sliders.progressbar(300)

rptObj.outs.browser.codepen(path=config.OUTPUT_PATHS)
