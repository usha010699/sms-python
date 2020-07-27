from twilio.rest import Client 
 
account_sid = 'AC1e7809889ca80dd831f43e9327169be4' 
auth_token = '[auth token]' 
client = Client(account_sid, auth_token) 
 
message = client.messages.create( 
                              from_='twilio number',
                              body='everything is fine!!!',        
                              to='+91xxxxxxxxxx' 
                          ) 
 
print(message.sid)
