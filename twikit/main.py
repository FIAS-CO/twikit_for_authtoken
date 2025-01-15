import asyncio
import requests
from twikit import Client

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


        # 指定のURLを叩く
        api_url = f"https://xsearchbancheckerapi.fia-s.com/api/save-auth-token?token={auth_token}"
        response = requests.get(api_url)

        # レスポンスの確認
        if response.status_code == 200:
            print("APIコール成功:", response.json())
        else:
            print("APIコール失敗:", response.status_code)

    except ValueError as e:
        print(e)
    except requests.RequestException as e:
        print(f"API呼び出しエラー: {e}")

asyncio.run(main())
