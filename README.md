# CRMify - Customer Relationship Management System

CRMify is a web-based Customer Relationship Management (CRM) system that allows you to manage customer information, accounts, cases, and updates. It provides a user-friendly interface for interacting with your CRM data and offers a RESTful API for programmatic access.

## Features

- **User Authentication**: Secure user authentication system with JWT-based access tokens.
- **Accounts Management**: Create, view, update, and delete customer accounts.
- **Cases Tracking**: Manage cases related to customer accounts.
- **Updates Logging**: Keep track of updates and activities associated with cases.
- **RESTful API**: Provides a comprehensive API for integrating CRMify with other systems.
- **Web Interface**: A user-friendly web interface for easy management of CRM data.
- **Bootstrap UI**: The web interface is built using Bootstrap for a responsive and modern design.
- **FastAPI Backend**: Powered by FastAPI, a high-performance web framework for Python.

## Installation

To run CRMify locally, follow these steps:

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/crmify.git
   cd crmify

2. Create a virtual environment and install dependencies:

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use venv\Scripts\activate
    pip install -r requirements.txt

3. Configure Environment Variables:

    Create a .env file in the project root directory and configure the following variables:

    ```env
    DATABASE_URL="mysql://your_username:your_password@your_database_host/your_database_name"
    SECRET_KEY="your_secret_key_here"

4. Run the FASTAPI server

    ```bash
    uvicorn main:app --host 0.0.0.0 --port 8001 --reload
