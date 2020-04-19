
from epyk.core.Page import Report

import config

rptObj = Report()

# Create a default datepicker object
cob = rptObj.ui.date()

# Create a date picker object starting today
today = rptObj.ui.fields.today(label="Date", helper="This is the report timestamp")

# Create a datepicker object with two excluded date
rptObj.ui.fields.cob(label="Date").excluded_dates(["2020-09-01", "2020-09-06"])

# Create a timepicker object
rptObj.ui.fields.now(label="timestamp", color="red", helper="This is the report timestamp")

# Add a countdown object
rptObj.ui.rich.countdown("2020-09-24", label="Countdown")

# Add a tag date
rptObj.ui.rich.update()

rptObj.outs.browser.codepen(path=config.OUTPUT_PATHS)
