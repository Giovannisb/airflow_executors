import yfinance as yf


def get_stock(ticker, start_date, end_date):
    path = f"./datalake/acoes/{ticker}.csv"
    hist = yf.Ticker(ticker).history(
        period="1d",
        interval="1h",
        start=start_date,
        end=end_date,
        prepost=True
    ).to_csv(path)

get_stock("GOOG", "2023-02-01", "2023-02-05")
get_stock("APPL", "2023-02-01", "2023-02-05")   