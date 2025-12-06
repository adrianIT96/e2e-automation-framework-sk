from playwright.sync_api import Page, Locator

class LoginPage:
    
    def __init__(self, page: Page):
        self.page = page
        # A. Selectors (Locators)
        self.email_input: Locator = page.locator("#Email")
        self.password_input: Locator = page.locator("#Password")
        self.login_button: Locator = page.locator(".login-button")
        self.logout_link: Locator = page.locator(".ico-logout")
        self.login_link: Locator = page.locator(".ico-login")
        self.error_message: Locator = page.locator(".validation-summary-errors")

    # B. Methods (Actions)
    def navigate_to_login(self):
        """Navigates directly to the login page."""
        self.page.goto("https://demowebshop.tricentis.com/login")
        
    def login(self, email, password):
        """Performs login action on the page."""
        self.email_input.fill(email)
        self.password_input.fill(password)
        self.login_button.click()
        # NOVÝ RIADOK: Explicitné čakanie na zobrazenie Log out
        # Hovoríme Playwrightu: "Počkaj maximálne 5 sekúnd, kým sa objaví tento element."
        self.logout_link.wait_for(state="visible", timeout=5000) 
        # Poznámka: timeout je v milisekundách (5000ms = 5s)
        
    def is_logged_out(self) -> bool:
        """Helper method to check if the login link is visible."""
        return self.login_link.is_visible()
