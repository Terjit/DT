from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Image
from reportlab.lib import colors
import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
import io
from reportlab.lib.utils import ImageReader

conn = sqlite3.connect('dt.db')
# Sample DataFrame
data = pd.read_sql_query(f"SELECT * FROM DEV WHERE wellName = '3S-714'", conn)
data['TVD'] = round(data['TVD'],2)
data['DLS'] = round(data['DLS'],2)
data['EW'] = round(data['EW'],2)
data['NS'] = round(data['NS'],2)
pdf = SimpleDocTemplate("dataframe.pdf", pagesize=letter)

table_data = []
table_data.append(data.columns.tolist())
for i, row in data.iterrows():
    table_data.append(list(round(row, 2)))

table = Table(table_data)

table_style = TableStyle([
    ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
    ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
    ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
    ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
    ('FONTSIZE', (0, 0), (-1, 0), 14),
    ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
    ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
    ('TEXTCOLOR', (0, 1), (-1, -1), colors.black),
    ('ALIGN', (0, 1), (-1, -1), 'CENTER'),
    ('FONTNAME', (0, 1), (-1, -1), 'Helvetica'),
    ('FONTSIZE', (0, 1), (-1, -1), 12),
    ('BOTTOMPADDING', (0, 1), (-1, -1), 8),
])

table.setStyle(table_style)

plt.plot(data['NS'], data['EW'])


buf = io.BytesIO()
plt.savefig(buf, format='png')
buf.seek(0)
img = Image(buf, width=400, height=300)





pdf_table = []
pdf_table.append(img)
pdf_table.append(table)



pdf.build(pdf_table)