import pytest

"""
pytest -m smoke
pytest -m 'smoke or regression'

To run html report: pytest --html=my_name_for_report.html --self-contained-html
To run allure report: pytest --alluredir=allure_reports
allure serve 'absolute file path' #Only on mac?

How to ignore warnings: 
    pytest --disable-warnings #warnings don't print. All are disabled so not a good option
"""
pytestmark = pytest.mark.frontend
#pytest -m frontend



@pytest.mark.smoke
def test_login_page_valid_user():
    print("Login with valid user")

@pytest.mark.regression
@pytest.mark.smoke
def test_login_wrong_password():
    print("Login with wrong password")

