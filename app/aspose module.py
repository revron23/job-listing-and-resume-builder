# -*- coding: utf-8 -*-
"""
Created on Wed Oct 11 13:44:58 2023

@author: Steve
"""

from pathlib import Path
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
import aspose.words as aw

doc = aw.Document("CV.pdf")
doc.save("Output.png")
doc2 = aw.Document("Output2003")
doc2.save("html code.html")
