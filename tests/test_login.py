# Import our Page Object class
from pages.login_page import LoginPage 

def test_successful_login(page):
    """Tests successful login with valid credentials."""
    
    # !!! Important: Create your own account on demowebshop.tricentis.com
    # and replace these values with your valid credentials.
    VALID_EMAIL = "adrianpalicka@gmail.com"
    VALID_PASSWORD = "manchesterU1" 
    
    # 1. Initialize POM (prepare object to work with the current page)
    login_page = LoginPage(page)
    
    # 2. Actions
    login_page.navigate_to_login()
    login_page.login(VALID_EMAIL, VALID_PASSWORD) 
    
    # 3. Verification (Assertion)
    # Check if "Log out" link is visible after successful login
    assert login_page.logout_link.is_visible(), "The 'Log out' button did not appear after login."
