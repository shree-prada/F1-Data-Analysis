import fastf1
import pandas as pd

session=fastf1.get_event_schedule(2023)
df=pd.DataFrame(session)
df.to_csv("2023_f1.csv")
