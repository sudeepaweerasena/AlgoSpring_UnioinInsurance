import os
import asyncio
import pandas as pd
from playwright.async_api import async_playwright
from login import Login
from formNew import FormNew
from load_yaml import CENSUS_DATA_PATH, ATTACHMENTS_DIR

async def main():
    # # Read data from Sheet1 and Medical Upload (Sheet3 seems to be df3 in your context)
    # file_path = 'D:\\AlgoSpring\\python\\Union_Insurance\\UnionInsurunce.xlsx'
    df1 = pd.read_excel(ATTACHMENTS_DIR, sheet_name="Sheet1")
    df3 = pd.read_excel(ATTACHMENTS_DIR, sheet_name="pioneer_plus")
    df4 = pd.read_excel(ATTACHMENTS_DIR, sheet_name="custom_group")

    # Update the correct path and sheet name for df2 (Medical Upload)
    # file_path_census = "D:\\AlgoSpring\\python\\Union_Insurance\\census-data.xlsx"
    df2 = pd.read_excel(CENSUS_DATA_PATH, sheet_name="Upload Template")

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
    


        # Close the browser
        await browser.close()

if __name__ == "__main__":
    asyncio.run(main())

