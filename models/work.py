class Work:
    def __init__(self, client, date_in, data_out, client_name, vehicle, diagnosis, repair, spare_part_cost, repair_cost, total_price, payment_method, done):
        self._client = client
        self._date_in = date_in
        self._date_out = data_out
        self._client_name = client_name
        self._vehicle = vehicle
        self._diagnosis = diagnosis
        self._repair = repair
        self._spare_part_cost = spare_part_cost
        self._repair_cost = repair_cost
        self._total_price = total_price
        self._payment_method = payment_method
        self._done = done
        