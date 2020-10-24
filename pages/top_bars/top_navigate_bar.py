from pages.basepage import BasePage
import allure


class TopNavigateBar(BasePage):
    """ Top navigation bar - the bar that appears at the top of the page after login"""

    def __init__(self):
        super().__init__()
        self.projects_btn = "[href='https://app.involve.me/projects']"
        self.templates_btn = "[href='https://app.involve.me/templates']"
        self.analytics_btn = "[href='https://app.involve.me/analytics']"
        self.integrations_btn = "[href='https://app.involve.me/integrations']"
        self.affiliate_program_btn = "[href='https://app.involve.me/affiliate']"
        self.account_drop_down_menu = "#nav-dropdown"
        self.logout_btn = "[href='https://app.involve.me/logout']"

    @allure.step("Click Projects tab")
    def click_projects(self):
        self._click(self.projects_btn)

    @allure.step("Click Templates tab")
    def click_templates(self):
        self._click(self.templates_btn)

    @allure.step("Click Analytics tab")
    def click_analytics(self):
        self._click(self.analytics_btn)

    @allure.step("Click Integrations tab")
    def click_integrations(self):
        self._click(self.integrations_btn)

    @allure.step("Click Affiliate Program tab")
    def click_affiliate_program(self):
        self._click(self.affiliate_program_btn)

    @allure.step("Logout from system")
    def logout(self):
        # Click account drop down menu
        self._click(self.account_drop_down_menu)
        # Click logout button
        self._click(self.logout_btn)
