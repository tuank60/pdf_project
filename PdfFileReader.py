# Python program to create 
# a pdf file 


from fpdf import FPDF
from fpdf import *


class PDF(FPDF):
    def header(self):
        # Logo
        self.image('logo.png', 10, 8, 33)
        # Arial bold 15
        self.set_font('Arial', 'B', 15)
        # Move to the right
        self.cell(80)
        # Title
        self.cell(30, 10, 'Title', 1, 0, 'C')
        # Line break
        self.ln(20)

    # Page footer
    def footer(self):
        # Position at 1.5 cm from bottom
        self.set_y(-15)
        # Arial italic 8
        self.set_font('Arial', 'I', 8)
        # Page number
        self.cell(0, 10, 'Page ' + str(self.page_no()) + '/{nb}'+"Hello\nWorld!", 0, 0, 'C')

# save FPDF() class into a 
# variable pdf 
pdf = PDF()
pdf.alias_nb_pages()
# Add a page
pdf.add_page() 

# set style and size of font 
# that you want in the pdf 
pdf.set_font("Arial", size = 15) 

# create a cell 
pdf.cell(200, 10, txt = "GeeksforGeeks", ln = 1, align = 'C')
pdf.image('logo.png',x=35,y=130,w=150,h=150)
pdf.link(0,0,20,20,"https://www.google.com/")
# add another cell 
pdf.cell(200, 10, txt = "A Computer Science portal for geeks.", ln = 2, align = 'C')

pdf.ln(5)

epw = pdf.w - 2*pdf.l_margin
col_width = epw/4
data = [['First name','Last name','Age','City'],['Jules','Smith',34,'San Juan'],['Mary','Ramos',45,'Orlando'],['Carlson','Banks',19,'Los Angeles']]

pdf.set_font('Times','B',14.0)
pdf.cell(epw, 0.0, 'Demographic data', align='C')
pdf.set_font('Times','',10.0)
pdf.ln(4)

th = pdf.font_size

for row in data:
	for datum in row:
		# Enter data in colums
		# Notice the use of the function str to coerce any input to the
		# string type. This is needed
		# since pyFPDF expects a string, not a number.
		pdf.cell(col_width, th, str(datum), border=1)
	pdf.ln(th)

# Line break equivalent to 4 lines
pdf.ln(4 * th)

pdf.set_font('Times', 'B', 14.0)
pdf.cell(epw, 0.0, 'With more padding', align='C')
pdf.set_font('Times', '', 10.0)
pdf.ln(4)

# Here we add more padding by passing 2*th as height
for row in data:
	for datum in row:
		# Enter data in colums
		pdf.cell(col_width, 2 * th, str(datum), border=1)
	pdf.ln(2 * th)

for i in range(1, 41):
	pdf.cell(0, 10, 'Printing line number ' + str(i), 0, 1)
pdf.output("GFG.pdf")


