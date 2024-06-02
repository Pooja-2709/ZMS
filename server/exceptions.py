
"""
Description: 
    To Update single Record 
Arguments:
    Exception : Invalid number is entered
Returns:
    Return message 
"""

class InvalidPage(Exception):
    pass

"""
Description: 
    To Update single Record 
Arguments:
    Exception : if value is as entered as string in Offset or in paginator , so it must be entered integer
Returns:
    Return message as invalid page
"""

class PageNotAnInteger(InvalidPage):
    pass

"""
Description: 
    To Update single Record 
Arguments:
    Exception : if value is not entered in Offset or in paginator 
Returns:
    Return message as invalid page , a numerical value must entere into offset 
"""
class EmptyPage(InvalidPage):
    pass
