import requests
import json

URL = 'https://sugoku.herokuapp.com/board?difficulty=random'


def get_sudoku():
    """
    get random sudoku from api and parse json data to object data
    :return:
    """
    response = requests.get(URL)

    if response.status_code == 200:
        return json.loads(response.text)

    return None
