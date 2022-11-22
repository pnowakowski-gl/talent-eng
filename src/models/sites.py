import requests


class Sites:
    def __init__(self, connection) -> None:
        self.sites_list = []
        self.connection = connection
        try:
            self.response = requests.get(connection)
            self.raise_for_status = self.response.raise_for_status()
            self.status_code = self.response.status_code
        except requests.exceptions.RequestException:
            raise requests.exceptions.HTTPError(f"No connection found")

    def add_to_database(self) -> None:
        '''
        If connection is valid and does not raise for status, add it to database.
        Otherwise raise Exception.
        Returns None.
        '''
        if not self.raise_for_status:
            self.sites_list.append(self.connection)
            print(f"{self.connection} was added to database.")
            return

        raise Exception("No connection found. Site was not added to database.")

    def remove_from_database(self) -> None:
        '''
        If site was found in the database, remove it.
        Otherwise raise Exception.
        Returns None.
        '''
        if self.connection in self.sites_list:
            self.sites_list.remove(self.connection)
            print(f"{self.connection} was removed from database.")
            return
        
        raise Exception("Site was not found in the database.")
