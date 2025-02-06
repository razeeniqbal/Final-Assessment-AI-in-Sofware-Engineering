# AI House Price Prediction with CI/CD Pipeline

## Overview
This project implements a Continuous Integration and Continuous Deployment (CI/CD) pipeline for an AI component that predicts house prices. The machine learning model is trained on the "House Prices - Advanced Regression Techniques" dataset from Kaggle and deployed using Kubernetes with a Blue-Green deployment strategy.

## Architecture
The project uses a comprehensive DevOps pipeline with the following stages:
- Version Control (Git)
- Continuous Integration (Jenkins)
- Continuous Deployment (Kubernetes)
- Automated Testing
- Monitoring and Logging

### Blue-Green Deployment Strategy
The system implements a Blue-Green deployment strategy in Kubernetes, maintaining two identical environments:
- Blue: Current live environment
- Green: New environment for updates
This ensures minimal downtime and easy rollback capabilities.

## Tech Stack

### Core Technologies
- Python (AI/ML)
- Docker (Containerization)
- Kubernetes (Orchestration)
- Jenkins (CI/CD)

### Tools & Services
- **Version Control:** Git
- **CI/CD:** Jenkins
- **Containerization:** Docker
- **Orchestration:** Kubernetes, Helm
- **Testing:** JMeter
- **Monitoring:** 
  - Prometheus & Grafana (Metrics)
  - ELK Stack (Logging)
- **Code Quality:** SonarQube

## Getting Started

### Prerequisites
- Docker
- Kubernetes cluster
- Jenkins
- Git
- Python 3.8+

### Installation

1. Clone the repository:
```bash
git clone [repository-url]
cd [project-directory]
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Build Docker image:
```bash
docker build -t house-price-predictor .
```

4. Deploy to Kubernetes:
```bash
helm install house-price-predictor ./helm-charts
```

## Testing

The project includes comprehensive testing procedures:
- Unit Testing for individual components
- Integration Testing for pipeline validation
- Load Testing with JMeter (1000 concurrent users)
- Performance Testing for latency validation

### Performance Metrics
- Average Response Time: 200ms
- Throughput: 500 requests per second
- Prediction Latency: <50ms under load

## Monitoring

### Metrics Monitored
- Response times
- Error rates
- Resource utilization
- Model prediction latency
- System throughput

### Dashboards
- Grafana for real-time metrics visualization
- Kibana for log analysis
- Kubernetes dashboard for deployment status

## CI/CD Pipeline Stages

1. **Version Control**
   - Git-based version control
   - Rebasing policy for clean commit history
   - Feature branch workflow

2. **Continuous Integration**
   - Automated builds with Jenkins
   - Dependency installation
   - Unit testing
   - Static code analysis (SonarQube)

3. **Continuous Deployment**
   - Docker containerization
   - Kubernetes orchestration
   - Helm chart management
   - Blue-Green deployment strategy

4. **Testing**
   - Automated test suite execution
   - Load testing with JMeter
   - Performance validation

5. **Monitoring**
   - Real-time metrics collection
   - Centralized logging
   - Alert configuration
