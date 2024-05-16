#!/bin/bash

# Create directory structure
mkdir -p backend/app/models
mkdir -p backend/app/routes
mkdir -p backend/app/services
mkdir -p backend/app/utils
mkdir -p backend/app/tests
mkdir -p frontend/public
mkdir -p frontend/src/components
mkdir -p frontend/src/routes
mkdir -p frontend/src/store
mkdir -p k8s
mkdir -p scripts
mkdir -p .github/workflows

# Create empty files for backend
touch backend/app/__init__.py
touch backend/app/main.py
touch backend/app/models/__init__.py
touch backend/app/models/models.py
touch backend/app/routes/__init__.py
touch backend/app/routes/api.py
touch backend/app/services/__init__.py
touch backend/app/services/service.py
touch backend/app/utils/__init__.py
touch backend/app/utils/utils.py
touch backend/app/tests/__init__.py
touch backend/app/tests/test_main.py
touch backend/app/tests/test_service.py
touch backend/Dockerfile
touch backend/requirements.txt
touch backend/README.md

# Create empty files for frontend
touch frontend/public/index.html
touch frontend/src/components/NavBar.svelte
touch frontend/src/components/Footer.svelte
touch frontend/src/routes/Home.svelte
touch frontend/src/routes/About.svelte
touch frontend/src/store/store.js
touch frontend/src/App.svelte
touch frontend/src/main.js
touch frontend/package.json
touch frontend/rollup.config.js
touch frontend/README.md

# Create empty files for Kubernetes configurations
touch k8s/deployment.yaml
touch k8s/service.yaml
touch k8s/ingress.yaml

# Create empty files for scripts
touch scripts/deploy.sh
touch scripts/init_db.py

# Create empty files for GitHub Actions workflows
touch .github/workflows/ci.yml
touch .github/workflows/cd.yml

# Create root files
touch .dockerignore
touch .gitignore
touch README.md

echo "Project structure created successfully."
