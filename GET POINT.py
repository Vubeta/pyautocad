from pyautocad import Autocad, APoint
acad = Autocad()
point1 = acad.doc.Utility.GetPoint()
point2 = acad.doc.Utility.GetPoint()
point01 = APoint(point1[0],point1[1])
point02 = APoint(point2[0],point2[1])
acad.model.AddLine(point01,point02)





