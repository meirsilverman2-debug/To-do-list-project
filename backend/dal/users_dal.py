from backend.db.database import soldiers

class Repo:
    def __init__(self, table):
        self.table = table

    def createRow(self, data: dict):
        """
        create the row and returns it
        data does not includes id
        """
        return self.table.insert(data).select("*").execute().data[0]

    def updateRow(self, data: dict, **filter):
        """
        update the row with 'data' and returns it.
        """
        key, val = list(filter.items())[0]
        return self.table.update(data).eq(key, val).select("*").execute().data[0]

    def deleteRow(self, **filter):
        """
        delete the row, and returns it
        """
        key, val = list(filter.items())[0]
        soldiersList = self.table.delete().eq(key, val).select("*").execute().data
        if soldiersList:
            return soldiersList[0]
        else:
            return None

    def getRows(self, **filter):
        "returns all rows in the table"
        query = self.table.select("*")
        for (key, val) in list(filter.items()):
            query = query.eq(key, val)

        return query.execute().data

    def getOneRow(self, **filter):
        """returns a row by id or personal number"""
        key, val = list(filter.items())[0]
        soldiersList = self.table.select("*").eq(key, val).execute().data
        if soldiersList:
            return soldiersList[0]
        else:
            return None


usersRepo = Repo(soldiers)

if __name__ == "__main__":
    # newSoldier = usersRepo.createRow({"personal_number": "87654325", "name": "moishy"})
    # updatedSoldier = usersRepo.updateRow({"name": "mordechai"}, personal_number="87654324")
    # soldiers = usersRepo.getRows()
    # soldier = usersRepo.getRowById(personal_number="87654324")
    # deletedSoldier = usersRepo.deleteRow(personal_number="87654324")
    # undefined = usersRepo.getRowById(personal_number="87654324")
    # print({"newSoldier": newSoldier})
    # print({"updatedSoldier": updatedSoldier})
    # print({"soldiers": soldiers})
    # print({"soldier": soldier})
    # print({"deletedSoldier": deletedSoldier})
    # print({"undefined": undefined})