from pprint import pprint
import requests

TEST_VEHICLE_DATA={
    "license_plate":"UPDATE1234",
    "v_type":"Car",
    "color":"Blue",
    "parking_spot_no":"20",
    "description":"This is the description of the updated vehicle.",
    "user_id":"1"
}

URL="http://127.0.0.1:5000/users/1/vehicles"

def update_user():
    out= requests.put(URL, json=TEST_VEHICLE_DATA)
    if out.status_code==200:
        pprint(out.json())
    else:
        print("Something went wrong while trying to update vehicle.")

if __name__=="__main__":
    update_user()