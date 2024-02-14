from mailing.engine import mailjet
from db_details import mailjet_sender_email as sender

#TODO: TO FINISH THE HTML
def register_email_send(user):

    register_email = {
        'Messages': [
            {
                "From": {
                    "Email": f'{sender}',
                    "Name": 'Shift Seek',
                },
                "To": [
                    {
                        "Email": f'{user.email}',
                        "Name": f'{user.username}'
                    }
                ],
                "Subject": "Shift Seek Registration",
                "TextPart": "Welcome to Shift Seek!",
                "HTMLPart": f'<h1>Thank you for joining us!</h1> <br>' +
                f'<p>Activate your account!</p>'
            }
        ]
    }

    result = mailjet.send.create(data=register_email)
    return result