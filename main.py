import requests
import json
import os
from datetime import datetime, timedelta
from prettytable import PrettyTable

while True:
    loktyp = input("Loktyp: ")
    nummer = input("Loknummer: ")
    url = f"https://konzern-apps.web.oebb.at/lok/index/{loktyp}.0{nummer}"
    response = requests.get(url)
    json_data = response.content.decode('utf-8')
    data = json.loads(json_data)

    for row in data:
        if row["departure"] is not None:
            departure_time = datetime.fromisoformat(row["departure"].replace("Z", "+00:00"))
            row["departure"] = (departure_time + timedelta(hours=2)).strftime("%Y-%m-%d %H:%M:%S")
            row["departure"] = row["departure"].replace("2023-", "").replace("T", " ")
            row["departure"] = row["departure"][:row["departure"].find(":")+3]
        if row["arrival"] is not None:
            arrival_time = datetime.fromisoformat(row["arrival"].replace("Z", "+00:00"))
            row["arrival"] = (arrival_time + timedelta(hours=2)).strftime("%Y-%m-%d %H:%M:%S")
            row["arrival"] = row["arrival"].replace("2023-", "").replace("T", " ")
            row["arrival"] = row["arrival"][:row["arrival"].find(":")+3]

    table = PrettyTable()
    table.field_names = ["Zugnummer", "Bahnhof", "Loknummer", "Ankunft", "Abfahrt"]
    for row in data:
        table.add_row([
            row.get("train_number", ""),
            row.get("name", ""),
            row.get("unit_number", ""),
            row.get("arrival", ""),
            row.get("departure", ""),
        ])

    # display the table
    print(table)

    # create the file path
    now = datetime.now()
    date = now.strftime("%Y-%m-%d")
    file_name = f"{loktyp}_{nummer}_{date}.txt"
    file_path = os.path.join("C:/Users/Jonathan/Desktop/Fahrpläne", file_name)

    # write the table to the file
    with open(file_path, "w") as f:
        f.write(str(table))

    print(f"Fahrplan erfolgreich erstellt und gespeichert unter {file_path}!")

