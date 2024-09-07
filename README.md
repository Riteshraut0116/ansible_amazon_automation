# Ansible Automation Project

This project automates the process of fetching Dell laptops from Amazon, creating an Excel file with the product details, and sending it via email.

## Repository Structure

ansible-automation/ ├── .github/ │ └── workflows/ │ └── deploy.yml ├── inventory.ini ├── playbook.yml ├── roles/ │ └── fetch_dell_laptops/ │ ├── tasks/ │ │ └── main.yml │ ├── vars/ │ │ └── main.yml │ ├── files/ │ │ ├── create_excel.py │ │ └── send_email.py ├── README.md