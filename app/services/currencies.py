from app.core.config import logger, settings
from app.services.base import BaseService
from scraper.parser import xe_currencies_parser
from utils import get_root_dir, check_staleness


def currency_slug_to_name(slug: str) -> str:
    return slug[4:].replace("-", " ").replace("_", " ").title()


class CurrenciesService(BaseService):
    file_path = get_root_dir().joinpath("storage/app/currencies.json")
    headers_source = "currencies"
    scrape_url = "https://www.xe.com/_next/data/zXvi01CWf5uhNGPHQuwm0/en/currency.json"

    @classmethod
    async def get_list(cls) -> dict[str, str] | None:
        """
        Get list of currencies from local file that is updated regularly
        """
        logger.info("Get list of currencies from local file or download from provider")
        file_data = cls.open_storage_file()

        # file does not exist or is empty
        if file_data is None:
            # call file to save list
            file_data = await cls.retrieve_values_from_provider(parser=xe_currencies_parser)

        # file content may be stale
        if check_staleness(file_data.timestamp, settings.STALE_TIME):
            # call file to save list
            file_data = await cls.retrieve_values_from_provider(parser=xe_currencies_parser)

        if file_data:
            logger.info("Transform data to right schema")
            currency_dict = {currency_slug_to_name(k): v for k, v in file_data.data.items()}
            return currency_dict
