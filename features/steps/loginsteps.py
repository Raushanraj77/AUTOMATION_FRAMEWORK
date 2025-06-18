from behave import *
from configuration.config import TestData
from pages.LoginPage import LoginPage
from pages.DashboardPage import DashboardPage





# @given(u'Launch the browser')
# def launch_browser(context):
#     if TestData.BROWSER == 'chrome':
#         service = Service(ChromeDriverManager().install())
#         context.driver = webdriver.Chrome(service=service)
#         #context.driver = webdriver.Chrome(executable_path=TestData.CHROME_EXECUTABLE_PATH)
#     elif TestData.BROWSER == 'firefox':
#         service = Service(ChromeDriverManager().install())
#         Service
#         context.driver = webdriver.Chrome(service=service)
#         #context.driver = webdriver.Firefox(executable_path=TestData.FIREFOX_EXECUTABLE_PATH)
#     else:
#         raise ValueError('Browser is not supported')



@when(u'Open the url')
def open_login_page(context):
    try:
        context.driver.get(TestData.URL)
        context.loginPage = LoginPage(context.driver)
        context.dashboardpage = DashboardPage(context.driver)
        
    except:        
        assert False,"Test is failed in open login page section"

@then(u'The login portal has been opened')
def validate_login_page(context):
    try:        
        context.loginPage.validateTitle()
    except:        
        assert False, "Test is failed in validate login page title"

@given(u'Provide the username and password')
def enter_login_creds(context):
    try:                 
        context.loginPage.enter_username(TestData.USERNAME.strip())
        context.loginPage.enter_password(TestData.PASSWORD.strip())           
    except Exception as e:
        print(f"Login creential entry failed: {e}")      
        assert False, "Test failed while entering login credentials"

@given(u'Provide the username "{user}" and password "{pwd}"')
def enter_login_creds(context, user, pwd):
    try:        
        context.loginPage.enter_username(user)
        context.loginPage.enter_password(pwd)  
        #context.loginPage.enter_login_credentials(user,pwd)
    except:        
        assert False, "Test is failed in enter login credentials"

@when(u'Click on the Login button')
def enter_login(context):
    try:
        context.loginPage.enter_login()
    except:        
        assert False, "Test is failed in enter login"


@then(u'Login is successful and dashboard is opened')
def validate_dashboard_page(context):
    try:
        context.dashboardpage.validatePageLoaded()
    except:        
        assert False, "Test is failed in validating dashboard"

@then(u'Login is failed and invlid credential error is displayed')
def validate_invalid_login(context):
    try:
        context.loginPage.validateInvalidCreds()
    except:        
        assert False, "Test is failed in validating invalid login"

@given(u'Provide the password "{pwd}"')
def enter_login_creds(context, pwd):
    try:
        context.loginPage.enter_password(pwd)
    except:        
        assert False, "Test is failed in enter password"

@given(u'Provide the username "{user}"')
def enter_login_creds(context, user):
    try:
        context.loginPage.enter_username(user)
    except:        
        assert False, "Test is failed in enter username"

@then(u'Login is failed and empty username error is displayed')
def validate_empty_username(context):
    try:
        context.loginPage.validateEmptyUsername()
    except:        
        assert False, "Test is failed in validate empty username"

@then(u'Login is failed and empty password error is displayed')
def validate_empty_passeword(context):
    try:
        context.loginPage.validateEmptyPassword()
    except:        
        assert False, "Test is failed in validate empty password"



@then(u'Close the browser')
def step_impl(context):
    context.driver.close()