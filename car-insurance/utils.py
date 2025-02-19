from datetime import datetime
from dateutil.relativedelta import relativedelta

class Date_utils:
    
    def __init__(self):
        pass
    
    def convertMDYYYY(self, date_str):
        return datetime.strptime(date_str, "%m/%d/%Y")
    
    def getLegalAge(self, date_obj):
        return date_obj + relativedelta(years=18)
    
    def isLegalAge(self, legalAge, currentYear):
        return ((currentYear - legalAge) > 0)
    
    def cal_leagl_age(self, date_str):
        return self.isLegalAge( self.getLegalAge(self.convertMDYYYY(date_str)).year, 2010)