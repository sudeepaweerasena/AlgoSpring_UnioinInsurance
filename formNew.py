import asyncio
import datetime
import time
import re
from pioneer_plus import Pioneer_Plus
from customized_group_plan import Customized_Group_Plan

class FormNew:
    def __init__(self, page, df1, df2, df3, df4):
        self.page = page
        self.df1 = df1
        self.df2 = df2
        self.df3 = df3
        self.df4 = df4

    def get_value(self, df, key):
        return df[df['KEY'] == key]['VALUE'].values[0]

    
    async def fill_company_information(self, num_categories, unique_mapped_categories):


#----------------------------------------------Customer Details-------------------------------------------------
        select_plan = self.get_value(self.df1, "Plan Selection")
        print(select_plan)
        await asyncio.sleep(1)

        if select_plan == "Pioneer Plus":
            pioneer_plus_control = Pioneer_Plus(self.page, self.df1, self.df2, self.df3)
            await pioneer_plus_control.fill_poineer_plus_information(num_categories, unique_mapped_categories)
        elif select_plan == "Customized Group Plan":
            custom_plus_control = Customized_Group_Plan(self.page, self.df1, self.df2, self.df3, self.df4)
            await custom_plus_control.fill_custom_group_plan_information(num_categories, unique_mapped_categories)