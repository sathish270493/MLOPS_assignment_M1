# MLOps CI/CD Pipeline

This project demonstrates the setup of a CI/CD pipeline for a simple machine learning project.

## Project Structure

## How to Run Locally
1. Clone the repository.
2. Install dependencies: pip install -r requirements.txt
3. Train the model: python src/model.py
4. Make predictions: python src/predict.py
5. Run tests: pytest src/tests

## CI/CD Pipeline
The pipeline includes:
- Linting with Flake8.
- Unit testing with Pytest.
- Triggered on push or pull requests to the main branch.