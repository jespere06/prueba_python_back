import httpx

class FetchEngine:   
    async def user_albums(self, user_id):
        async with httpx.AsyncClient() as client:
            response = await client.get(f'https://jsonplaceholder.typicode.com/users/{user_id}/albums')
        return response.json()
    
    async def user_todos(self, user_id):
        async with httpx.AsyncClient() as client:
            response = await client.get(f'https://jsonplaceholder.typicode.com/users/{user_id}/todos')
        return response.json()
    
    async def user_posts(self, user_id):
        async with httpx.AsyncClient() as client:
            response = await client.get(f'https://jsonplaceholder.typicode.com/users/{user_id}/posts')
        return response.json()