import pandas
excel_data_hami = pandas.read_excel(C:\Users\AlpErenOKUR\Desktop/HAMI-Qatar.xls', sheet_name='Sayfa1')
colums = excel_data_hami.columns.ravel()

Years = excel_data_hami[colums[0]].tolist()
Unemployement = excel_data_hami[colums[1]].tolist()
Inflation = excel_data_hami[colums[2]].tolist()
Interestrate = excel_data_hami[colums[3]].tolist()
columns4List = excel_data_hami[colums[4]].tolist()

df = pandas.DataFrame({colums[1]: Unemployment,
                       colums[2]: Inflation,
                       colums[3]: Interestrate,
                       colums[4]: GDPpercapitagrowth},
                    index=Years)

df["HAMI"] = df[colums[1]] + df[colums[2]] + df[colums[3]] - df[colums[4]]

df = df.drop(columns = [colums[1], colums[2], colums[3], colums[4]])

    df.to_excel("AssıgnAlpERENOKUR.xls")