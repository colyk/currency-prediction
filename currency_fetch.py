from typing import List

import matplotlib.pyplot as plt
import pandas as pd
import requests


def fetch(start_date: str, end_date: str, symbols: List[str], base: str = "USD"):
    params = {
        "start_at": start_date,
        "end_at": end_date,
        "symbols": symbols,
        "base": base,
    }
    url = "https://api.exchangeratesapi.io/history"
    response = requests.get(url, params=params)
    response_json = response.json()
    df = pd.DataFrame(response_json["rates"]).T
    df.to_csv('currency_data')
    df.plot()
    plt.show()


if __name__ == "__main__":
    fetch("2018-11-11", "2019-11-11", ["PLN"])
