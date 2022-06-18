import pytest
from service.ReimbursementService import*


@pytest.mark.parametrize("testName,expected",(
    ("    ",False),("",False),("k",False),("Official visit to client on 15-11-20",True),
    (" spaceInfront",True),("spaceAfter ",True),("......",False),("Relocate to Toronto",True),
    ("_underscoreFront",True),("^&*(?<",False),("two._inTheMid",True),("two..inTheMid",True),
    ("5565",False),("periodAtEnd.",True),("+-367--",False),
    ("more_Than_Fifty_Characters_are not allowed to enter",False)
))
def test_Description(testName,expected):
    assert(validateDescription(testName)) == expected

@pytest.mark.parametrize("testName,expected",(
    ("    ",False),("",False),("k",False),("$200",False),(125,True),(120.5,True),
    (5565,False),(-367,False),(0,False),(1,True),(1000,True),(1001,False)
))
def test_amount(testName,expected):
    assert(validateAmount(testName)) == expected

@pytest.mark.parametrize("testName,expected",(
    ("    ",False),("",False),("k",False),("Approved $90.25",True),
    (" spaceInfront",True),("spaceAfter ",True),("......",False),("The request is approved",True),
    ("_underscoreFront",True),("^&*(?<",False),("two._inTheMid",True),("two..inTheMid",True),
    ("5565",False),("periodAtEnd.",True),("+-367--",False),
    ("more_Than_Fifty_Characters_are not allowed to enter",False)
))
def test_Comments(testName,expected):
    assert(validateComments(testName)) == expected