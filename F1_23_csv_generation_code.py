import fastf1
import pandas as pd

year=2023
racename="FORMULA 1 GULF AIR BAHRAIN GRAND PRIX 2023"
session=fastf1.get_session(year,racename,"R")
session.load()
drivers= session.drivers
df=pd.DataFrame(drivers)
df.to_csv(f"Drivers_{year}.csv")


