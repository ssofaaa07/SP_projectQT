import psycopg2
import os

main_command = "sqlacodegen postgresql://cs-main:eid4Uepo@cs-vm-postgre.cs.vsu.ru/project-cs " \
               "--schema SCHEMA --outfile models/SCHEMA.py"


def db_conn(db_name='project-cs', table_name='other'):
    print(f"Подключение к базе данных '{db_name}'. Таблица - '{table_name}'")
    con = psycopg2.connect(dbname=db_name, user='cs-main',
                           password='eid4Uepo', host='cs-vm-postgre.cs.vsu.ru')
    cursor = con.cursor()

    return cursor, con


def update_all_schemas(schemas):
    for schema in schemas:
        print(schema, "autocode started")
        os.system(main_command.replace("SCHEMA", schema))
        print(schema, "autocode done")


def update_schema(schema):
    print(schema, "autocode update started")
    os.system(main_command.replace("SCHEMA", schema))
    print(schema, "autocode update done")


cur, con = db_conn()
cur.execute("SELECT schema_name FROM " + '"information_schema"' + ".schemata")
schemas = [schema[0] for schema in cur.fetchall()]

# update_all_schemas(schemas)
