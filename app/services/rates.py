from datetime import datetime

from app.core.config import logger, settings
from app.exceptions.internal import WrongCurrencyCodeException
from app.schemas import ConversionCreate, Conversion
from app.services.base import BaseService
from scraper.parser import xe_rates_parser
from utils import get_root_dir, check_staleness


class RatesService(BaseService):
    file_path = get_root_dir().joinpath("storage/app/rates.json")
    headers_source = "rates"
    scrape_url = "https://www.xe.com/api/protected/midmarket-converter/"

    @classmethod
    async def convert(cls, in_data: ConversionCreate) -> Conversion | None:
        """
        Convert currency amount from one currency to another using the mid-rate
        :return amount of conversion
        """
        logger.info("Get rates from local file or download from provider")

        file_data = cls.open_storage_file()
        # file does not exist or is empty
        if file_data is None:
            # call file to save list
            file_data = await cls.retrieve_values_from_provider(parser=xe_rates_parser)

        # file content may be stale
        if check_staleness(file_data.timestamp, settings.STALE_TIME):
            # call file to save list
            file_data = await cls.retrieve_values_from_provider(parser=xe_rates_parser)

        if file_data:
            rates = file_data.data
            base_rate = rates.get(in_data.from_currency)
            if base_rate is None:
                raise WrongCurrencyCodeException("Invalid from_currency provided")
            dest_rate = rates.get(in_data.to_currency)
            if dest_rate is None:
                raise WrongCurrencyCodeException("Invalid to_currency provided")
            conversion_rate = round(float(dest_rate) / float(base_rate), 5)
            converted_amount = in_data.amount * conversion_rate

            logger.info("Transform data into right schema")

            result = {
                "converted_amount": converted_amount,
                "rate": conversion_rate,
                "metadata": {
                    "time_of_conversion": datetime.now(),
                    "from_currency": in_data.from_currency.upper(),
                    "to_currency": in_data.to_currency.upper()
                }
            }
            return Conversion(**result)
