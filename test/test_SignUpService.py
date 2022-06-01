from re import T
from service.SignUpService import *
import pytest




@pytest.mark.parametrize("testName,expected",(
    ("    ",False),("Dan",False),("Al",False),("john doe",False),("testing9",True),
    (" spaceInfront",True),("spaceAfter ",True),("......",False),
    ("_underscoreFront",False),("two__inTheMid",False),("two._inTheMid",False),("two..inTheMid",False),
    (".PeriodInfront",False),("periodAtEnd.",False),("underscoreAtEnd_",False),
    ("more_Than_Twenty_Characters",False)
))
def test_username(testName,expected):
    assert(validateUsername(testName)) == expected


@pytest.mark.parametrize("passoword,password2,expected",(
   ("one","one",False),("6chars","6chars",True),("`'.`&%(%#@","`'.`&%(%#@",True),
   ("don'tMatch","won'tMatch",False),("space in the mid","space in the mid",True),
   ("more_Than_Twenty_Characters","more_Than_Twenty_Characters",False)
))
def test_password(passoword,password2 ,expected):
    assert(validatePassword(passoword,password2))== expected


@pytest.mark.parametrize("testName,expected",(
    ("    ",False),("Dan",True),("Al",True),("john doe",False),("testing9",True),
    (" spaceInfront",True),("spaceAfter ",True),(".....",False)
))
def test_firstname(testName,expected):
    assert(validateFirstName(testName)) == expected



@pytest.mark.parametrize("testName,expected",(
    ("    ",False),("Dan",True),("Al",True),("john doe",False),("testing9",True),
    (" spaceInfront",True),("spaceAfter ",True),(".....",False)
))
def test_lastName(testName,expected):
    assert(validateLastName(testName)) == expected



@pytest.mark.parametrize("email,expected",(
    (".leadingDot@gmail.com",False),("two..inMid@gmail.com",False),("trailingDot@gmail.com.",False),
    ("hiephuynh@gmail.com",True)
))
def test_email(email,expected):
     assert(validateEmail(email)) == expected
