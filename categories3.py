import asyncio
import time
import re

class Categories3:
    def __init__(self, page, df1, df3):
        self.page = page
        self.df1 = df1
        self.df3 = df3

    def get_value(self, column_name):
        try:
            # Fetch value from the specific column and convert to string
            return str(self.df3[column_name].values[2])
        except KeyError:
            print(f"KeyError: '{column_name}' column not found in DataFrame.")
            return None
        except IndexError:
            print(f"IndexError: No data found in column '{column_name}'.")
            return None

    async def categories3_information(self):
        # Network
        network = self.get_value("Network")
        print(network)
        await self.page.wait_for_load_state('networkidle')
        await asyncio.sleep(1)
        await self.page.locator("(//input[@type='text'])[14]").click()
        await self.page.locator("span").filter(has_text=network).nth(2).click()
        # await self.page.click(f'text="{network}"')
        await asyncio.sleep(3) 

        # Plan
        await self.page.click("(//input[contains(@type,'text')])[15]")
        await asyncio.sleep(1) 
        await self.page.wait_for_load_state('networkidle')
        await self.page.keyboard.press('ArrowDown')
        await self.page.keyboard.press('ArrowDown')
        await self.page.keyboard.press('Enter')
        await asyncio.sleep(3) 


        # Diagnostic Services*
        diagnostic_services = self.get_value("Co-payment on diagnostics")
        print(diagnostic_services)
        await asyncio.sleep(1)
        await self.page.click("(//input[contains(@type,'text')])[16]")
        await self.page.locator("#additional_general_offer0text2").get_by_role("list").get_by_text(diagnostic_services).click()
        #await self.page.click(f'text="{diagnostic_services}"')
        await asyncio.sleep(2) 
 

        # Pharmacy*
        pharmacy = self.get_value("Pharmacy")
        print(pharmacy)
        await asyncio.sleep(1)
        await self.page.click("(//input[contains(@type,'text')])[17]")   
        await self.page.locator(f"#additional_general_offer1text2").get_by_role("list").get_by_text(f"{pharmacy}").click()
        #await self.page.click(f'text="{pharmacy}"')
        await asyncio.sleep(2) 

        # Dental
        dental = self.get_value("Dental")
        print(dental)
        await asyncio.sleep(1)
        await self.page.click("(//input[contains(@type,'text')])[18]")
        await self.page.locator("#additional_general_offer2text2").get_by_role("list").get_by_text(dental).click()
        #await self.page.click(f'text="{dental}"')
        await asyncio.sleep(2)


        # Optical
        optical = self.get_value("Optical")
        print(optical)
        if optical == "Not Covered":
            await asyncio.sleep(1)
            await self.page.click("(//input[contains(@type,'text')])[19]")
            await self.page.locator("#additional_general_offer3text2").get_by_role("list").get_by_text("Not Covered").click()
            
        else:
            await asyncio.sleep(1)
            await self.page.click("(//input[contains(@type,'text')])[19]")
            await self.page.locator("#additional_general_offer3text2").get_by_role("list").get_by_text(optical).click() 
        await asyncio.sleep(2)


#        -------------------------gr-------------
        await self.page.get_by_text("Calculate").click()
        await asyncio.sleep(180)
        await self.page.get_by_role("button", name="Create Quote roundarrowwhite").click()
        await asyncio.sleep(30)
        await self.page.goto("https://secure.unioninsurance.ae/Quotationtool/#/groupplan/group_quotes")
        # Set the download path before initiating the download
        self.page.set_download_behavior(download_path="D:\\AlgoSpring\\python\\Union_Insurance")
        async with self.page.expect_download() as download_info:
            await self.page.get_by_role("link", name="Download Quote roundarrowwhite").click()
        download = await download_info.value
        return download