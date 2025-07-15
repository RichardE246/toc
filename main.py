import pandas as pd
from pypdf import PdfReader, PdfWriter
import numpy as np

reader = PdfReader("source/Barbados-Economic-and-Social-Report-2024.pdf")
writer = PdfWriter()
writer.append(reader)

df = pd.read_csv('source/bb-report-header.csv', dtype=str, header=0)
df = df.replace(np.nan, None)

parent_header = None
parent_subheader = None
for index, row in df.iterrows():

    header = row['header']
    subheader = row['subheader']
    paragraph = row['paragraph']
    page = row['page']

    page = int(page) - 1

    if header:
        outline_header = writer.add_outline_item(title=header, page_number=page, parent=None)
        parent_header = outline_header
    elif subheader:
        outline_subheader = writer.add_outline_item(title=subheader, page_number=page, parent=parent_header)
        parent_subheader = outline_subheader
    else:
        outline_paragraph = writer.add_outline_item(title=paragraph, page_number=page, parent=parent_subheader)


writer.write('build/Barbados-Economic-and-Social-Report-2024_Outlined.pdf')