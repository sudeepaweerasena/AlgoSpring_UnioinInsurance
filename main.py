import os
import asyncio
import pandas as pd
from playwright.async_api import async_playwright
from login import Login
from formNew import FormNew


async def main():
    # # Read data from Sheet1 and Medical Upload (Sheet3 seems to be df3 in your context)
    file_path = 'D:\\AlgoSpring\\python\\Union_Insurance\\UnionInsurunce.xlsx'
    df1 = pd.read_excel(file_path, sheet_name="Sheet1")
    df3 = pd.read_excel(file_path, sheet_name="pioneer_plus")
    df4 = pd.read_excel(file_path, sheet_name="custom_group")

    # Update the correct path and sheet name for df2 (Medical Upload)
    file_path = "D:\\AlgoSpring\\python\\Union_Insurance\\census-data.xlsx"
    df2 = pd.read_excel(file_path, sheet_name="Upload Template")

    if df1.empty:
        print("No data found in Sheet1")
        raise Exception("No data found in Sheet1")

    if df2.empty:
        print("No data found in Census Upload")
        raise Exception("No data found in Census Upload")

# Extract unique categories from the 'Category' column
    unique_categories = df2['Category'].unique()
    
    category_mapping = {
        "Category A": "A",
        "Category B": "B",
        "Category C": "C"
    }
    mapped_categories = [category_mapping.get(category, category) for category in unique_categories]
    unique_mapped_categories = sorted(set(mapped_categories))
    
    print(f"Mapped and unique categories: {unique_mapped_categories}")

    # Get the number of unique categories
    num_categories = len(unique_mapped_categories)
    print(f"Number of unique categories: {num_categories}")

    async with async_playwright() as playwright:
        # Launch the browser
        browser = await playwright.chromium.launch(headless=False)
        context = await browser.new_context()
        context.set_default_timeout(60000)
        page = await context.new_page()

        # Login and process form
        login = Login(page)
        await login.perform_login("likith.b@gargashinsurance.com", "Lik@06092024")
        # Instantiate formNew with df1 data
        formNew = FormNew(page, df1, df2, df3, df4)
   
        await formNew.fill_company_information(num_categories, unique_mapped_categories)
    

        # # Process categories based on unique categories in letters
        # if 'A' in unique_mapped_categories:
        #     cat1 = df2[df2['Category'] == 1]
        #     categories1 = Categories1(page, df3, cat1)
        #     await categories1.categories1_information()

        # if 'B' in unique_mapped_categories:
        #     cat2 = df2[df2['Category'] == 2]
        #     categories2 = Categories2(page, df3, cat2)
        #     await categories2.categories2_information()

        # if 'C' in unique_mapped_categories:
        #     cat3 = df2[df2['Category'] == 3]
        #     categories3 = Categories3(page, df3, cat3)
        #     await categories3.categories3_information()
#----------------------------------------------------Finish-----------------------------------------------------

        # await page.get_by_role("button", name="Next roundarrowwhite").click()

        # # Client/Broker Email Request 
        # await page.locator("[id=\"claim_up_field\\[0\\]\"]").click()
        # await page.locator("[id=\"claim_up_field\\[0\\]\"]").set_input_files("C:\\Users\\sudeepa.w\\Downloads\\QA202412180106.pdf")   

        # # List of members 
        # await page.locator("[id=\"claim_up_field\\[1\\]\"]").click()
        # await page.locator("[id=\"claim_up_field\\[1\\]\"]").set_input_files("C:\\Users\\sudeepa.w\\Downloads\\QA202412180106.pdf")

        # # Current Table of benefits
        # await page.locator("[id=\"claim_up_field\\[2\\]\"]").click()
        # await page.locator("[id=\"claim_up_field\\[2\\]\"]").set_input_files("C:\\Users\\sudeepa.w\\Downloads\\QA202412180106.pdf")

        # # Loss ratio report
        # await page.locator("[id=\"claim_up_field\\[3\\]\"]").click()
        # await page.locator("[id=\"claim_up_field\\[3\\]\"]").set_input_files("C:\\Users\\sudeepa.w\\Downloads\\QA202412180106.pdf")

        # # Submit Button
        # await page.get_by_role("button", name="Submit Request roundarrowwhite").click()
     

        # Close the browser
        await browser.close()

if __name__ == "__main__":
    asyncio.run(main())

