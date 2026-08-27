import lancedb

from app.config import VECTOR_DB_PATH, TABLE_NAME


class LanceVectorStore:

    def __init__(self):
        print("Connecting to LanceDB")

        self.db = lancedb.connect(VECTOR_DB_PATH)

        print("Connected successfully.")

        self.table = None

    def get_table(self):
        """ Open the table if it exists.
        """
        response = self.db.list_tables()

        print("Existing tables:", response.tables)

        if TABLE_NAME in response.tables:
            self.table = self.db.open_table(TABLE_NAME)
            print(f"Opened table: {TABLE_NAME}")

        else:
            print(f"Table '{TABLE_NAME}' does not exist.")

        return self.table

    def add_data(self, data):
        """
        Create the table if it doesn't exist.
        Otherwise add new records.
        """
        if not data:
            return

        if self.table is None:
            self.get_table()

        if self.table is None:
            print("Creating table...")

            self.table = self.db.create_table(
                TABLE_NAME,
                data=data
            )

        else:
            print(f"Adding {len(data)} new records...")
            self.table.add(data)

    def get_existing_chunk_ids(self):
        """
        Returns all existing chunk_ids.
        Used to avoid duplicate vectors.
        """
        if self.table is None:
            self.get_table()

        if self.table is None:
            return set()

        rows = self.table.search().select(["chunk_id"]).to_list()

        return {row["chunk_id"] for row in rows}

    def search(self, query_vector, k=3):
        """
        Perform vector similarity search.
        """
        if self.table is None:
            self.get_table()

        if self.table is None:
            return []

        results = (
            self.table.search(query_vector)
            .limit(k)
            .to_list()
        )

        return results