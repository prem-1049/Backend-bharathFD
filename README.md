# FAQ Management System
## This is a Django-based FAQ management system that supports multi-language translations, a WYSIWYG editor for answers, and a REST API for managing FAQs. It also includes Redis-based caching for improved performance.

# Table of Contents
1. Installation

2. API Usage

3. Contribution Guidelines

# Installation
## Prerequisites
   Python 3.8 or higher
   Redis server (for caching)
   Git (optional)

#### Steps:
   # Clone the Repository:

      git clone https://github.com/prem-1049/Backend-bharathFD.git
      cd faq_project
   # Create a Virtual Environment:

      python -m venv venv
   # Activate the Virtual Environment:

      On Windows:
         venv\Scripts\activate
      On macOS/Linux:
         source venv/bin/activate
   # Install Dependencies:
      pip install -r requirements.txt

   # Set Up the Database:
      Run migrations to create the database tables:

         python manage.py migrate
   # Create a Superuser:
      Create an admin account to access the Django admin panel:

         python manage.py createsuperuser
   # Start the Development Server:

      python manage.py runserver
   # Access the Application:

      Admin Panel: http://127.0.0.1:8000/admin/

      API Endpoint: http://127.0.0.1:8000/api/faqs/

### API Usage
   The FAQ management system provides a REST API for fetching FAQs in multiple languages.

   # Fetch FAQs
      Endpoint: /api/faqs/

      Method: GET

      Query Parameters:
         lang: Language code (e.g., en, hi, bn). Defaults to en if not provided.

   # Examples
      1. Fetch FAQs in English (default):

      curl http://127.0.0.1:8000/api/faqs/
      2. Fetch FAQs in Hindi:

      curl http://127.0.0.1:8000/api/faqs/?lang=hi
      3. Fetch FAQs in Bengali:

      curl http://127.0.0.1:8000/api/faqs/?lang=bn
   # Response Format
      The API returns a JSON response with the following structure:

      [
         {
            "question": "What is Django?",
            "answer": "Django is a web framework."
         },
         {
            "question": "What is Redis?",
            "answer": "Redis is an in-memory data store."
         }
      ]
## Contribution Guidelines
   We welcome contributions! Please follow these guidelines to contribute to the project.

   ## Steps to Contribute
   # Fork the Repository:
      Click the "Fork" button on the top right of the repository page.

   # Clone Your Fork:
      git clone https://github.com/prem-1049/Backend-bharathFD.git
      cd faq_project
   # Create a New Branch:
      git checkout -b feature/your-feature-name
   # Make Changes:

      Make your changes and ensure the code follows PEP8 guidelines.
      Write unit tests for new features or bug fixes.

   # Commit Your Changes:
      Use clear and descriptive commit messages:
         git add .
         git commit -m "feat: Add multilingual FAQ model"
   # Push Your Changes:
          push origin feature/your-feature-name
   # Create a Pull Request:
      Go to the original repository and click "New Pull Request".
      Provide a detailed description of your changes.


Contact
For questions or feedback, please contact:

Your Name: premyandapalli11@gmail.com

GitHub: [prem-1049](https://github.com/prem-1049)

![image](https://github.com/user-attachments/assets/ceb376b9-fe41-4084-9612-7e16b7e187d4)

![image](https://github.com/user-attachments/assets/f2239859-939d-4510-b99f-606ba58472ab)

![image](https://github.com/user-attachments/assets/b058f10a-654d-4591-80a3-0fec02c4dc1d)

![image](https://github.com/user-attachments/assets/7d05bdba-504f-47a6-8986-638953d3b403)

![image](https://github.com/user-attachments/assets/87010e61-184a-4cc3-b4fe-48310f1125fb)

![image](https://github.com/user-attachments/assets/4516876d-0a8a-456e-b5ab-9b49c92585db)

![image](https://github.com/user-attachments/assets/cd8604e2-0289-455d-9793-5dc32fd5f7c6)






