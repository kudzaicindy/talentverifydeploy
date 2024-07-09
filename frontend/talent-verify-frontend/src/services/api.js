import axios from 'axios';
import Cookies from 'js-cookie';

const API_BASE_URL = 'http://localhost:8000/api/';

const api = axios.create({
  baseURL: API_BASE_URL,
  withCredentials: true,
});

export const getCsrfToken = async () => {
  const response = await api.get('/csrf/');
  return response.data.csrfToken;
};

api.interceptors.request.use(
  function (config) {
    const csrfToken = Cookies.get('csrftoken');
    if (csrfToken) {
      config.headers['X-CSRFToken'] = csrfToken;
    }
    return config;
  },
  function (error) {
    return Promise.reject(error);
  }
);

export const setAuthToken = (token) => {
  if (token) {
    api.defaults.headers.common['Authorization'] = `Bearer ${token}`;
  } else {
    delete api.defaults.headers.common['Authorization'];
  }
};

export const login = (username, password) => api.post('login/', { username, password });

export const register = (userData) =>
  api.post('register/', userData)
    .then(response => {
      console.log('Registration API response:', response);
      return response;
    })
    .catch(error => {
      console.error('Registration API error:', error.response?.data || error.message);
      throw error;
    });

export const searchEmployees = (query) => api.get(`employees/search/?q=${query}`);

export const getCompanyDepartments = (id) => api.get(`/companies/${id}/departments`);



export const getRoleHistory = async (employeeId) => {
  const response = await axios.get(`${API_BASE_URL}/employees/${employeeId}/roles/`);
  return response.data;
};

export const deleteRole = async (employeeId, roleId) => {
  const response = await axios.delete(`${API_BASE_URL}/roles/${roleId}/`);
  return response.data;
};

export const addRole = async (employeeId, roleData) => {
  const response = await axios.post(`${API_BASE_URL}/employees/${employeeId}/roles/`, roleData);
  return response.data;
};

export const getCompanies = () => api.get('companies/');

export const getCompany = (id) => api.get(`/companies/${id}`);

export const createCompany = (companyData) => api.post('companies/', companyData);

export const getEmployees = () => api.get('employees/');

export const getEmployee = (id) => api.get(`employees/${id}/`);

export const getEmployeeDetails = async (employeeId) => {
  try {
    const response = await api.get(`employees/${employeeId}/`);
    return response.data;
  } catch (error) {
    throw error;
  }
};

export const createEmployee = (employeeData) => api.post('/employees/', employeeData);

export const updateEmployee = (id, employeeData) => api.put(`/employees/${id}/`, employeeData);

export const deleteEmployee = (id) => api.delete(`/employees/${id}/`);

export const updateCompany = (id, companyData) => api.put(`/companies/${id}/`, companyData);

export const deleteCompany = (id) => api.delete(`/companies/${id}/`);

export const addDepartment = async (companyId, departmentData) => {
  console.log('Sending request to add department:', { companyId, departmentData });
  try {
    const response = await api.post(`/companies/${companyId}/departments/`, departmentData);
    console.log('Server response:', response);
    return response.data;
  } catch (error) {
    console.error('Server error response:', error.response?.data);
    throw error;
  }
};

export const deleteDepartment = (companyId, departmentId) => 
  api.delete(`/companies/${companyId}/departments/${departmentId}/`);

export const bulkUpload = async (file, companyId) => {
  const formData = new FormData();
  formData.append('file', file);
  formData.append('company', companyId);

  try {
    const response = await api.post('employees/bulk_upload/', formData, {
      headers: {
        'Content-Type': 'multipart/form-data',
      },
    });
    return response.data;
  } catch (error) {
    throw error;
  }
};

export default api;