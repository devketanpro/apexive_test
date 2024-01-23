# Apexive Test

To adhere to Django's best practices, create a view that employs dynamic field serialization for a Django project featuring basic Author and Book models.

## Table of Contents
  - [Project Structure](#project_structure)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)


### Project Structure

The project focuses on maintaining a clear and organized structure, adhering to Django best practices. The Book model leverages custom queryset and manager classes, showcasing an extensible design for future enhancements. The ForeignKey relationship establishes a connection between authors and their respective books. Overall, the project is well-documented, providing usage examples for the custom queryset and manager methods.

### Prerequisites

List the software and tools that need to be installed before running the Dhango Project. Provide links to installation instructions if necessary.

- Python: [Installation Guide](https://www.python.org/downloads/)
- Django: [Installation Guide](https://www.djangoproject.com/download/)


### Installation

1. Clone this repository:

   ```bash
   git clone https://github.com/devketanpro/apexive_test
   ```

2. Checkout in to the branch:

   ```bash
   git checkout main
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

### Usage
1. Goto Project Directory
   ```bash
   cd apexive_test
   ```

2. Start the development server:

   ```bash
   python manage.py runserver
   ```

3. Access the application at 

   `http://localhost:8000/`



4. Use this book API (`http://localhost:8000/books/`) to perform book   related action.

5. Use this author API (`http://localhost:8000/author/`) to perform author related action.