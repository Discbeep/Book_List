# Book_List: A Flask Application

**Book_List** is a Flask-based web application that displays a list of ten books fetched from the Open Library API. This application demonstrates basic Flask functionality such as routing, template rendering, and making API calls. 

Visit the live site: [Book_List on Render](https://book-list-512n.onrender.com)

## Table of Contents
- [Features](#features)
- [Prerequisites](#prerequisites)
- [Getting Started](#getting-started)
  - [Clone the Repository](#clone-the-repository)
  - [Set Up a Virtual Environment](#set-up-a-virtual-environment)
  - [Activate the Virtual Environment](#activate-the-virtual-environment)
  - [Install Dependencies](#install-dependencies)
  - [Run the Application](#run-the-application)
- [Usage in GitPod](#usage-in-gitpod)
- [Deployment](#deployment)
  - [Render Deployment](#render-deployment)
- [Troubleshooting](#troubleshooting)
- [Contributing](#contributing)


## Features
- **List Display:** Shows a list of the first ten books based on a predefined query from the Open Library API.
- **Book Details:** Each book title is clickable and leads to a detailed view of the book.

## Prerequisites
Ensure you have the following installed on your system before you begin:
- Python 3.6 or higher
- pip (Python package installer)
- Git (Version control system)

## Getting Started

### Clone the Repository
Clone the repository to your local machine to get started with Book_List:
```sh
git clone https://github.com/Discbeep/Book_List.git
cd Book_List
### Set Up a Virtual Environment 
It is recommended to use a virtual environment to manage the project's dependencies separately:

python -m venv my_virtualenv

### Activate the Virtual Environment
On Mac OS/Linux
source my_virtualenv/bin/activate
On Windows
my_virtualenv\Scripts\activate

### Install Dependencies

Install all required packages using pip:
pip install -r requirements.txt

### Run the Application

Run the application on your local machine with the following command:
python app.py
This starts a local server. Open your web browser and go to http://localhost:8080 to view the application.

## Usage in GitPod

In GitPod, run:


python app.py

Select browser or preview to view the application.
Deployment
Render Deployment

### Ensure gunicorn is installed:

pip install gunicorn

Update requirements.txt:


pip freeze > requirements.txt

Create a wsgi.py file:

python

from app import app

if __name__ == "__main__":
    app.run()

Commit and push changes to GitHub:


git add requirements.txt wsgi.py
git commit -m "Added Gunicorn and wsgi configuration for Render deployment"
git push origin main  # Replace 'main' with your branch name if different

## Deployment
Deploy to Render:
Create a new web service on Render.
Connect your GitHub repository.
Set the build command to pip install -r requirements.txt.
Set the start command to gunicorn wsgi:app.

Troubleshooting

Issues with virtual environment creation and activation:
Check the structure of the virtual environment:


ls my_virtualenv

The output should contain bin, include, lib, pyvenv.cfg.

Once the virtual environment is activated, run:


pip install -r requirements.txt
pip install gunicorn  # If not already installed
pip freeze > requirements.txt

Commit and push changes to GitHub:



git add requirements.txt
git commit -m "Updated requirements.txt with current package versions"
git push origin main  # Replace 'main' with your branch name if different

Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.
