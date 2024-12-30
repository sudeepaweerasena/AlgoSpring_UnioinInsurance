import asyncio
import time
import re

class Custom_Categories1:
    def __init__(self, page,df1, df3, df4):
        self.page = page
        self.df1 = df1
        self.df3 = df3
        self.df4 = df4

    def get_value(self, column_name):
        try:
            # Fetch value from the specific column and convert to string
            return str(self.df4[column_name].values[0])
        except KeyError:
            print(f"KeyError: '{column_name}' column not found in DataFrame.")
            return None
        except IndexError:
            print(f"IndexError: No data found in column '{column_name}'.")
            return None

    async def custom_categories1_information(self):
        # Network
        network = self.get_value("Network")
        print(network)
        await self.page.wait_for_load_state('networkidle')
        await asyncio.sleep(1)
        await self.page.click("(//input[contains(@type,'text')])[1]")
        await self.page.click(f'text="{network}"')
        await asyncio.sleep(3) 

        # Annual Limit
        annual_limit = self.get_value("Annual Limit")
        await asyncio.sleep(0.5)
        annual_limit = int(float(annual_limit))  # Convert to float first, then to int
        annual_limit_formatted = f"{annual_limit:,}"
        await asyncio.sleep(0.5)
        await self.page.click("(//input[contains(@type,'text')])[2]")
        await self.page.click(f'text="{annual_limit_formatted}"')


        # Territory
        territory = self.get_value("Territory")
        print(territory)
        await asyncio.sleep(1)
        await self.page.click("(//input[contains(@type,'text')])[3]")
        await self.page.click(f'text="{territory}"')
        await asyncio.sleep(3) 

        # IP & OP
        await self.page.get_by_text("IP & OP").first.click()
        await asyncio.sleep(1) 

