from dotenv import load_dotenv
import requests
import os

load_dotenv()

username = os.getenv("username")
token = os.getenv("token")

print(f"USING USERNAME: {username}")


def get_cpu() -> dict:
	request = requests.get('https://www.pythonanywhere.com/api/v0/user/{username}/cpu/'.format(
        username=username
    ),
	headers={"Authorization": "Token {token}".format(token=token)}
	)

	if request.status_code == 200:
		return request.content
	
	print(f"Got unexpected status code: {request.status_code} - {request.content}")


if __name__ == '__main__':
	test = get_cpu()
	print(test)
