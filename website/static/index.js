
function deleteMessage(message_id,text,user_id){
    var msg_obj={
        'message_id': message_id,
        'text': text,
        'user_id': user_id
    };
    console.log("message: "+msg_obj)

    fetch('/delete-message',{
        method: 'POST',
        body: JSON.stringify({msg_obj})
    }).then((_res)=> {
        window.location.href= "/"
    })
}