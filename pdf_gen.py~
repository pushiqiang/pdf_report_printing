#coding:utf-8
from django.http import HttpResponse
from reportlab.lib.styles import getSampleStyleSheet,ParagraphStyle
from reportlab.platypus import Table,SimpleDocTemplate,Paragraph,Spacer,flowables
from reportlab.lib.units import inch
from reportlab.lib.enums import TA_JUSTIFY

import reportlab.rl_config
reportlab.rl_config.warnOnMissingFontGlyphs = 0
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfgen import canvas

pdfmetrics.registerFont(TTFont('hei', '/usr/share/fonts/truetype/wqy/wqy-microhei.ttc'))
from reportlab.lib import fonts,colors
fonts.addMapping('hei', 0, 0, 'hei')
fonts.addMapping('hei', 0, 1, 'hei')

def GenPDF(tablename,head,result):

    stylesheet=getSampleStyleSheet()
    elements = []

    response = HttpResponse(content_type='application/octet-stream')
    response['Content-Disposition'] = 'attachment;filename="test.pdf"'

    doc = SimpleDocTemplate(response)
    headname = '<font name="hei">' + str(tablename) +'表格</font>'
    #headname = '<font name="hei">%s表格</font>' % tablename
    elements.append(Paragraph(headname,stylesheet['Title']))
    elements.append(Spacer(1,12))
 
    data = []
    data.append(head)
    
    for l in result:
        row = [l[key] for key in head]
        data.append(row)

    ts=[('INNERGRID', (0,0), (-1,-1), 0.25, colors.black),('BOX', (0,0), (-1,-1), 0.25, colors.black),('FONT', (0,0), (-1,-1), 'hei')]
    table = Table(data, 6.3/len(head)*inch, 0.24*inch, ts)
    elements.append(table)
    doc.build(elements)

    return response


