#get_info.py>


import requests
import json
from datetime import datetime
import math




def get_connection(dep, dest, stime):
    connection = requests.get(f"http://transport.opendata.ch/v1/connections?from={dep}&to={dest}&time={stime}&limit=5")
            
    dict_connection = json.loads(connection.content.decode("UTF-8"))
    d1 = dict_connection["connections"]
    connections = []
    for i in range(1,5):
        station = str(d1[i]["from"]["station"]["name"])
        platform = str(d1[i]["from"]["platform"])
        dep_time = d1[i]["from"]["departure"]
        dep_timestamp = datetime.fromtimestamp(d1[i]["from"]["departureTimestamp"]).strftime("%H:%M")
        transfers = d1[i]["transfers"]
        con_time = (d1[i]["to"]["arrivalTimestamp"] - d1[i]["from"]["departureTimestamp"]) / 60
        con_time_h = 0
        if con_time > 59:
            con_time_h = math.trunc(con_time / 60)
        con_time_m = math.trunc(con_time - 60 * con_time_h)

        if con_time_h >= 1:
            con_time_r = f"{con_time_h} h {con_time_m} min"
        else: 
            con_time_r = f"{con_time_m} min"
        
        con = [dep_timestamp, station, platform, transfers, con_time_r]

        connections.append(con)
        
    return connections




if __name__ == "__main__":
    get_connection()
    

    


        