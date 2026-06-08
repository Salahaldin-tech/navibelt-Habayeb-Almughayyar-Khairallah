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

    print(f"Routes loaded : {len(routes)}")

    print(f"Events loaded : {len(log)}\n")

    print("[2/5] Available navigation routes:")

    rm.display_routes(routes)

if __name__ == "__main__":
    main()