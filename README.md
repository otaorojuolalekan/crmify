<div align="center" text-decoration="underline">
 <strong>CRMify - Customer Relationship Management System</strong>
</div>
   <br>

<p align="center">
  <img src="https://github.com/otaorojuolalekan/crmify/assets/25134473/22d6b69d-7ba6-4db4-bad8-bdbff1512a69" alt="Image Description" />
</p>


<a href="http://crmify.onifemi.tech" target="_blank">CRMify</a> is a web-based Customer Relationship Management (CRM) system that allows you to manage customer information, accounts, cases, and updates. It provides a user-friendly interface for interacting with your CRM data and offers a RESTful API for programmatic access.

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
5. Access CRMify in your web browser at http://localhost:8001.

## Usage
- **API DOCUMENTATION**:
    CRMify provides interactive API documentation powered by Swagger UI. You can access it at http://localhost:8001/docs.

- **Web Interface**
- Open your web browser and go to http://localhost:8001.
- Log in with your credentials or create a new account.
- Use the web interface to manage accounts, cases, and updates.

## Suites Used
- ![image](https://github.com/otaorojuolalekan/crmify/assets/25134473/5bd6269f-b8b6-4627-b557-5f357fe72a41)
- ![image](https://github.com/otaorojuolalekan/crmify/assets/25134473/aa7cc0f4-5070-4fdb-95b5-733eac887dfa)
- ![image](https://github.com/otaorojuolalekan/crmify/assets/25134473/a5e0c9e8-da1f-4f44-8a7f-457f9664f951)
- ![image](https://github.com/otaorojuolalekan/crmify/assets/25134473/ca5635b5-6812-4617-a42b-7cdd45934647)

## Contributing
We welcome contributions! If you want to contribute to CRMify, please follow the guidelines in the CONTRIBUTING.md file.

## FUTURE DEVELOPMENT

The following is to be included in future versions of the CRMify application

## License
This project is licensed under the MIT License - see the LICENSE file for details.

```csharp
Copy code

You can copy and paste this content into your README.md file.



