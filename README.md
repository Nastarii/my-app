# Streamlit + FastAPI + MySQL Stack in Docker

This project is a web application built using **Streamlit**, **FastAPI**, and **MySQL**, all orchestrated with **Docker**. It leverages an ORM for database management and migrations using **Alembic**.

## Features

- **Streamlit**: Interactive web interface for data visualization and user interaction.  
- **FastAPI**: Backend API for handling business logic and serving data.  
- **MySQL**: Relational database for data storage.  
- **Alembic**: Database migrations and schema management using an ORM.  
- **Docker**: Containerized environment for easy deployment and scalability.

## Technology Versions

- **Streamlit**: `1.25.0`  
- **FastAPI**: `0.103.1`  
- **MySQL**: `8.0`  
- **Alembic**: `1.12.0`  
- **Docker**: `24.0.6`

## Getting Started

### Prerequisites

- Install [Docker](https://www.docker.com/).
- Clone this repository:
    ```bash
    git clone https://github.com/your-username/your-repo.git
    cd your-repo
    ```

### Running the Application

1. Build and start the Docker containers:
     ```bash
     docker-compose up --build
     ```

2. Access the Streamlit app at `http://localhost:8501`.  
     The FastAPI docs are available at `http://localhost:8000/docs`.

### Database Migrations

This project uses **Alembic** for database migrations. To create and apply migrations:

1. Generate a new migration:
     ```bash
     alembic revision --autogenerate -m "Migration message"
     ```

2. Apply the migration:
     ```bash
     alembic upgrade head
     ```

## Folder Structure

```
my-app/
├── server/             # FastAPI application
├── server/db           # Alembic migrations
├── client/             # Streamlit application
├── docker-compose.yml  # Docker configuration
└── README.md           # Project documentation
```

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.