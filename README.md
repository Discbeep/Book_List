
# Book_List: A Flask Application

Flask-based web application that displays a list of ten books fetched from the Open Library API. This application demonstrates basic Flask functionality such as routing, template rendering, and making API calls. 


## Visit Site
https://book-list-512n.onrender.com)
## Features
 **List Display:** Shows a list of the first ten books based on a predefined query from the Open Library API.
 
**Book Details:** Each book title is clickable and leads to a detailed view of the book.
## Prerequisites
Ensure you have the following installed on your system before you begin:
- Python 3.6 or higher
- pip (Python package installer)
- Git (Version control system)
- VScode (I used GitPod)

## Getting Started
## Clone the Repository
Clone the repository to your local machine to get started with Book_List:
```sh
git clone https://github.com/Discbeep/Book_List.git
cd Book_List
## Set Up a Virtual Environment 
It is recommended to use a virtual environment to manage the project's dependencies separately:
python -m venv my_virtualenv

## Activate the Virtual Environment
**On Mac OS/Linux**
source my_virtualenv/bin/activate
**On Windows**
my_virtualenv\Scripts\activate

## Install Dependencies
Install all required packages using pip:
pip install -r requirements.txt

## Run the Application
Run the application on your local machine with the following command:
**python app.py**
This starts a local server. Open your web browser and go to http://localhost:8080 to view the application.

## Usage in GitPod
python app.py

## Ensure gunicorn is installed:
pip install gunicorn


## Update requirements.txt:
pip freeze > requirements.txt

## wsgi file
Create a wsgi.py file:

## Commit and push changes to GitHub:
git add requirements.txt wsgi.py
git commit -m "Added Gunicorn and wsgi configuration for Render deployment"
git push origin main  # Replace 'main' with your branch name if different

## Deployment
Deploy to https://render.com:
Create a new web service on Render.
Connect your GitHub repository.
Set the build command to pip install -r requirements.txt.
Set the start command to gunicorn wsgi:app.

## Troubleshooting
Issues with virtual environment creation and activation:
- Check the structure of the virtual environment:
- ls my_virtualenv
_The output should contain bin, include, lib, pyvenv.cfg._

Once the virtual environment is activated, run:
pip install -r requirements.txt
pip install gunicorn  # If not already installed
pip freeze > requirements.txt


## Contributing
Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.
