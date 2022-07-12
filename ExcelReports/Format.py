from openpyxl import load_workbook
from openpyxl.styles import Font
wb = load_workbook('pivot_table.xlsx')
# Select sheet to work with
sheet = wb['Report']

# Set title for the report
sheet['A1'] = 'Sales report'
# Set subtitle
sheet['A2'] = 'January'

# Set styles
sheet['A1'].font = Font('Menlo', bold=True, size=20)
sheet['A2'].font = Font('Menlo', bold=True, size=10)

wb.save('Report_January.xlsx')

