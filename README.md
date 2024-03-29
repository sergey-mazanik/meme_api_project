# meme_api_project

Steps for testing:

1. Clone the project
2. Add .env file to root of the project
3. Add test_data.py file to root of the project
4. Create virtual environment (venv)
5. Install all libraries from requirement.txt
6. ```pytest -m before_testing``` run in terminal. This step need for checking alive token and override token if it died
7. ```pytest -v -m "not before_testing" --alluredir=allure-results``` run in terminal for start testing
8. ```allure serve``` run in terminal for watch allure report of the run

