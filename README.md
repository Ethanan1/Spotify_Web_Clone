# Real Estate Web Application

This is a web application built using Flask, React, and Python for managing rental payments, maintenance requests, and lease agreements in the real estate domain.

## Features

- User authentication: Property managers and tenants can create accounts and log in to access relevant information.
- Rental payment tracking: Property managers can record and track rental payments, including due dates, amounts, and payment statuses.
- Maintenance request management: Property managers can receive, assign, and track maintenance requests from tenants, with status updates and communication capabilities.
- Lease agreement management: Central repository for managing lease agreements, including document uploads, renewal reminders, and expiration notifications.
- Dashboard and reports: Display relevant data and generate reports to provide property managers with an overview of rental activities and financial information.

## Technologies Used

- Flask: A micro web framework in Python for building the backend API.
- React: A JavaScript library for building the frontend user interface.
- Python: The programming language used for server-side logic.
- HTML/CSS: Markup and styling languages for building web pages.
- SQLite: A lightweight, file-based database used for development. (You can switch to a more robust database like PostgreSQL for production deployment.)

## Getting Started

### Prerequisites

- Python 3.8 or higher
- Node.js and npm (Node Package Manager)

### Installation

1. Clone the repository:

```bash
git clone https://github.com/your-username/your-repo.git
```

2. Set up the backend:
   - Open a terminal and navigate to the backend directory:
     ```
     cd real-estate-backend
     ```
   - Create a virtual environment:
     ```
     python -m venv venv
     ```
   - Activate the virtual environment:
     - Windows:
       ```
       venv\Scripts\activate
       ```
     - macOS/Linux:
       ```
       source venv/bin/activate
       ```
   - Install dependencies:
     ```
     pip install -r requirements.txt
     ```
   - Run the Flask server:
     ```
     python app.py
     ```

3. Set up the frontend:
   - Open a new terminal and navigate to the frontend directory:
     ```
     cd real-estate-frontend
     ```
   - Install dependencies:
     ```
     npm install
     ```
   - Start the development server:
     ```
     npm start
     ```

4. Open your browser and visit http://localhost:3000 to see the application running.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
