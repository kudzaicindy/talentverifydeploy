from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    CompanyViewSet, DepartmentViewSet, EmployeeViewSet, RoleViewSet,
    EmployeeSearchView, register, login_view, get_csrf_token, add_employee,
    employee_role_history, employee_list, employee_detail, add_employee_history
)
from django.contrib.auth.views import LogoutView

router = DefaultRouter()
router.register(r'companies', CompanyViewSet, basename='company')
router.register(r'departments', DepartmentViewSet, basename='department')
router.register(r'employees', EmployeeViewSet)
router.register(r'roles', RoleViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('register/', register, name='register'),
    path('login/', login_view, name='login'),
    path('csrf/', get_csrf_token, name='get_csrf_token'),
    path('employees/', employee_list, name='employee_list'),
    path('employees/add/', add_employee, name='add_employee'),
    path('employees/<int:employee_id>/', employee_detail, name='employee_detail'),
    path('employees/<int:employee_id>/add_history/', add_employee_history, name='add_employee_history'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    
    path('employees/<int:employee_id>/roles/', RoleViewSet.as_view({'get': 'employee_roles', 'post': 'employee_roles'}), name='employee-role-list-create'),
    path('companies/<int:company_id>/', include(router.urls)),
    path('companies/<int:company_id>/departments/', DepartmentViewSet.as_view({'get': 'list', 'post': 'create'}), name='department-list-create'),
    path('companies/<int:company_id>/departments/<int:pk>/', DepartmentViewSet.as_view({'get': 'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'}), name='department-detail'),
    path('employees/<int:id>/role-history/', employee_role_history, name='employee_role_history'),
    path('employees/bulk_upload/', EmployeeViewSet.as_view({'post': 'bulk_upload'}), name='employee-bulk-upload'),
    path('employees/search/', EmployeeSearchView.as_view(), name='employee_search'),
    path('api-auth/', include('rest_framework.urls')),
]