import fastf1 as ff1
import pandas as pd
'''
session=fastf1.get_event_schedule(2023)
df=pd.DataFrame(session)
df.to_csv("2023_f1.csv")
'''

qualification = ff1.get_session(2022, 'Saudi Arabian Grand Prix')
qualification.load()
df=pd.DataFrame(qualification.results)
df.to_csv("test.csv")