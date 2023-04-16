import requests
APPLICATION_KEY = 'ed423ce34emsh37571dc2a13cfa5p1dc960jsn4fa7650fe783'

def pan_verifiy(pan_no):
    print("pan_verify api called---->",pan_no)

    url = "https://pan-card-verification1.p.rapidapi.com/v3/tasks/sync/verify_with_source/ind_pan"

    payload = {
        "task_id": "74f4c926-250c-43ca-9c53-453e87ceacd1",
        "group_id": "8e16424a-58fc-4ba4-ab20-5bc8e7c3c41e",
        "data": {"id_number": "ABCDE1234"}
    }
    headers = {
        "content-type": "application/json",
        "X-RapidAPI-Key": f"{APPLICATION_KEY}",
        "X-RapidAPI-Host": "pan-card-verification1.p.rapidapi.com"
    }

    response = requests.request("POST", url, json=payload, headers=headers)

    print(response.text)
    