from load_csv import load
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter


# Custom formatter function
def millions_formatter(x, pos):
    """Format the y axis from a numeric value to a string prefixed with M"""
    return f'{x:.0f}M'


def main():
    """loads the file population_total.csv, and displays the country
    information of Portugal versus Brazil"""
    plt.style.use("default")
    df = load("population_total.csv")

    for i, country in enumerate(df["country"]):
        if country == "Portugal":
            pt_index = i
        if country == "Brazil":
            br_index = i

    # Conver the row to numeric values for plot
    pt_population = []
    for p in df.loc[pt_index][1:]:
        pt_population.append(float(p.strip("M")))

    br_population = []
    for p in df.loc[br_index][1:]:
        br_population.append(float(p.strip("M")))

    df.loc[pt_index][1:] = pt_population
    df.loc[br_index][1:] = br_population

    ax = df.loc[pt_index][1:250].plot(label="Portugal")
    ax = df.loc[br_index][1:250].plot(label="Brazil")

    ax.set_title("Population Projections")
    ax.set_xlabel("Year")
    ax.set_ylabel("Population")
    ax.yaxis.set_major_formatter(FuncFormatter(millions_formatter))
    ax.legend(loc="lower right")

    plt.show()


if __name__ == "__main__":
    main()
