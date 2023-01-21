import json
from typing import Callable

from app.core.config import logger
from app.schemas.internal import StoredData
from scraper import collectors
from scraper.headers import get_xe_headers
from utils import get_root_dir


class BaseService:
    file_path = get_root_dir()
    scrape_url = ""
    headers_source = ""

    @classmethod
    def open_storage_file(cls) -> StoredData | None:
        """Open Storage File

        :return data
        """
        logger.info("Loading File With Scraped Data")
        data = None
        try:
            if cls.file_path.exists():
                with open(cls.file_path, "r") as f:
                    data = json.load(f)
                    if data:
                        return StoredData(**data)
        except Exception as e:
            logger.error("Error encountered during file opening: " + str(e))

    @classmethod
    async def retrieve_values_from_provider(cls, parser: Callable) -> StoredData | None:
        logger.info("Retrieving data from provider")
        try:
            response = collectors.get_data(cls.scrape_url, headers=get_xe_headers(source=cls.headers_source))
            if response is not None:
                parsed_data = parser(response)
                if parsed_data:
                    await cls.save_values_to_file(parsed_data)
                return StoredData(**parsed_data)
        except Exception as e:
            logger.error("Error encountered retrieving data from provider: " + str(e))
        return None

    @classmethod
    async def save_values_to_file(cls, data: dict) -> None:
        logger.info("Saving scraped data to file")
        json_object = json.dumps(data, indent=4)
        with open(cls.file_path, "w") as f:
            f.write(json_object)
