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
    
let body = document.querySelector("body")

let ViewAllContainer= document.querySelector("#ViewAllContainer")
let DeleteRequestContainer=document.querySelector("#DeleteRequestContainer")

let viewAllButton=ViewAllContainer.children[0]

viewAllButton.addEventListener("click",followPath)

function followPath()
{
    let applicationAPIUrl="http://127.0.0.1:5000/reimbursement"
    console.log("action Performed")
    fetch(applicationAPIUrl).then(response=>{
        response.json().then(json_body=>{
            console.log(json_body)
            generateTable(json_body)
        })
    })
}

function generateTable(tableData)
{
    tableholder=document.querySelector("#viewAllRequests");
    newTable=`
    <table border="1">
        <tr>
            <th>Request ID</th>
            <th>Description</th>
            <th>Amount</th>
            <th>Comments</th>
            <th>Category</th>
            <th>Status</th>
        </tr>`;
        for( let data of tableData){
            newTable +=
            `<tr>
            <td>${data.reimbursement_id}</td>
            <td>${data.description}</td>
            <td>${data.amount}</td>
            <td>${data.comments}</td>
            <td>${data.category_id}</td>
            <td style="color: red">${data.status}</td>
        </tr>`
        }
    `</table>`

        tableholder.innerHTML = newTable;
}