from load_csv import load
import matplotlib.pyplot as plt


# Custom formatter function
def millions_formatter(x, pos):
    """Format the y axis from a numeric value to a string prefixed with M"""
    return f'{x:.0f}M'


def main():
    """Displays the projection of life expectancy in relation to the
    gross national product of the year 1900 for each country."""
    gdp_df = load("income_per_person_gdppercapita_ppp_inflation_adjusted.csv")
    life_expec_df = load("life_expectancy_years.csv")

    gdp_1900 = gdp_df["1900"][1:]
    life_expec_1900 = life_expec_df["1900"][1:]

    plt.scatter(gdp_1900, life_expec_1900,
                label="Life Expectancy in 1900 Of GDP Per Capita")
    plt.xlabel("Gross Domestic Product")
    plt.ylabel("Life Expectancy")
    plt.title("1900")
    plt.legend()

    plt.show()


if __name__ == "__main__":
    main()
