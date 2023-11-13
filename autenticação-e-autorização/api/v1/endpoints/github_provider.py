from fastapi import APIRouter, status
from starlette.responses import RedirectResponse
import httpx


router = APIRouter()

github_client_id = '3df3ca56cb0efe8460bc'
github_client_secret = '320b0e55d12d2944b461708c0fdeaf2c5cf2271c'


@router.get('/')
async def github_login():
    return RedirectResponse(f"https://github.com/login/oauth/authorize?client_id={github_client_id}", status_code=status.HTTP_302_FOUND)


@router.get('/github-code')
async def github_code(code: str):
    params = {
        'client_id': github_client_id,
        'client_secret': github_client_secret,
        'code': code
    }
    headers = {
        'Accept': 'application/json'
    }
    async with httpx.AsyncClient() as client:
        response = await client.post(url='https://github.com/login/oauth/access_token', params=params, headers=headers)
        
        
    response_json = response.json()
    print(response_json)
