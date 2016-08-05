from admin_interface import AdminInterface


logged_in_as_admin = AdminInterface.log_in()
if logged_in_as_admin:
    interface = AdminInterface()
    interface.run()
