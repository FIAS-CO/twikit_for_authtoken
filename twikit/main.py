import asyncio
from twikit import Client

USERNAME = 'example_user'
EMAIL = 'email@example.com'
PASSWORD = 'password0000'

# Initialize client
client = Client('en-US')

async def main():
    # アカウントにログイン
    await client.login(
        auth_info_1='connrori' ,
        password='connconnrorirori'
    )
    try:
        auth_token = client.get_auth_token()
        print(f"auth token: {auth_token}")
    except ValueError as e:
        print(e)

asyncio.run(main())
