import datetime

from db.common import execute_query, execute_transaction
from utils.datatype import convert_tuple_to_dict


def __get_rental_duration_operation(id):
    def invoke_cursor_func(cursor):
        sql = "select id, type, time_gap, array_size, description from rental_duration_operation t where t.id = %s"
        cursor.execute(sql, (id,))
        return convert_tuple_to_dict(
            cursor.fetchone(),
            [
                "id",
                "type",
                "time_gap",
                "array_size",
                "description",
            ],
        )

    return execute_query(invoke_cursor_func)


def __get_quote_scraping_task(id):
    def invoke_cursor_func(cursor):
        sql = "select id, created_at, created_by, rental_duration_operation_id from quote_scraping_task t where t.id = %s"
        quote_scraping_task = convert_tuple_to_dict(
            cursor.fetchone(sql, (id,)),
            [
                "id",
                "created_at",
                "created_by",
                "rental_duration_operation_id",
            ],
        )
        rental_duration_operation_id = quote_scraping_task.pop(
            "rental_duration_operation_id", None
        )
        if rental_duration_operation_id is not None:
            quote_scraping_task[
                "rental_duration_operation"
            ] = __get_rental_duration_operation(rental_duration_operation_id)

        return quote_scraping_task

    return execute_query(invoke_cursor_func)


def __get_rental_route(id):
    def invoke_cursor_func(cursor):
        sql = """SELECT
                    t1.pick_up_location_id,
                    t1.drop_off_location_id,
                    t2.name pick_up_location_name,
                    t3.name drop_off_location_name
                FROM
                    rental_route t1,
                    location t2,
                    location t3
                WHERE
                    t1.pick_up_location_id = t2.id
                        AND t1.drop_off_location_id = t3.id and t1.id = %s """
        return convert_tuple_to_dict(
            cursor.fetchone(sql, (id,)),
            [
                "pick_up_location_id",
                "drop_off_location_id",
                "pick_up_location_name",
                "drop_off_location_name",
            ],
        )

    return execute_query(invoke_cursor_func)


def __get_rental_duration(id):
    def invoke_cursor_func(cursor):
        sql = "select id, pick_up_datetime, drop_off_datetime from rental_duration t where t.id = %s"
        return convert_tuple_to_dict(
            cursor.fetchone(sql, (id,)),
            ["id", "pick_up_datetime", "drop_off_datetime"],
        )

    return execute_query(invoke_cursor_func)


def __get_booking_request_templates(quote_scraping_task_id):
    def invoke_cursor_func(cursor):
        quote_scraping_task = __get_quote_scraping_task(quote_scraping_task_id)
        sql = "select id, rental_route_id, rental_duration_id from booking_request_template t where t.quote_scraping_task_id = %s"
        cursor.execute(sql, (quote_scraping_task_id,))
        booking_request_templates = []
        for (
            id,
            rental_route_id,
            rental_duration_id,
        ) in cursor:
            booking_request_templates.append(
                {
                    "id": id,
                    "rental_route": __get_rental_route(rental_route_id),
                    "rental_duration": __get_rental_duration(rental_duration_id),
                    "quote_scraping_task": quote_scraping_task,
                }
            )

        return booking_request_templates

    return execute_query(invoke_cursor_func)


def get_rental_duration_operations():
    def invoke_cursor_func(cursor):
        sql = "select id, type, time_gap, array_size, description from rental_duration_operation"
        cursor.execute(sql)

        rental_duration_operations = []
        for rental_duration_operation in cursor:
            rental_duration_operations.append(
                convert_tuple_to_dict(
                    rental_duration_operation,
                    [
                        "id",
                        "type",
                        "time_gap",
                        "array_size",
                        "description",
                    ],
                )
            )

        return rental_duration_operations

    return execute_query(invoke_cursor_func)


def create_quote_scraping_task(
    created_by, rental_duraion_operation_id, booking_request_template_configs
):
    def execute_step_1(cursor):
        """Create the quote scraping task"""
        sql = "insert into quote_scraping_task(created_at, created_by, rental_duration_operation_id) values(%s, %s, %s)"
        cursor.execute(
            sql,
            (
                datetime.datetime.now(),
                created_by,
                rental_duraion_operation_id,
            ),
        )
        return cursor.lastrowid

    def execute_step_2(cursor, quote_scraping_task_id):
        """Create the booking request templates"""
        rental_duration_operation = __get_rental_duration_operation(
            rental_duraion_operation_id
        )
        sql = "insert into booking_request_template(rental_route_id, rental_duration_id, quote_scraping_task_id) values(%s, %s, %s)"
        for booking_request_template_config in booking_request_template_configs:
            params = booking_request_template_config + (quote_scraping_task_id,)
            cursor.execute(sql, params)
            booking_request_template_id = cursor.lastrowid
            __create_booking_requests_based_on_template(
                cursor, booking_request_template_id, rental_duration_operation
            )

    def __create_booking_requests_based_on_template(
        cursor, booking_request_template_id, rental_duration_operation
    ):
        array_size = rental_duration_operation["array_size"]
        index_in_array = 0
        booking_requests = []
        while index_in_array < array_size:
            booking_requests.append(
                (
                    booking_request_template_id,
                    index_in_array,
                )
            )
            index_in_array += 1

        sql = "insert into booking_request(booking_request_template_id, index_in_array) values(%s, %s)"
        cursor.executemany(sql, booking_requests)

    def invoke_cursor_func(cursor):
        quote_scraping_task_id = execute_step_1(cursor)
        execute_step_2(cursor, quote_scraping_task_id)
        return quote_scraping_task_id

    return execute_transaction(invoke_cursor_func)


def get_booking_requests(quote_scraping_task_id):
    def invoke_cursor_func(cursor):
        pass


def save_rental_categroy(rental_category):
    pass


def save_rental_quote(rental_quote):
    pass