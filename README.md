# 🚀 End-to-End MLOps Pipeline: Loan Risk Prediction

An enterprise-grade, fully automated Machine Learning Operations (MLOps) pipeline. This project trains a predictive model, containerizes the serving API, and deploys it to a production Kubernetes cluster via a Jenkins CI/CD pipeline.

## 🏗️ Architecture & Tech Stack
* **Machine Learning:** Scikit-Learn, Pandas
* **Experiment Tracking:** MLflow
* **API Framework:** FastAPI, Uvicorn
* **Database:** PostgreSQL
* **Containerization:** Docker
* **Cloud Infrastructure:** Google Cloud Platform (GCP)
* **Container Registry:** Google Artifact Registry
* **Orchestration:** Google Kubernetes Engine (GKE) Autopilot
* **CI/CD Automation:** Jenkins, GitHub Webhooks

---

## 🧠 Project Lifecycle Overview

1. **Model Training & Tracking:** Python scripts train the loan prediction model. MLflow tracks metrics (accuracy), parameters, and artifacts locally.
2. **Containerization:** The FastAPI application and model are packaged into a lightweight Docker image.
3. **Infrastructure Provisioning:** A highly available GKE Autopilot cluster is spun up in GCP (`asia-south1`).
4. **Continuous Integration/Continuous Deployment (CI/CD):** * Code pushed to GitHub triggers a Jenkins pipeline.
   * Jenkins checks out the code, builds the Docker image, and securely authenticates with GCP using direct access tokens.
   * The image is pushed to Google Artifact Registry.
   * Jenkins dynamically updates the Kubernetes `deployment.yaml` and applies the rollout to the GKE cluster with zero downtime.

---

## 🛠️ Step-by-Step Setup Guide (For Future Reference)

### 1. Local Development
Create a virtual environment and install dependencies:
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

