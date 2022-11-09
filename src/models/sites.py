import requests


class Sites:
    def __init__(self, connection) -> None:
        self.sites_list = []
        self.connection = connection
        try:
            self.status_code = requests.get(self.connection).status_code
        except (requests.exceptions.InvalidSchema, requests.exceptions.MissingSchema):
            self.status_code = 400

    def add_to_database(self):
        if 200 <= self.status_code <= 299:
            self.sites_list.append(self.connection)
            print(f"{self.connection} was added to database.")
            return True
        else:
            print(f"Status code is {self.status_code}. Site was not added to database.")
            return False

    def remove_from_database(self):
        if self.connection in self.sites_list:
            self.sites_list.remove(self.connection)
            print(f"{self.connection} was removed from database.")
            return True
        else:
            print(f"{self.connection} does not exist in database.")
            return False
