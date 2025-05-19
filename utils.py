import aiohttp
import os
from dotenv import load_dotenv

load_dotenv()

async def check_ban(uid):
    api_url = f"https://api-check-ban.up.railway.app/check_ban/{uid}"
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(api_url) as response:
                if response.status != 200:
                    return None

                response_data = await response.json()
                if response_data.get("status") == 200:
                    data = response_data.get("data")

                    return {
                        "is_banned": data.get("is_banned", 0),
                        "nickname": data.get("nickname", ""),
                        "period": data.get("period", 0),
                        "region": data.get('region',0 )
                    }
                else:
                    return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None
