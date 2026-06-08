import matplotlib.pyplot as plt


class Visualizer:

    def direction_chart(
        self,
        direction_counts: dict
    ):

        fig, ax = plt.subplots(
            figsize=(8, 5)
        )

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