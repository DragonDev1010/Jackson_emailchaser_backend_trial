from allauth.socialaccount.models import SocialToken
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from django.core.mail import EmailMessage

def send_gmail_with_oauth2(subject, body, to, request):
    # Get the user's OAuth2 token
    social_token = SocialToken.objects.get(account__user=request.user, account__provider='google')
    oauth2_token = Credentials.from_authorized_user_info(info=social_token.token, scopes=['https://www.googleapis.com/auth/gmail.compose'])
    
    # Create a Gmail API client with the user's credentials
    try:
        service = build('gmail', 'v1', credentials=oauth2_token)
    except HttpError as error:
        print('An error occurred: %s' % error)
        return False
    
    # Create the email message
    message = EmailMessage(subject=subject, body=body, to=[to])
    
    # Send the email message
    try:
        message.send()
    except Exception as e:
        print(str(e))
        return False
    
    return True

def read_gmail_with_oauth2(request):
    user = request.user
    credentials = Credentials.from_authorized_user_info(user.social_auth[0].extra_data)
    service = build('gmail', 'v1', credentials=credentials)

    try:
        result = service.users().messages().list(userId='me', maxResults=5).execute()
        messages = result.get('messages', [])

        for message in messages:
            msg = service.users().messages().get(userId='me', id=message['id']).execute()
            payload = msg['payload']
            headers = payload['headers']

            for header in headers:
                if header['name'] == 'Subject':
                    subject = header['value']
                elif header['name'] == 'From':
                    sender = header['value']
                elif header['name'] == 'Date':
                    created_at = header['value']

            snippet = msg['snippet']
            print(f"Subject: {subject}\nFrom: {sender}\nDate: {created_at}\nSnippet: {snippet}\n\n")

    except HttpError as error:
        print(f"An error occurred: {error}")

