**Project Name**

Resume Analyser

**Description**

This Flask application is designed to extract and parse information from uploaded resumes using OpenAI's GPT-3.5-turbo model. It leverages the following functionalities:

  - **PDF Text Extraction:** Extracts text content from uploaded PDF resumes using the PyPDF2 library.
  - **OpenAI Integration:** Uses the OpenAI API to parse the extracted text and identify key information like name, phone number, email, experience, education, skills, and social links.
  - **Database Storage:** Stores the parsed data in a SQLite database for easier retrieval and management.
  - **Web Interface:** Provides a user interface for uploading resumes, viewing parsed data, and listing all resumes in the database.

**Getting Started**

1.  **Prerequisites:**
      - Python 3.x
      - Flask
      - SQLAlchemy
      - PyPDF2
      - OpenAI API Key (Obtain a key from [https://beta.openai.com/account/api-keys](https://www.google.com/url?sa=E&source=gmail&q=https://beta.openai.com/account/api-keys))
2.  **Installation:**
      - Clone this repository or download the code.
      - Create a virtual environment (recommended):
        ```bash
        python -m venv venv
        source venv/bin/activate  # Windows: venv\Scripts\activate
        ```
      - Install dependencies:
        ```bash
        pip install -r requirements.txt
        ```
3.  **Configuration:**
      - Set your OpenAI API key in the `api_key` variable within the application code.
      - (Optional) Modify `app.config['UPLOAD_FOLDER']` if you want to change the upload directory for resumes.
4.  **Database Creation:**
      - Run the application to automatically create the database tables:
        ```bash
        python app.py
        ```
5.  **Usage:**
      - Access the application in your web browser, typically at `http://127.0.0.1:5000/` (default port).
      - Upload your resume in PDF format.
      - The parsed data will be displayed on a results page.
      - You can also view a list of all resumes and their details through the provided routes.

**Features**

  - Resume upload and parsing
  - Viewing parsed data (name, phone number, email, experience, education, skills, social links)
  - Extracts the important Data which can be later matched with requirements to filter out resumes
  - Listing all stored resumes
**License**
- This Project Uses Apache 2.0 License
**Additional Notes**

  - The accuracy of the parsing depends on the quality of the uploaded PDF and the OpenAI model's capabilities.
  - Consider potential limitations of the OpenAI API, such as usage quotas and potential costs.
  - Explore advanced features like error handling, user authentication, and deployment options for production environments.

