import requests
from dataclasses import dataclass


@dataclass
class CryptoPrijs:
    naam: str
    prijs_eur: float

    def toon(self):
        print(f"{self.naam}: €{self.prijs_eur:.2f}")


class ApiClient:
    URL = "https://api.coingecko.com/api/v3/simple/price"

    def fetch_price(self, coin="bitcoin"):
        params = {
            "ids": coin,
            "vs_currencies": "eur"
        }

        response = requests.get(
            self.URL,
            params=params,
            timeout=5
        )

        response.raise_for_status()
        return response.json()


def parse_crypto(data, coin="bitcoin"):
    prijs = data[coin]["eur"]
    return CryptoPrijs(
        coin.capitalize(),
        prijs
    )


def main():
    client = ApiClient()

    try:
        data = client.fetch_price("bitcoin")
        crypto = parse_crypto(data)

        crypto.toon()

    except requests.exceptions.Timeout:
        print(" Timeout: API reageert niet.")

    except requests.exceptions.ConnectionError:
        print(" Geen internetverbinding.")

    except requests.exceptions.HTTPError:
        print(" Serverfout bij API.")

    except KeyError:
        print(" Onverwacht antwoord van API.")

    except Exception as e:
        print(" Onbekende fout:", e)


if __name__ == "__main__":
    main()