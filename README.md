# Flask + Express Deployment on Kubernetes (Minikube)

## 📌 Objective

Deploy a Flask frontend and Express backend on a Kubernetes cluster using Minikube (locally).

---

## 🛠 Technologies Used

- Flask (Python)
- Express (Node.js)
- Docker
- Kubernetes
- Minikube
- GitHub

---

## 📁 Project Structure

project-root/
├── flask-frontend/
│ ├── app.py
│ ├── requirements.txt
│ └── Dockerfile
├── express-backend/
│ ├── index.js
│ ├── package.json
│ └── Dockerfile
├── k8s/
│ ├── flask-deployment.yaml
│ ├── flask-service.yaml
│ ├── express-deployment.yaml
│ ├── express-service.yaml
└── README.md



1. Created Flask and Express apps
2. Dockerized both apps with Dockerfiles
3. Built Docker images and tagged them
4. Pushed images to Docker Hub (or used them locally with Minikube)
5. Wrote Kubernetes YAML files for deployments and services
6. Deployed using `kubectl apply -f <file>.yaml`
7. Exposed Flask frontend with NodePort
8. Verified with browser and `kubectl get` commands


## ✅ Deployment Verification

- `kubectl get pods`
- `kubectl get svc`
- `kubectl get deployments`
- Browser shows Flask frontend calling Express backend


## 📸 Screenshots

(Screenshots included in `screenshots/` folder)

1. Running pods
2. Services
3. Flask app in browser





