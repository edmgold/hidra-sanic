from peewee import ModelSelect
from src.util.args import Args

class Api():

    @staticmethod
    def api_return_pattern(result=None, args=Args, meta=None):
        """
        Create a partner to web api return.

        :param result: The result of any method.
        :param meta: New options to be add inside meta property.
        :param current_page: Current page in the pagination, when there aren't pagination the result will be the zero.
        :param limit: Total number of records per page, when there aren't pagination the result will be the number of records.
        :return:

            {
            "meta": {
                "limit": 0,
                "offset": 0,
                "recordCount": 0
            },
            "records": []
            }

        """

        if isinstance(result, ModelSelect):
            result = [x for x in result]

        if result is None:
            result = []

        records = []
        if isinstance(result, (list, tuple)):
            records = result
        else:
            records.append(result)

        final_result = \
            {
            "meta": {
                "limit": args.limit,
                "offset": args.offset,
                "recordCount": len(records)
            },
            "records": records
            }

        if meta is not None:
            final_result["meta"].update(meta)

        return final_result
