from pprint import pprint
import requests


TEST_VEHICLE={
    "license_plate":"HSY4&DHDJQ",
    "v_type":"Truck",
    "color":"Green",
    "parking_spot_no":"5",
    "description":"This is the description.",
    "user_id":"1"

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