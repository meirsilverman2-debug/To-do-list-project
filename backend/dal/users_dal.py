from backend.db.database import soldiers


class Repo:
    def __init__(self, table=soldiers):
        self.table = table

    def create_row(self, data: dict):
        """
        create the row and returns it
        data does not includes id
        """
        data = self.table.insert(data).select("*").execute().data
        return data[0] if data else None

    def update_row(self, data: dict, **filter):
        """
        update the row with 'data' and returns it.
        """
        key, val = list(filter.items())[0]
        data = self.table.update(data).eq(key, val).select("*").execute().data
        return data[0] if data else None

    def delete_row(self, **filter):
        """
        delete the row, and returns it
        """
        key, val = list(filter.items())[0]
        data = self.table.delete().eq(key, val).select("*").execute().data
        return data[0] if data else None

    def get_rows(self, **filter):
        "returns all rows in the table"
        query = self.table.select("*")
        for (key, val) in list(filter.items()):
            query = query.eq(key, val)

        return query.execute().data

    def get_one_row(self, **filter):
        """returns a row by id or personal number"""
        key, val = list(filter.items())[0]
        data = self.table.select("*").eq(key, val).execute().data
        return data[0] if data else None


soldiers_repo = Repo(soldiers)