#------------------------------------------------
  

        # Pre-existing Condition
        pre_existing = self.get_value("Pre-existing")
        print(pre_existing)
        await asyncio.sleep(1)
        await self.page.click("(//input[contains(@type,'text')])[4]")
        await self.page.click(f'text="{pre_existing}"')
        await asyncio.sleep(3) 

        # Semi Private Room
        semi_private_room = self.get_value("Semi Private Room")
        print(semi_private_room)
        if semi_private_room == "Covered":
            await self.page.locator("#coinsurance_general_offer0text0").get_by_text("Applicable").click()
        else:
            print("Not Covered")
        await asyncio.sleep(1)

        # Consultation
        consultation = self.get_value("Consultation")
        print(consultation)
        consultation_type = type(consultation)
        if consultation_type == float:
            await asyncio.sleep(1)
            consultation = int(float(consultation) * 100)
            consultation = f"{consultation}%"
            await self.page.click("(//input[contains(@type,'text')])[5]")
            await self.page.click(f'text="{consultation}"')
        else:
            await asyncio.sleep(1)
            await self.page.click("(//input[contains(@type,'text')])[5]")
            await self.page.click(f'text="{consultation}"')
        await asyncio.sleep(3) 

        # OP Coinsurance
        op_coInsurance = self.get_value("Op Co Insurance")
        print(op_coInsurance)
        if op_coInsurance == "Nil":
            await self.page.click("(//input[contains(@type,'text')])[6]")
            await asyncio.sleep(1)
            await self.page.locator("#coinsurance_general_offer1text0").get_by_role("list").get_by_text("Nil").click()
        else:
            op_coInsurance = int(float(op_coInsurance) * 100)
            op_coInsurance = f"{op_coInsurance}%"
            await asyncio.sleep(1)
            await self.page.click("(//input[contains(@type,'text')])[6]")
            await self.page.click(f'text="{op_coInsurance}"')
        await asyncio.sleep(3)

        # Maternity
        maternity = self.get_value("Maternity")
        print(maternity)
        await asyncio.sleep(1)
        if maternity == "OpenLimit":
            await self.page.click("(//input[contains(@type,'text')])[7]")
            await asyncio.sleep(0.5)
            await self.page.locator("#additional_general_offer0text0").get_by_role("list").get_by_text("OpenLimit").click()
        else:
            maternity = int(float(maternity))
            maternity_formatted = f"{maternity:,}"
            await asyncio.sleep(0.5)
            await self.page.click("(//input[contains(@type,'text')])[7]")
            await self.page.click(f'text="{maternity_formatted}"')
            await asyncio.sleep(3) 

        # Preventive Services, Vaccines and Immunizations
        await self.page.locator(".offerrep > .offer > .custom_checkbox > label > span").first.click()
        await asyncio.sleep(0.5) 

        # Work Related Accident
        if self.get_value("Work Related Accident") == "Covered":
            await self.page.locator("div:nth-child(3) > .offerrep > .offer > .custom_checkbox > label > span").first.click()
        else:
            print("Not Covered")
        await asyncio.sleep(0.5) 

        # Congenital
        if self.get_value("Congenital") == "Covered":
            # await self.page.locator("div:nth-child(4) > .offerrep > .offer > .custom_checkbox > label > span").first.click()
            await self.page.locator("div:nth-child(4) > .offerrep > .offer > .custom_checkbox > label > span").first.click()
        else:
            print("Not Covered")
        await asyncio.sleep(0.5) 

        # Alternative Treatment
        alt_treatment = self.get_value("Alternative Medicine")
        print(alt_treatment)
        await asyncio.sleep(0.5)
        alt_treatment = int(float(alt_treatment))
        alt_treatment = f"{alt_treatment:,}"
        await asyncio.sleep(0.5)
        await self.page.click("(//input[contains(@type,'text')])[8]")
        await self.page.click(f'text="{alt_treatment}"')
        await asyncio.sleep(0.5)

        # Psychiatric Treatment
        psy_treatment = self.get_value("Psychiatric Treatment")
        print(psy_treatment)
        await asyncio.sleep(0.5)
        psy_treatment = int(float(psy_treatment))
        psy_treatment = f"{psy_treatment:,}"  # Format with commas
        await asyncio.sleep(0.5)
        await self.page.click("(//input[@type='text'])[9]")
        await self.page.locator("#additional_general_offer0text0").get_by_role("list").get_by_text(psy_treatment).click()

        # Repatriation
        repatriation = self.get_value("Repatriation of Mortal remains")
        print(repatriation)
        await asyncio.sleep(0.5)
        repatriation = int(float(repatriation))
        repatriation_formatted = f"{repatriation:,}"  
        await asyncio.sleep(0.5)
        await self.page.wait_for_load_state('networkidle')
        await self.page.click("(//input[@type='text'])[10]")
        await asyncio.sleep(1)
        await self.page.wait_for_load_state('networkidle')
        await self.page.click(f'text="{repatriation_formatted}"')

        # Dental
        dental = self.get_value("Dental")
        dental = int(float(dental) * 100) 
        dental_formatted = f"{dental}%" 
        print(dental_formatted)
        await self.page.locator("(//input[contains(@type,'text')])[11]").first.click()
        await self.page.locator(f"#additional_general_offer0text0 span:text('{dental_formatted}')").click()
        await asyncio.sleep(5)     
        
        # Dental Limit ---Sub Field---
        dental_limit = self.get_value("Dental Limit")
        print(dental_limit)
        await asyncio.sleep(0.5)
        dental_limit = int(float(dental_limit.replace(',', '')))
        dental_limit_formatted = f"{dental_limit:,}"
        await asyncio.sleep(0.5)
        await self.page.keyboard.press('Tab')
        await self.page.keyboard.press('Enter')
        await asyncio.sleep(0.5)
        # await self.page.click("(//input[contains(@type,'text')])[12]")
        await self.page.locator("#additional_general_offer0text0").get_by_role("list").get_by_text(dental_limit_formatted).click()

        # Optical
        optical = self.get_value("Optical")
        print(optical)
        optical = int(float(optical) * 100)
        optical = f"{optical}%"
        await asyncio.sleep(1)
        await self.page.click("(//input[contains(@type,'text')])[14]")
        await self.page.locator("#additional_general_offer0text0").get_by_role("list").get_by_text(optical).click()
        await asyncio.sleep(3)

        # Optical Limit ---Sub Field---
        optical_limit = self.get_value("Optical Limit")
        print(optical_limit)
        await asyncio.sleep(0.5)
        optical_limit = int(float(optical_limit))
        optical_limit_formatted = f"{optical_limit:,}"  # Format with commas
        await asyncio.sleep(0.5)
        await self.page.click("(//input[contains(@type,'text')])[15]")
        await self.page.locator("#additional_general_offer0text0").get_by_role("list").get_by_text(optical_limit_formatted).click()


        # Preventive Screening
        if self.get_value("Preventive Screening") == "Covered":
            await self.page.locator("div:nth-child(10) > .offerrep > .offer > .custom_checkbox > label > span").first.click()
        else:
            print("Not Covered")
        #await self.page.locator("div:nth-child(10) > .offerrep > .offer > .custom_checkbox > label > span").first.click()      
        await asyncio.sleep(1)

        # Routine Check-up
        if self.get_value("Routine Check-up") == "Covered":
            await self.page.locator("div:nth-child(11) > .offerrep > .offer > .custom_checkbox > label > span").first.click()
        else:
            print("Not Covered")
        # await self.page.locator("div:nth-child(11) > .offerrep > .offer > .custom_checkbox > label > span").first.click()
        await asyncio.sleep(1)

        # Nursing at Home
        if self.get_value("Nursing at Home") == "Covered":
            await self.page.locator("div:nth-child(12) > .offerrep > .offer > .custom_checkbox > label > span").first.click()
        else:
            print("Not Covered")
        # await self.page.locator("div:nth-child(12) > .offerrep > .offer > .custom_checkbox > label > span").first.click()
        await asyncio.sleep(1)

        # Child Vaccination
        if self.get_value("Child Vaccination") == "Covered":
            await self.page.locator("#additional_general_offer1text0").get_by_text("Applicable").click()
        else:    
            print("Not Covered")
        # await self.page.locator("#additional_general_offer1text0").get_by_text("Applicable").click()
        await asyncio.sleep(1)


        # Infertility Cover
        infertility_cover = self.get_value("Infertility Cover")
        print(infertility_cover)
        await asyncio.sleep(0.5)
        infertility_cover = int(float(infertility_cover))
        infertility_cover_formatted = f"{infertility_cover:,}"
        await asyncio.sleep(0.5)
        await self.page.click("(//input[contains(@type,'text')])[16]")
        await self.page.locator("#additional_general_offer1text0").get_by_role("list").get_by_text(infertility_cover_formatted).click()
