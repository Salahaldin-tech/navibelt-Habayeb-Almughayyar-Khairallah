import csv
from datetime import datetime 

class ObstacleManager:

    def load_log(self,filepath):

        log = []
        try:

            with open(filepath) as f:

                reader=csv.DictReader( f)

                for row in reader:

                    row["distance_cm"]=int(row["distance_cm"])

                    log.append(row)

        except FileNotFoundError:

            return []

        return log
    
    def save_log(self, log, filepath):

        fields = ["event_id","route_id","timestamp","direction","distance_cm","severity"]

        with open(filepath, "w", newline="") as f:

            writer = csv.DictWriter(f,fieldnames=fields)
            writer.writeheader()
            writer.writerows(log)

        print("Log saved")
    
    def add_event(self,log,route_id,direction, distance_cm):

        valid = ["Front", "Left", "Right", "Rear" ]

        if direction not in valid:
            raise ValueError(f"Invalid direction: {direction}")

        if distance_cm < 50:
            severity = "High"

        elif distance_cm <= 100:
            severity = "Medium"

        else:
            severity = "Low"

        new_id = f"EVT{len(log)+1:03d}"

        event = { "event_id": new_id,
                  "route_id": route_id,
                  "timestamp":datetime.now().strftime( "%Y-%m-%d %H:%M:%S"),
                  "direction": direction,
                  "distance_cm": distance_cm,
                  "severity": severity
        }

        log.append(event)

        print(f"Event logged: {new_id} — {direction} obstacle at {distance_cm} cm ({severity}) on {route_id}")

        return log   
    
    def get_by_route(self, log, route_id):
        return [e for e in log if e["route_id"] == route_id]

    def analyze_directions(self, log):
        counts = {}
        for e in log:
            direction = e["direction"]
            counts[direction] = counts.get(direction, 0) + 1
        return counts

