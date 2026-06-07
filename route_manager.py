import json


class RouteManager:

    def load_routes(self, filepath: str) -> list:
        # to open the file
        try:
            with open(filepath, "r") as f:
                routes_data = json.load(f)

            return routes_data["routes"]
        # file not found error
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
        #to raise the error
        if route is None:

            raise ValueError("Route not found")

        return route["waypoints"]
    

    def display_routes(self,routes: list) -> None:
        # to print the headers
        print(f"{'Route ID':<10} | "f"{'Name':<30} | "f"{'Distance (m)':<12} | "f"Waypoints")

        print( "-" * 85)
        # to print the data
        for route in routes:

            print(
                f"{route['route_id']:<10} | "f"{route['name']:<30} | "f"{route['distance_m']:<12} | "f"{len(route['waypoints'])}")