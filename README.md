Book_List: A Flask Application
Booksy is a Flask-based web application that displays a list of ten books fetched from the Open Library API. This application demonstrates basic Flask functionality such as routing, template rendering, and making API calls. Visit the live site:https://book-list-512n.onrender.com

Writing code directly in GitPod https://www.gitpod.io/docs/introduction/getting-started and deployment done on https://render.com/

render was completely free, no credit card required.


Features

List Display: Shows a list of the first ten books based on a predefined query from the Open Library API. Book Details: Each book title is clickable and leads to a detailed view of the book. Prerequisites Ensure you have the following installed on your system before you begin:

Python 3.6 or higher

pip (Python package installer)

Git (Version control system)

render.com


Getting Started

Clone the Repository Clone the repository to your local machine to get started with Book_List:

git clone https://github.com/Discbeep/Book_List.git cd Book_list

Set Up a Virtual Environment It is recommended to use a virtual environment to manage the project's dependencies separately:

python -m venv my_virtualenv

Activate the virtual environment

source my_virtualenv/bin/activate# On macOS and Linux venv\Scripts\activate # On Windows Install Dependencies Install all required packages using pip:

pip install -r requirements.txt 

Run the application on your local machine with the following command: python app.py **This starts a local server**..

In GitPod:
python app.py, select browser or preview

Push changes to GitHub if you made any changes to your program

Git add .
git commit -m "Updated requirements.txt with current package versions"
git push origin main  # Replace 'main' with your branch name if different


Troubleshoot:
issues with virtual environment creation and activation
check the structure of the venv:
ls my_virtualenv (Output should contain bin, include, lib, pyvenv.cfg)

Once Venv is activated, run the cmmands below

pip install -r requirements.txt
pip install gunicorn  # If not already installed
pip freeze > requirements.txt

git add requirements.txt
git commit -m "Updated requirements.txt with current package versions"
git push origin main  # Replace 'main' with your branch name if different

