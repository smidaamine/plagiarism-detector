# -*- coding: utf-8 -*-
import urllib
import sys
from cStringIO import StringIO
import nltk

from pdfminer.cmapdb import CMapDB
from pdfminer.image import ImageWriter
from pdfminer.pdfdevice import PDFDevice
from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdfpage import PDFPage
from pdfminer.pdfparser import PDFParser
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
import re

from google import search


__author__ = 'SMIDA'


class PlagiaUtils():
    """
    This class contain PLAGIA functions detections

    """

    def jaccardSimilarity(self,listNgramSu,listNgramOri):
        count=0.0
        matchTri=[]

        for temp in listNgramSu:
            if temp in listNgramOri :
                count+=1
                matchTri.append(temp)

        #print "count ",count,"Tail list ",len(listNgramSu)
        return  (count/len(listNgramSu)),matchTri




class Websearch():



    def Websarch(self,requet,numberResu):
        """
        this method we use http://breakingcode.wordpress.com/2010/06/29/google-search-python/
        """

        urls=search(requet,stop=numberResu)
        return  urls

    def readPdfWeb(self,url):
        try:
            webFile = urllib.urlopen(url)

            pdfFile = open(url.split('/')[-1], 'wb')
            pdfFile.write(webFile.read())
            webFile.close()
            pdfFile.close()
            return url.split('/')[-1],url

        except:
            return None,None



def convert_pdf_To_Txt(path,opts={}):
    """
    this ALGO form pdfinterp modul  documentation


    """

        # debug option
    debug = 0
    # input option
    password = ''
    pagenos = set()
    maxpages = 0
    # output option
    outfile = None
    outtype = None
    imagewriter = None
    layoutmode = 'normal'
    codec = 'utf-8'
    pageno = 1
    scale = 1
    caching = True
    showpageno = True
    laparams = LAParams()
    for (k, v) in opts:
        if k == '-d': debug += 1
        elif k == '-p': pagenos.update( int(x)-1 for x in v.split(',') )
        elif k == '-m': maxpages = int(v)
        elif k == '-P': password = v
        elif k == '-o': outfile = v
        elif k == '-C': caching = False
        elif k == '-n': laparams = None
        elif k == '-A': laparams.all_texts = True
        elif k == '-V': laparams.detect_vertical = True
        elif k == '-M': laparams.char_margin = float(v)
        elif k == '-L': laparams.line_margin = float(v)
        elif k == '-W': laparams.word_margin = float(v)
        elif k == '-F': laparams.boxes_flow = float(v)
        elif k == '-Y': layoutmode = v
        elif k == '-O': imagewriter = ImageWriter(v)
        elif k == '-t': outtype = v
        elif k == '-c': codec = v
        elif k == '-s': scale = float(v)
    #
    PDFDocument.debug = debug
    PDFParser.debug = debug
    CMapDB.debug = debug
    PDFResourceManager.debug = debug
    PDFPageInterpreter.debug = debug
    PDFDevice.debug = debug
    #
    rsrcmgr = PDFResourceManager(caching=caching)
    if not outtype:
        outtype = 'text'
        if outfile:
            if outfile.endswith('.htm') or outfile.endswith('.html'):
                outtype = 'html'
            elif outfile.endswith('.xml'):
                outtype = 'xml'
            elif outfile.endswith('.tag'):
                outtype = 'tag'
    if outfile:
        outfp = file(outfile, 'w')
    else:
        outfp = sys.stdout
    retstr = StringIO()
    if outtype == 'text':
        device = TextConverter(rsrcmgr, retstr, codec=codec, laparams=laparams,
                               imagewriter=imagewriter)
    fp = file(path, 'rb')
    interpreter = PDFPageInterpreter(rsrcmgr, device)
    for page in PDFPage.get_pages(fp, pagenos,
                                      maxpages=maxpages, password=password,
                                      caching=caching, check_extractable=True):
        interpreter.process_page(page)
    #print retstr.getvalue()
    txt2Pdf=retstr.getvalue()
    #print type(txt2Pdf)

    #fp.close()
    #device.close()
    #outfp.close()
    return txt2Pdf
def cleanHtml(page):

    #

    page=nltk.clean_html( page)
    page = re.sub('\|', ' ', page)
    page = re.sub('\s+', ' ', page)



    return page


#convert_pdf_To_Txt()