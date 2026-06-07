import json
import csv

def create_routes(filepath="routes.json"):
    data = {
        "routes": [
            {
                "route_id": "RT01",
                "name": "Home to Campus Main Gate",
                "distance_m": 850,
                "waypoints": [
                    {"step": 1, "landmark": "Front Door",    "direction": "North", "distance_m": 50},
                    {"step": 2, "landmark": "Street Corner", "direction": "East",  "distance_m": 200},
                    {"step": 3, "landmark": "Crosswalk",     "direction": "North", "distance_m": 300},
                    {"step": 4, "landmark": "Campus Gate",   "direction": "East",  "distance_m": 300},
                ],
            },
            {
                "route_id": "RT02",
                "name": "Campus Gate to Library",
                "distance_m": 420,
                "waypoints": [
                    {"step": 1, "landmark": "Main Gate",     "direction": "East",  "distance_m": 100},
                    {"step": 2, "landmark": "Fountain",      "direction": "North", "distance_m": 150},
                    {"step": 3, "landmark": "Library Steps", "direction": "East",  "distance_m": 170},
                ],
            },
            {
                "route_id": "RT03",
                "name": "Dorm to Cafeteria",
                "distance_m": 310,
                "waypoints": [
                    {"step": 1, "landmark": "Dorm Exit",      "direction": "South", "distance_m": 80},
                    {"step": 2, "landmark": "Garden Path",    "direction": "West",  "distance_m": 130},
                    {"step": 3, "landmark": "Cafeteria Door", "direction": "South", "distance_m": 100},
                ],
            },
        ]
    }
    with open(filepath, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Routes saved: {filepath}")

def create_obstacle_log(filepath="obstacle_log.csv"):
    rows = [
        ["event_id", "route_id", "timestamp",           "direction", "distance_cm", "severity"],
        ["EVT001",   "RT01",     "2026-05-15 08:12:34", "Front",     "45",          "High"   ],
        ["EVT002",   "RT01",     "2026-05-15 08:12:50", "Left",      "90",          "Medium" ],
        ["EVT003",   "RT01",     "2026-05-15 08:13:10", "Front",     "30",          "High"   ],
        ["EVT004",   "RT02",     "2026-05-15 09:05:11", "Front",     "120",         "Low"    ],
        ["EVT005",   "RT02",     "2026-05-15 09:05:40", "Right",     "60",          "Medium" ],
        ["EVT006",   "RT02",     "2026-05-15 09:06:02", "Front",     "35",          "High"   ],
        ["EVT007",   "RT03",     "2026-05-15 12:30:15", "Left",      "55",          "Medium" ],
        ["EVT008",   "RT03",     "2026-05-15 12:30:45", "Front",     "25",          "High"   ],
        ["EVT009",   "RT01",     "2026-05-16 08:10:05", "Rear",      "110",         "Low"    ],
        ["EVT010",   "RT02",     "2026-05-16 09:00:20", "Front",     "40",          "High"   ],
    ]
    with open(filepath, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerows(rows)
    print(f"Obstacle log saved: {filepath}")

if __name__ == "__main__":
    create_routes()
    create_obstacle_log()