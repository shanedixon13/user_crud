from pprint import pprint
import requests


TEST_VEHICLE={
    "license_plate":"HSY4KDU88",
    "v_type":"Mini-Van",
    "color":"Grey",
    "parking_spot_no":"25",
    "description":"This is the description of John's vehicle.",
    "user_id":"3"

}

URL="http://127.0.0.1:5000/users/vehicles"

def test_vehicle_creation():
    out=requests.post(URL, json=TEST_VEHICLE)
    if out.status_code==201:
        out_json=out.json()
        pprint(out_json)
        return out_json["new_id"]
    else:
        print("Something went wrong while creating a vehicle.")
        return -1

if __name__=="__main__":
    new_id=test_vehicle_creation()