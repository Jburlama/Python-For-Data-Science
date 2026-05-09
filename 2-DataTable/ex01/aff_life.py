from load_csv import load
"""matplotlib.pyplot it provides a collection of functions that allow you to
create, customize, and
display data visualizations."""
import matplotlib.pyplot as plt


def main():
    df = load("life_expectancy_years.csv")

    for i, country in enumerate(df["country"]):
        if country == "Brazil":
            index = i

    """
    .plot() generate a standard line chart of the data frame numbers
    pandas internaly call matplotlib for it
        """
    ax = df.loc[index][1:].plot()

    print(ax)

    ax.set_title("Brasil Life Expectancy Projections")
    ax.set_xlabel("Years")
    ax.set_ylabel("Life Expectancy")

    plt.show()


if __name__ == "__main__":
    main()
