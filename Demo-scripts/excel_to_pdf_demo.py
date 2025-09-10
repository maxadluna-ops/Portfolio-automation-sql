import pandas as pd
from fpdf import FPDF

# Cargar archivo Excel (ejemplo: ventas.xlsx)
df = pd.read_excel("ventas.xlsx")

# Crear PDF
pdf = FPDF()
pdf.add_page()
pdf.set_font("Arial", size=12)
pdf.cell(200, 10, txt="Reporte de Ventas (Demo)", ln=True, align='C')

# Datos (solo muestra valores)
for i, row in df.iterrows():
    pdf.cell(200, 10, txt=str(row.values), ln=True)

# Guardar PDF
pdf.output("reporte_ventas_demo.pdf")
print("Demo de PDF creado.")
