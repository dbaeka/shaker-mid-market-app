from utils import invert_dict, get_unix_time


def xe_currencies_parser(body: dict) -> dict | None:
    if body.get('pageProps') and body.get('pageProps').get('codeToSlugMap'):
        data = body.get('pageProps').get('codeToSlugMap')
        # invert keys and values
        data = invert_dict(data)
        data = {"data": data, "timestamp": get_unix_time()}
        return data


def xe_rates_parser(body: dict) -> dict | None:
    if body.get('rates'):
        data = body.get('rates')
        provider_timestamp = body.get('timestamp')
        data = {"data": data, "timestamp": get_unix_time(), "provider_timestamp": provider_timestamp}
        return data
