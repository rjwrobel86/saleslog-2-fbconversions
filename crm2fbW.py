#CRM Sold Log -> FB Sold Log

import pandas as pd
import numpy as np

data = pd.read_csv('sldlog.csv')

fbframe = data[['SoldDate', 'FirstName', 'LastName', 'Email', 'EvePhone', 'PostalCode', 'State', 'FrontGross', 'BackGross', 'SoldNote', 'VehicleVIN','AutoLeadID']]

fbframe['Country'] = 'US'
fbframe['Event'] = 'Purchase'
fbframe['Currency'] = 'USD'
fbframe['Order ID'] = fbframe['AutoLeadID']
fbframe['Value'] = fbframe['FrontGross'] + fbframe['BackGross']

fbframe['Phone'] = fbframe['EvePhone']
fbframe['Phone'] = fbframe['Phone'].astype(str)

fbframe['Phone'] = '+1' + fbframe['Phone']
fbframe['Phone'] = fbframe['Phone'].str.rstrip('.0')

#fbframe['Value'] = fbframe['Value'].astype(str)
fbframe['Value'] = fbframe['Value'].clip(lower = 1)

fbframe = fbframe.drop(fbframe.columns[4], axis=1)

columns = {'SoldDate':'Event Time','FirstName':'First Name','LastName':'Last Name','Email':'Email','EvePhone':'Phone','PostalCode':'ZIP/Postal Code','State':'State/Province','VehicleVIN':'Item Number','Country':'Country','Value':'Value'}
fbframe = fbframe.rename(columns=columns)
fbframe = fbframe.drop(['FrontGross','BackGross','SoldNote','AutoLeadID'], axis=1)
#fbframe['Phone'] = fbframe['Phone'].astype('string')

fbframe['Event Time'] = pd.to_datetime(fbframe['Event Time'])

fbframe['Event Time'] = fbframe['Event Time'].dt.date

fbframe.fillna(1, inplace=True)
#fbframe['Phone'].add_prefix("'+")

fbframe.to_csv('soldlog4facebook.csv', index=False)
