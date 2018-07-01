import datetime
import pandas as pd
import requests
import os.path

datestr = datetime.date.today().strftime("%Y%m%d")
file_path = "tablaunica_9_{}.html".format(datestr)
url = "http://www.ahba.com.ar/muestro_datos_tablas_unicas.php?mi_tabla=9"

headers = {
    "host": "www.ahba.com.ar",
    "user-agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:60.0) Gecko/20100101 Firefox/60.0",
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "accept-language": "en-GB,en;q=0.5",
    "accept-encoding": "gzip, deflate",
    "DNT": "1",
    "connection": "keep-alive",
    "upgrade-insecure-requests": "1"}

if (not os.path.isfile(file_path)):
    r = requests.get(url, headers=headers)
    r.encoding = "utf-8"
    s = r.text

    # Write file
    with open(file_path, 'w') as file:
        file.write(s)

# Open file
with open(file_path, 'r') as f:
    tables = pd.read_html(f.read(), match="TABLA DE POSICIONES", header=2)

df = tables[0]
df = df.set_index(['Club'])

print(df.head(5))

#
# # print(df[["Club", "Pts"]].head(5)) # Regs de las columnas
#
# # print(df[0:5]) # Regs del 0:5
#
# print(df.loc[[0]])
#
#
# print(df.loc[["ITALIANO-B", "CAMIONEROS"]])
