import csv


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
    
    
    



