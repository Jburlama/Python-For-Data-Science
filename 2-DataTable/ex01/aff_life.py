from load_csv import load
import matplotlib.pyplot as plt


def main():
    plt.style.use("default")
    df = load("life_expectancy_years.csv")

    for i, country in enumerate(df["country"]):
        if country == "Portugal":
            index = i

    ax = df.loc[index][1:].plot()

    ax.set_title("Portugal Life Expectancy Projections")
    ax.set_xlabel("Years")
    ax.set_ylabel("Life Expectancy")

    plt.show()


if __name__ == "__main__":
    main()
