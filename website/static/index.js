async function alterReimbursement(request_id,status){
    let comments=document.getElementById(request_id).querySelector('#comments').value
    let reimbursement_id=request_id.replace("reimbursement","")
    fetch('/reimbursement/alter',{
        method: 'POST',
        body: JSON.stringify( {
            "reimbursement_id":reimbursement_id,
            "status":status,
            "comments":comments
        })
    }).then((_res)=> {
        return _res.json()
        // console.log(_res)
    }).then (data => console.log(data))
    
    
}