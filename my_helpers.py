from datetime import datetime

def yearWeekToDateTime(yw):
# Change year_week to the date of the Monday of that week.
# Some acrobatics to get the conversion right. Python counts weeks %W and weekdays %w from 0, 
# so e.g. 1.1.2021 was a Friday. Week 0 weekday 0 of 2021 is pd.to_datetime(('2021-00' + '-0'), format="%Y-%W-%w") 
# which yields 3.1.2021 (first Sunday of 2021). Week 53 of 2020 is also week 00 of 2021.
# In our data however week 1 of 2021 means the one starting 4.1.2021
    (y, w) = yw.split('-')
    neww = w if y=='2021' else str(int(w) - 1)    
    return datetime.strptime((y + '-' + neww + '-1'), "%Y-%W-%w") 
    

    

