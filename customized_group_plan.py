import asyncio
import datetime
import time
import re
from custom_categories1 import Custom_Categories1
from custom_categories2 import Custom_Categories2
from custom_categories3 import Custom_Categories3
from convert_excel import nlg_transfer_medical_data
# import yaml

# # Load the configuration file
# def load_config():
#     with open('config.yaml', 'r') as file:
#         config = yaml.safe_load(file)
#     return config


# config = load_config()

class Customized_Group_Plan:
    def __init__(self, page, df1, df2, df3, df4):
        self.page = page
        self.df1 = df1
        self.df2 = df2
        self.df3 = df3
        self.df4 = df4
        # self.config = load_config()  # Load configuration

    def get_value(self, df, key):
        return df[df['KEY'] == key]['VALUE'].values[0]

# Category A
    def get_value_A(self, column_name):
        try:
            # Fetch value from the specific column and convert to string
            return str(self.df4[column_name].values[0])
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
            return str(self.df4[column_name].values[1])
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
            return str(self.df4[column_name].values[2])
        except KeyError:
            print(f"KeyError: '{column_name}' column not found in DataFrame.")
            return None
        except IndexError:
            print(f"IndexError: No data found in column '{column_name}'.")
            return None

    
    async def fill_custom_group_plan_information(self, num_categories, unique_mapped_categories):
        nlg_transfer_medical_data()

        # census_file_path = self.config['file_paths']['census_data']  # Correct key

        # claim_pdf_path = self.config['file_paths']['documents']['claim_pdf'] 
        
        # Select "Customized Group Plan"
        await self.page.locator("//html/body/app-root/app-homepage/section/div/div/div[2]/div/div[5]/div[3]/div/a[1]").click()
        await asyncio.sleep(0.5)  

#----------------------------------------------Customer Details-------------------------------------------------

        # Fill in the Company Name from Sheet1
        await self.page.locator('#customer_name').fill(self.get_value(self.df1, "Company Name"))
        await asyncio.sleep(10)  

        # Fill in the Trade License Number from Sheet1
        await self.page.wait_for_load_state('networkidle')
        await self.page.locator("div").filter(has_text=re.compile(r"^Source Direct Broker AgentSource Direct Broker Agent$")).get_by_role("textbox").click()
        await self.page.locator("span").filter(has_text="Broker").click()
        await asyncio.sleep(1)  

        # Fill in the Email from Sheet1
    # Open the dropdown by clicking on it
        await self.page.wait_for_load_state('networkidle')
        await asyncio.sleep(0.5) 
        await self.page.locator("div:nth-child(3) > .inbuilt_lbl_fields > .select_menu > .large > .input-field > .select-wrapper > input").click()
        await self.page.locator("span").filter(has_text="GARGASH INSURANCE SERVICE CO").click()

        await asyncio.sleep(0.5)  


        # Fill in the Company Name from Sheet1
        commission = self.get_value(self.df1, "Broker Margin")
        # Clean the commission string
        commission = commission.replace('%', '').strip()
        # Split the string by spaces and take the first value
        commission = commission.split()[0]
        # Convert to float and then to int
        commission = int(float(commission))
        await asyncio.sleep(0.5)
        await self.page.locator('#commission').fill(str(commission))
        await asyncio.sleep(0.5) 

        # Select Request Type
        await self.page.locator("div").filter(has_text=re.compile(r"^Request TypeVirginExperienceRequest TypeVirginExperience$")).get_by_role("textbox").click()
        await self.page.locator("span").filter(has_text="Experience").click()
        await asyncio.sleep(0.5)  

        # Fill CRM Ref No
        await self.page.locator('#crm_refno').fill("2323")
        await asyncio.sleep(0.5)  

        # Upload Census file
        # await self.page.locator("#claim_up_field").set_input_files(census_file_path)
        
        await self.page.locator("#claim_up_field").set_input_files("D:\\AlgoSpring\\python\\Union_Insurance\\census-data.xlsx")
        await asyncio.sleep(0.5)  

        # Click Select Benefit Button
        await self.page.get_by_role("button", name="Select Benefits").click()
        await asyncio.sleep(5)  

        # Process categories based on unique categories in letters
        if 'A' in unique_mapped_categories:
            cat1 = self.df2[self.df2['Category'] == 1]
            custom_categories1 = Custom_Categories1(self.page, self.df1, self.df3, self.df4)
            await custom_categories1.custom_categories1_information()

        if 'B' in unique_mapped_categories:
            cat2 = self.df2[self.df2['Category'] == 2]
            custom_categories2 = Custom_Categories2(self.page, self.df1, self.df3, self.df4)
            await custom_categories2.custom_categories2_information()

        if 'C' in unique_mapped_categories:
            cat3 = self.df2[self.df2['Category'] == 3]
            custom_categories3 = Custom_Categories3(self.page, self.df1, self.df3, self.df4)
            await custom_categories3.custom_categories3_information()

        # Click on the "Next" button
        # await self.page.locator('#submitform ').click()


        await self.page.get_by_role("button", name="Next roundarrowwhite").click()

        # Client/Broker Email Request 
        await self.page.locator("[id=\"claim_up_field\\[0\\]\"]").click()
        # await self.page.locator("[id=\"claim_up_field\\[0\\]\"]").set_input_files(claim_pdf_path)
        await self.page.locator("[id=\"claim_up_field\\[0\\]\"]").set_input_files("C:\\Users\\sudeepa.w\\Downloads\\QA202412180106.pdf")   

        # List of members 
        await self.page.locator("[id=\"claim_up_field\\[1\\]\"]").click()
        await self.page.locator("[id=\"claim_up_field\\[1\\]\"]").set_input_files("C:\\Users\\sudeepa.w\\Downloads\\QA202412180106.pdf")

        # Current Table of benefits
        await self.page.locator("[id=\"claim_up_field\\[2\\]\"]").click()
        await self.page.locator("[id=\"claim_up_field\\[2\\]\"]").set_input_files("C:\\Users\\sudeepa.w\\Downloads\\QA202412180106.pdf")

        # Loss ratio report
        await self.page.locator("[id=\"claim_up_field\\[3\\]\"]").click()
        await self.page.locator("[id=\"claim_up_field\\[3\\]\"]").set_input_files("C:\\Users\\sudeepa.w\\Downloads\\QA202412180106.pdf")

        # Submit Button
        await self.page.get_by_role("button", name="Submit Request roundarrowwhite").click()