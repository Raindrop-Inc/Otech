def attendance(employee, status, shift, attendance_date, log_type, datetime, late_entry=None, early_exit=None):
    attendance = frappe.new_doc("Attendance")
    attendance.employee = employee
    attendance.status = status
    attendance.shift = shift
    attendance.attendance_date = attendance_date
    attendance.docstatus = 1
    attendance.insert()
    frappe.db.commit()
    employee_check_in = frappe.new_doc("Employee Checkin")
    employee_check_in.employee = employee
    employee_check_in.log_type = log_type
    employee_check_in.datetime = datetime
    employee_check_in.attendance = attendance.name
    employee_check_in.insert()
    frappe.db.commit()
