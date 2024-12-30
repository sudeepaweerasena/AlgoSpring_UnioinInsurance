import undetected_playwright as playwright
import re
import time


class Login:
    def __init__(self, page):
        self.page = page

    async def perform_login(self, username: str, password: str):
        await self.page.wait_for_load_state('networkidle')
        await self.page.goto('https://secure.unioninsurance.ae/Quotationtool/#/login?return=%2FSME')
        await self.page.wait_for_load_state('networkidle')

        # Enter login credentials
        await self.page.locator("#user_name_critical").fill(username)
        await self.page.locator("#password_critical").fill(password)      

        # Click sign-in button
        await self.page.get_by_role("button", name="Sign in roundarrowwhite").click()
        time.sleep(0.5)
    
