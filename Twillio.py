from twilio.rest import Client

account_ sid = ""
auth_token = ""
client = Client(account_sid, auth_token)

message = client.sms.messages.create(
    body = "Hello Drew, this is a test message, my name is Terminator",
    to = "Insert Phone number here",
    from = "Insert Twillio number here"
)

print (message.sid)

# I need a burner phone and email to get this to work
