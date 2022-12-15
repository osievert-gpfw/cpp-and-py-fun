#!/usr/bin/env python3

from reportlab.pdfgen import canvas
from reportlab.pdfgen import canvas
from reportlab.lib.units import cm, inch, mm
from reportlab.graphics import shapes
from reportlab.graphics import renderPDF

pagesize = (8.5 * inch, 11 * inch)
c = canvas.Canvas("out.pdf", pagesize=pagesize)
c.drawString(9*cm, 22*cm, "Hello World!")
c.setFillColorRGB(1,0,0)
d = shapes.Drawing(400, 200)
d.add(shapes.Rect(4*cm, 7*cm, 1 * inch, 1 * inch, strokeWidth=4, fillColor=shapes.colors.green, strokeColor=shapes.colors.purple, fill=1))
renderPDF.draw(d, c, 5*cm, 5*cm)
c.rect(4*cm, 5*cm, 1 * inch, 1 * inch, stroke=1, fill=1)
c.rect(2*cm, 2*cm, 1 * cm, 1 * cm, stroke=0, fill=1)
c.showPage()
c.rect(2*cm, 2*cm, 1 * cm, 1 * cm, stroke=0, fill=1)
c.showPage()
c.save()
