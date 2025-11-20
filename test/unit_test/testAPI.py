import pytest
import requests
import json

endpoint = "http://127.0.0.1:8000"

#HTTP ヘッダーリクエスト
header = {
    "Content-Type": "application/json",
    "Accept": "application/json"
}

def test01():
    
    #送信するJSONデータ
    data = {
        "id" : "12345"
    }
        
    
    
    response = requests.post(
        endpoint, headers=header, data=json.dump(fp=data)
    )
    
    assert response.status_code == 200