from . import __version__ as app_version

app_name = "project"
app_title = "Project"
app_publisher = "Midocean Technologies Pvt Ltd"
app_description = "Custom Project App for ERPNext / Frappe"
app_icon = "octicon octicon-file-directory"
app_color = "grey"
app_email = "sagar@midocean.tech"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
app_include_css = "/assets/project/css/business_theme_v14.css"

# app_include_js = "/assets/project/js/project.js"

# include js, css files in header of web template
# web_include_css = "/assets/project/css/project.css"
# web_include_js = "/assets/project/js/project.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "project/public/scss/website"

# Installation
# ------------

# before_install = "project.install.before_install"
# after_install = "project.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "project.uninstall.before_uninstall"
# after_uninstall = "project.uninstall.after_uninstall"

# Desk Notifications
# ------------------

# notification_config = "project.notifications.get_notification_config"

# Scheduled Tasks
# ---------------

# scheduler_events = {
#     "all": ["project.tasks.all"],
#     "daily": ["project.tasks.daily"],
#     "hourly": ["project.tasks.hourly"],
#     "weekly": ["project.tasks.weekly"],
#     "monthly": ["project.tasks.monthly"],
# }

# Testing
# -------

# before_tests = "project.install.before_tests"

# Overriding Methods
# ------------------

# override_whitelisted_methods = {
#     "frappe.desk.doctype.event.event.get_events": "project.event.get_events"
# }

# override_doctype_dashboards = {
#     "Task": "project.task.get_dashboard_data"
# }
