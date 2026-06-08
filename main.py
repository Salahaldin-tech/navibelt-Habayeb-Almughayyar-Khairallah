from route_manager import RouteManager
from obstacle_manager import ObstacleManager
from visualizer import Visualizer


def main():

    ROUTES_FILE = "routes.json"
    LOG_FILE = "obstacle_log.csv"

    rm = RouteManager()
    om = ObstacleManager()
    viz = Visualizer()

    print("[1/5] Loading data...")

    routes = rm.load_routes(ROUTES_FILE)

    log = om.load_log(LOG_FILE)

    print(f"      Routes loaded : {len(routes)}")

    print(f"      Events loaded : {len(log)}\n")

    print("[2/5] Available navigation routes:")

    rm.display_routes(routes)

    print("\n[3/5] Waypoints for RT01:")

    waypoints = rm.get_waypoints(routes,"RT01")

    for wp in waypoints:

        print(
            f"      Step {wp['step']}: "
            f"{wp['landmark']:<20} "
            f"→ {wp['direction']:<5} "
            f"for {wp['distance_m']} m"
        )

    print("\n[4/5] Logging a test obstacle event...")

    try:

        log = om.add_event(log,
            route_id="RT01",
            direction="Front",
            distance_cm=38
        )

        om.save_log(log,LOG_FILE)

    except ValueError as e:

        print(f"      Failed: {e}")

    print("\n[5/5] Displaying charts...")

    direction_counts = (om.analyze_directions(log))

    viz.direction_chart(direction_counts)

    viz.severity_pie(log)

    print("\nDone!")
    
if __name__ == "__main__":
    main()