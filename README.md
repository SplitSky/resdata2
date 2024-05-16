# ResData

ResData is a comprehensive full-stack application designed to facilitate efficient data management and analysis for research groups. Built with FastAPI, MongoDB, Svelte, and Kubernetes, ResData aims to provide a robust and scalable solution for handling large datasets generated from lab equipment.

## Table of Contents

- [Features](#features)
- [Technology Stack](#technology-stack)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Usage](#usage)
- [Deployment](#deployment)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

## Features

- **Real-time Data Ingestion**: Stream data from lab equipment in real-time.
- **Secure Data Storage**: Store data efficiently using MongoDB with robust security measures.
- **User-friendly Interface**: Interact with your data through a modern Svelte-based frontend.
- **Scalability**: Deploy on-premises or scale effortlessly using Kubernetes on AWS.
- **Integration with Jupyter**: Seamlessly integrate Jupyter notebooks for advanced data analysis.
- **Continuous Development**: CI/CD pipelines to ensure continuous integration and deployment.

## Technology Stack

- **Backend**: FastAPI
- **Database**: MongoDB
- **Frontend**: Svelte
- **Containerization**: Docker
- **Orchestration**: Kubernetes
- **Cloud**: AWS

## Project Structure
resdata/
├── backend/
│ ├── app/
│ │ ├── init.py
│ │ ├── main.py
│ │ ├── models/
│ │ │ ├── init.py
│ │ │ └── models.py
│ │ ├── routes/
│ │ │ ├── init.py
│ │ │ └── api.py
│ │ ├── services/
│ │ │ ├── init.py
│ │ │ └── service.py
│ │ ├── utils/
│ │ │ ├── init.py
│ │ │ └── utils.py
│ │ └── tests/
│ │ ├── init.py
│ │ ├── test_main.py
│ │ └── test_service.py
│ ├── Dockerfile
│ ├── requirements.txt
│ └── README.md
├── frontend/
│ ├── public/
│ │ └── index.html
│ ├── src/
│ │ ├── components/
│ │ │ ├── NavBar.svelte
│ │ │ └── Footer.svelte
│ │ ├── routes/
│ │ │ ├── Home.svelte
│ │ │ └── About.svelte
│ │ ├── store/
│ │ │ └── store.js
│ │ ├── App.svelte
│ │ └── main.js
│ ├── package.json
│ ├── rollup.config.js
│ └── README.md
├── k8s/
│ ├── deployment.yaml
│ ├── service.yaml
│ └── ingress.yaml
├── scripts/
│ ├── deploy.sh
│ └── init_db.py
├── .github/
│ └── workflows/
│ ├── ci.yml
│ └── cd.yml
├── .dockerignore
├── .gitignore
└── README.md

## Installation

### Prerequisites

- Docker
- Kubernetes (kubectl)
- AWS CLI (if deploying to AWS)
- Python 3.9+
- Node.js

### Backend

1. Navigate to the backend directory:
   ```bash
   cd resdata/backend
Install the required dependencies:

bash

pip install -r requirements.txt

Run the FastAPI application:

bash

    uvicorn app.main:app --reload

Frontend

    Navigate to the frontend directory:

    bash

cd resdata/frontend

Install the required dependencies:

bash

npm install

Start the Svelte application:

bash

    npm run dev

Usage
Running the Application Locally

    Ensure both backend and frontend services are running.
    Access the frontend at http://localhost:5000 (or the port specified in your configuration).

API Endpoints

    GET /api/data: Fetch data
    POST /api/data: Upload data
    WebSocket /ws: Real-time data stream

Deployment
On-Premises

    Navigate to the scripts directory:

    bash

cd resdata/scripts

Run the deployment script:

bash

    bash deploy.sh

AWS Deployment with Kubernetes

    Ensure you have configured AWS CLI and kubectl.
    Update Kubernetes manifests in resdata/k8s.
    Apply the Kubernetes configuration:

    bash

    kubectl apply -f resdata/k8s/

Contributing

    Fork the repository.
    Create a new branch (git checkout -b feature/your-feature).
    Commit your changes (git commit -am 'Add some feature').
    Push to the branch (git push origin feature/your-feature).
    Create a new Pull Request.

License

This project is licensed under the MIT License. See the LICENSE file for details.
Contact

For more information, please contact:

    GitHub: SplitSky