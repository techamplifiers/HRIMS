from django.contrib.auth import views as auth_views
from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name="home-page"),
    path('login', auth_views.LoginView.as_view(template_name='employee_information/login1.html',
                                               redirect_authenticated_user=True), name="login"),
    path('register', views.registrations, name='register'),
    path('logout', views.logout_user, name="logout"),
    path('about', views.about, name="about-page"),
    path('departments', views.departments, name="department-page"),
    path('manage_departments', views.manage_departments, name="manage_departments-page"),
    path('save_department', views.save_department, name="save-department-page"),
    path('delete_department', views.delete_department, name="delete-department"),
    path('positions', views.positions, name="position-page"),
    path('manage_positions', views.manage_positions, name="manage_positions-page"),
    path('save_position', views.save_position, name="save-position-page"),
    path('delete_position', views.delete_position, name="delete-position"),
    path('employees', views.employees, name="employee-page"),
    path('save_tag_employee/<int:id>', views.save_tag_employee, name='save_tag_employee'),
    path('personal_info', views.personal_info, name='personal_info'),
    path('savePersonal', views.savePersonal, name='savePersonal'),
    path('update_employee/<int:id>', views.update_employee, name='update_employee'),
    path('updatePersonal/<int:id>', views.updatePersonal, name='updatePersonal'),
    path('saveEducational', views.saveEducational, name='saveEducational'),
    path('Edit_education/<int:id>', views.Edit_education, name='Edit_education'),
    path('updateEducation/<int:id>', views.updateEducation, name='updateEducation'),
    path('add_education', views.add_education, name='add_education'),
    path('saveExperience', views.saveExperience, name='saveExperience'),
    path('View_experience', views.View_experience, name='View_experience'),
    path('Edit_experience/<int:id>', views.Edit_experience, name='Edit_experience'),
    path('updateExperience/<int:id>', views.updateExperience, name='updateExperience'),
    path('add_experience', views.add_experience, name='add_experience'),
    path('leave_request', views.leave_request, name='leave_request'),
    path('saveLeave', views.saveLeave, name='saveLeave'),
    path('login_hrs', views.login_hrs, name='login_hrs'),
    path('employee_login', views.employee_login, name='employee_login'),
    path('employee_leave', views.employee_leave, name='employee_leave'),
    path('update_emp_request/<int:id>', views.update_emp_request, name='update_emp_request'),
    path('saveBreak', views.saveBreak, name='saveBreak'),
    path('update_leave_request/<int:id>', views.update_leave_request, name='update_leave_request'),
    path('updateLeave/<int:id>', views.updateLeave, name='updateLeave'),
    path('select_employee', views.select_employee, name='select_employee'),
    path('select_salary_date', views.select_salary_date, name='select_salary_date'),
    path('salary_details', views.salary_details, name='salary_details'),
    path('salary_hr', views.salary_hr, name='salary_hr'),
    path('save_salary', views.save_salary, name='save_salary'),
    path('view_employee_salary', views.view_employee_salary, name='view_employee_salary'),
    path('Edit_salary/<int:id>', views.Edit_salary, name='Edit_salary'),
    path('updateSalary/<int:id>', views.updateSalary, name='updateSalary'),
    path('render_to_pdf', views.render_to_pdf, name='render_to_pdf'),
    path('view_average_login_hrs/<int:id>', views.view_average_login_hrs, name='view_average_login_hrs'),
    path('help_desk', views.help_desk, name='help_desk'),
    path('save_IT_Help', views.save_IT_Help, name='save_IT_Help'),
    path('view_leave', views.view_leave, name='view_leave'),
    path('update_leave/<int:id>', views.update_leave, name='update_leave'),
    path('save_leave_type/<int:id>', views.save_leave_type, name='save_leave_type'),
    path('save_new_leave', views.save_new_leave, name='save_new_leave'),
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]