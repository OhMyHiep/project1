import pytest
from service.ReimbursementService import*
from dao.DB_orm import db
from flask_login import current_user
from unittest import mock, TestCase


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
    ("more Than one hundred Characters are not allowed to enter into the description of the reimbursement due to the constraints of the requirments for this functionality",False)
))
def test_Comments(testName,expected):
    assert(validateComments(testName)) == expected


@mock.patch("service.ReimbursementService.db")
@mock.patch("service.ReimbursementService.Reimbursement")
class Test(TestCase):

    
    @mock.patch("service.ReimbursementService.current_user")
    def test_addReimbursement(self,current_user,reimbursement,db):
        data={"description":"pytest reimbursement","amount":1,"category_id":2}
        reimbursement.return_value=Reimbursement()
        assert type(addReimbursement(data))==Reimbursement
        

    
    def test_viewRequestByEmployeeId(self,reimbursement,db):
        reimbursement.query.filter_by.return_value.all.return_value= [1,2,3]
        assert len(viewRequestByEmployeeId(8))>0


    
    def test_deleteRequestByReimbursementId(self,reimbursement,db):
        mock_reimbursement=Reimbursement()
        mock_reimbursement.status='pending'

        reimbursement.query.filter_by.return_value.first.return_value=mock_reimbursement
        assert deleteRequestByReimbursementId(8)==f"Request number {8} Deleted Successfully"


    
    def test_deleteRequestByReimbursementId_does_not_exits(self,reimbursement,db):
        reimbursement.query.filter_by.return_value.first.return_value=None
        assert deleteRequestByReimbursementId(8) =="No Data To Delete"

    
    
    def test_cancelRequestByReimbursementId(self,reimbursement,db):
        mock_reimbursement=Reimbursement()
        mock_reimbursement.status='pending'

        reimbursement.query.filter_by.return_value.first.return_value=mock_reimbursement
        assert cancelRequestByReimbursementId(8)==f"Request number {8} Cancelled Successfully"


    def test_viewRequestByStatus(self,reimbursement,db):
        data={"status":"fake","comments":"","reimbursement_id":8}
        mock_reimbursement=Reimbursement()
        
        reimbursement.query.filter_by.return_value.all.return_value=[1,2,3]

        assert viewRequestByStatus(data)==[1,2,3]

    
    @mock.patch("service.ReimbursementService.validateComments",return_value=True)
    @mock.patch("service.ReimbursementService.isManager",return_value=True)
    @mock.patch("service.ReimbursementService.current_user")
    def test_alterReimbursement(self,current_user,isManager,isValidComments,reimbursement,db):
        data={"status":"fake","comments":"","reimbursement_id":8}
        current_user.employee_id=7

        mock_reimbursement=Reimbursement()
        mock_reimbursement.employee_id=8

        reimbursement.query.filter_by.return_value.first.return_value=mock_reimbursement
        assert type(alterReimbursement(data))==Reimbursement