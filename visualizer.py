import matplotlib.pyplot as plt

class Visualizer:

    def direction_chart(self,direction_counts: dict):

        fig, ax = plt.subplots(figsize=(8, 5))

        ax.bar(
            direction_counts.keys(),
            direction_counts.values(),
            color="steelblue",
            edgecolor="white"
        )

        ax.set_title(
            "Obstacle Frequency by Sensor Direction"
        )

        ax.set_xlabel(
            "Direction"
        )

        ax.set_ylabel(
            "Number of Events"
        )

        plt.tight_layout()

        plt.show()

    def severity_pie(self,log: list):

        counts = {}

        for e in log:
            counts[e["severity"]] = counts.get(e["severity"],0) + 1
        colors = {

            "High": "tomato",

            "Medium": "orange",

            "Low": "steelblue"
        }

        fig, ax = plt.subplots(
            figsize=(7, 7)
        )

        ax.pie(
            counts.values(),
            labels=counts.keys(),
            autopct="%1.1f%%",
            startangle=140,
            colors=[colors.get(k,"gray") for k in counts.keys()]
        )

        ax.set_title(
            "Obstacle Severity Distribution"
        )

        plt.show()    
    
        