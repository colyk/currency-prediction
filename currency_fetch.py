from typing import List

import matplotlib.pyplot as plt
import requests
from pandas import DataFrame


def fetch_symbols() -> List[str]:
    url = "https://api.exchangeratesapi.io/latest"
    response = requests.get(url)
    response_json = response.json()
    return sorted(response_json["rates"].keys())


def fetch(
    start_date: str, end_date: str, symbols: List[str], base: str = "USD"
) -> DataFrame:
    params = {
        "start_at": start_date,
        "end_at": end_date,
        "symbols": symbols,
        "base": base,
    }
    url = "https://api.exchangeratesapi.io/history"
    response = requests.get(url, params=params)
    response_json = response.json()
    if "error" in response_json:
        raise ValueError(response_json["error"])

    rates = response_json["rates"]
    return DataFrame(rates, columns=sorted(rates.keys())).T


if __name__ == "__main__":
    print(fetch_symbols())

    df = fetch("2011-11-11", "2019-11-11", ["RUB", "PLN"])
    print(df.describe())
    df.to_csv("currency_data")
    df.plot()
    plt.show()
