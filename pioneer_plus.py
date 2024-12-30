import asyncio
import datetime
import time
import re
from categories1 import Categories1
from categories2 import Categories2
from categories3 import Categories3
from convert_excel import nlg_transfer_medical_data

class Pioneer_Plus:
    def __init__(self, page, df1, df2, df3):
        self.page = page
        self.df1 = df1
        self.df2 = df2
        self.df3 = df3

    def get_value(self, df, key):
        return df[df['KEY'] == key]['VALUE'].values[0]

# Category A
    def get_value_A(self, column_name):
        try:
            # Fetch value from the specific column and convert to string
            return str(self.df3[column_name].values[0])
        except KeyError:
            print(f"KeyError: '{column_name}' column not found in DataFrame.")
            return None
        except IndexError:
            print(f"IndexError: No data found in column '{column_name}'.")
            return None
        
# Category B
    def get_value_B(self, column_name):
        try:
            # Fetch value from the specific column and convert to string
            return str(self.df3[column_name].values[1])
        except KeyError:
            print(f"KeyError: '{column_name}' column not found in DataFrame.")
            return None
        except IndexError:
            print(f"IndexError: No data found in column '{column_name}'.")
            return None
        
# Category C
    def get_value_C(self, column_name):
        try:
            # Fetch value from the specific column and convert to string
            return str(self.df3[column_name].values[2])
        except KeyError:
            print(f"KeyError: '{column_name}' column not found in DataFrame.")
            return None
        except IndexError:
            print(f"IndexError: No data found in column '{column_name}'.")
            return None

    
    async def fill_poineer_plus_information(self, num_categories, unique_mapped_categories):
        nlg_transfer_medical_data()

        # Select "Customized Group Plan"
        await self.page.locator("div").filter(has_text=re.compile(r"^Range of different plans available across the UAE for SMEs\.CreateRetrieve$")).get_by_role("link").click()
        await asyncio.sleep(5)  

#----------------------------------------------Customer Details-------------------------------------------------
        emirates = self.get_value(self.df1,"Emirates")
        print(emirates)
        await self.page.wait_for_load_state('networkidle')
        await asyncio.sleep(3)
        await self.page.locator("//div[@class='row']//div[1]//div[1]//div[1]//div[1]//div[1]//input[1]").click()
        await self.page.locator(f"span:has-text('{emirates}')").click()
        await asyncio.sleep(0.5) 

        tpa = self.get_value_A("TPA")
        print(tpa)
        await self.page.wait_for_load_state('networkidle')
        await asyncio.sleep(1)
        await self.page.locator("//div[@class='plan_field squote_field']//div[2]//div[1]//div[1]//div[1]//div[1]//input[1]").click()
        await self.page.locator(f"span:has-text('{tpa}')").click()
        await asyncio.sleep(0.5) 

        # Click on the "Customer Information" button
        await self.page.get_by_role("button", name="Customer Information").click()
        await asyncio.sleep(2)  

        # Fill in the Company Name from Sheet1
        await self.page.locator('#sponser_name').fill(self.get_value(self.df1, "Company Name"))
        await asyncio.sleep(0.5)  

        # Fill in the Trade License Number from Sheet1
        emirates = self.get_value(self.df1,"Emirates")
        print(emirates)
        await self.page.wait_for_load_state('networkidle')
        await self.page.locator('//*[@id="ind_plan_form"]/div[1]/div/div/div[2]/div/div[1]/div[2]/div/div/div/div/input').click()
        await self.page.locator("span").filter(has_text=emirates).click()
        await asyncio.sleep(0.5)  

        await self.page.locator('#trade_no').fill(self.get_value(self.df1, "Trade License Number"))
        await asyncio.sleep(0.5)  

        await self.page.locator('#effective_date').fill(self.get_value(self.df1, "Trade License Expiry Date"))
        await asyncio.sleep(0.5)  
        await self.page.keyboard.press("Tab")

        await self.page.locator("#claim_up_field").set_input_files("D:\\AlgoSpring\\python\\Union_Insurance\\Standard Plans Template.xlsx")
        await asyncio.sleep(8)

        await self.page.wait_for_load_state('networkidle')
        await self.page.get_by_role("button", name="Plan selection roundarrowwhite").click()
        await asyncio.sleep(3)

# -------------------------------------Pioneer Plus / Pioneer Plus / Plan details-----------------------------------------
        tpa = self.get_value_A("TPA")
        print(tpa)
        await self.page.wait_for_load_state('networkidle')
        await asyncio.sleep(0.5)
        await self.page.locator('//*[@id="cutomized_group_plan_abudhabi"]/div[1]/div/div[2]/div/div/div/div/input').click()
        await self.page.locator(f"span:has-text('{tpa}')").click()
        await asyncio.sleep(3) 


  # Process categories based on unique categories in letters
        if 'A' in unique_mapped_categories:
            cat1 = self.df2[self.df2['Category'] == 1]
            categories1 = Categories1(self.page, self.df1, self.df3)
            await categories1.categories1_information()

        if 'B' in unique_mapped_categories:
            cat2 = self.df2[self.df2['Category'] == 2]
            categories2 = Categories2(self.page, self.df1, self.df3)
            await categories2.categories2_information()

        if 'C' in unique_mapped_categories:
            cat3 = self.df2[self.df2['Category'] == 3]
            categories3 = Categories3(self.page, self.df1, self.df3)
            await categories3.categories3_information()

       
      