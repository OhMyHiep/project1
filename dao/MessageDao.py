from dao import DatabaseUtil

def saveMessage(msg,user_id):
    sql="""
    INSERT INTO messages (message,user_id) VALUES (%s,%s) RETURNING message_id;
    """
    return DatabaseUtil.executeSimpleQuery(sql,msg,user_id)

def getMessagesByUserId(user_id):
    sql="""
    SELECT *
    FROM messages
    WHERE user_id=%s;
    """
    return DatabaseUtil.executeSimpleQuery(sql,user_id)


def deleteMessage(message_id):
    # print("message ID in dao: ", message_id)
    sql="""DELETE 
    FROM messages
    WHERE message_id=%s RETURNING *; """
    return DatabaseUtil.executeSimpleQuery(sql,message_id)

