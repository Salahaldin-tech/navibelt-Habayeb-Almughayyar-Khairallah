import json


class RouteManager:

    def load_routes(self, filepath: str) -> list:

        try:
            with open(filepath, "r") as f:
                routes_data = json.load(f)

            return routes_data["routes"]

        except FileNotFoundError:
            raise FileNotFoundError(
                f"Routes data file is not found: {filepath}"
            )

    def get_route(self,routes: list,route_id: str) -> dict:

        for route in routes:

            if route["route_id"].upper() == route_id.upper():

                return route

        return None
    
    def get_waypoints(self,routes: list,route_id: str) -> list:

        route = self.get_route(routes, route_id)

        if route is None:

            raise ValueError("Route not found")

        return route["waypoints"]