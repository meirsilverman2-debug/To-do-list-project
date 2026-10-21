from backend.db.database import tasks


class TaskDal:
    def __init__(self, table=tasks):
        self.table = table

    def get_rows(self, **filters):
        query = self.table.select("*, soldiers(name, role)")

        for k, v in filters.items():
            query = query.eq(k, v)

        res = query.execute()
        return res.data

    def create(self, data):
        query = self.table.insert(data).select()

        res = query.execute()
        return res.data[0] if res.data else None

    def update(self, id, data):
        query = self.table.update(data).eq("id", id).select()

        res = query.execute()
        return res.data[0] if res.data else None

    def delete(self, id):
        query = self.table.delete().eq("id", id)

        res = query.execute()
        return len(res.data) > 0


tasks_dal = TaskDal()
