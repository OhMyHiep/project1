async function alterReimbursement(request_id,status){
    let request=document.getElementById(request_id)
    let comments=request.querySelector('#comments').value
    let reimbursement_id=request_id.replace("reimbursement","")
    fetch('/reimbursement/alter',{
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify( {
            "reimbursement_id":reimbursement_id,
            "status":status,
            "comments":comments
        })
    }).then((_res)=> {
        return _res.json()
        // console.log(_res)
    }).then (data => {
        console.log(data)
        data.hasOwnProperty('status')? request.remove():void(0)
        
    })
}
    
async function addReimbursement(){
    let category= document.getElementById('inputGroupSelect01').value;
    let description= document.getElementById("description").value;
    let amount=document.getElementById("amount").value;

    fetch('/reimbursement',{
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify( {
            "description":description,
            "category_id":category,
            "amount":amount
        })
    }).then((_res)=> {
        return _res.json()
    }).then (data => {
        console.log(data)
    })
    location.href='http://127.0.0.1:5000'
}


let body = document.querySelector("body")

let ViewAllContainer= document.querySelector("#ViewAllContainer")
let DeleteRequestContainer=document.querySelector("#DeleteRequestContainer")

let viewAllButton=document.querySelector("#ViewAllBtn")


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
            <th>Delete</th>
        </tr>`
        for( let data of tableData){
            // fontColor=findColor(data.status);
            newTable +=
            `<tr>
            <td>${data.reimbursement_id}</td>
            <td>${data.description}</td>
            <td>${data.amount}</td>
            <td>${data.comments}</td>
            <td>${data.category_id}</td>
            <td style="color:red">${data.status}</td>
            <td><button type="CancelRequest" name=${data.reimbursement_id} id="cancelReq${data.reimbursement_id}"class="btn btn-outline-success" onclick=cancelRequest(${data.reimbursement_id})>Cancel</button></td>
        </tr>`
        }
    `</table>`

        tableholder.innerHTML = newTable;
}

function findColor(data)
{
    if (data=="Rejected"){
        return red;
    }else if(data=="Accepted"){
        return green;
    }else{
        return blue;
    }
}

function cancelRequest(req_id)
{
    console.log(req_id);
    const URL = '/reimbursement'
    const xhr = new XMLHttpRequest();
    sender = JSON.stringify({"req_id":req_id})
    xhr.open('DELETE', URL);
    xhr.onload  = function() {
        var jsonResponse = JSON.parse(xhr.responseText);
        // do something with jsonResponse
        alert(jsonResponse);
     };
    xhr.send(sender);
    followPath()
}

let DeleteRequest=document.querySelector("#DeleteRequestBtn")


DeleteRequest.addEventListener("click",followDelPath)

function followDelPath()
{
    let applicationAPIUrl="http://127.0.0.1:5000/reimbursement"
    console.log("action Performed")
    fetch(applicationAPIUrl).then(response=>{
        response.json().then(json_body=>{
            console.log(json_body)
            generateDelTable(json_body)
        })
    })
}

function generateDelTable(tableData)
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
            <th>Delete</th>
        </tr>`
        for( let data of tableData){
            if(data.status=="pending" || data.status =="Cancelled")
            {
                newTable +=
                `<tr>
                <td>${data.reimbursement_id}</td>
                <td>${data.description}</td>
                <td>${data.amount}</td>
                <td>${data.comments}</td>
                <td>${data.category_id}</td>
                <td style="color:red">${data.status}</td>
                <td><button type="DeleteRequest" name=${data.reimbursement_id} id="deleteReq${data.reimbursement_id}"class="btn btn-outline-success" onclick=deleteRequest(${data.reimbursement_id})>Delete</button></td>
                </tr>`
            }
        }
    `</table>`

        tableholder.innerHTML = newTable;
}


function deleteRequest(req_id)
{
    console.log(req_id);
    const URL = '/delreimbursement'
    const xhr = new XMLHttpRequest();
    sender = JSON.stringify({"req_id":req_id})
    xhr.open('DELETE', URL);
    xhr.onload  = function() {
        var jsonResponse = JSON.parse(xhr.responseText);
        // do something with jsonResponse
        alert(jsonResponse);
     };
    xhr.send(sender);
    followDelPath()
    
}