from backend.db.database import soldiers

class Repo:
    def __init__(self, table=soldiers):
        self.table = table

    def create_row(self, data: dict):
        """
        create the row and returns it
        data does not includes id
        """
        return self.table.insert(data).select("*").execute().data[0]

    def update_row(self, data: dict, **filter):
        """
        update the row with 'data' and returns it.
        """
        key, val = list(filter.items())[0]
        return self.table.update(data).eq(key, val).select("*").execute().data[0]

    def delete_row(self, **filter):
        """
        delete the row, and returns it
        """
        key, val = list(filter.items())[0]
        soldiersList = self.table.delete().eq(key, val).select("*").execute().data
        if soldiersList:
            return soldiersList[0]
        else:
            return None

    def get_rows(self, **filter):
        "returns all rows in the table"
        query = self.table.select("*")
        for (key, val) in list(filter.items()):
            query = query.eq(key, val)

        return query.execute().data

    def get_one_row(self, **filter):
        """returns a row by id or personal number"""
        key, val = list(filter.items())[0]
        soldiersList = self.table.select("*").eq(key, val).execute().data
        if soldiersList:
            return soldiersList[0]
        else:
            return None


soldiers_repo = Repo(soldiers)

