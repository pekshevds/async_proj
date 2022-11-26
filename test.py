import csv
import time
from db.crud.counteragent import counteragents_bulk_insert_mappings, delete_all_counteragents
from db.models import Counteragent


def get_file_lines():
    with open("data.txt", mode="r", encoding="utf-8-sig") as file:
        lines = list(csv.DictReader(file, delimiter="\t"))
    return lines

def time_wrapper(f):
    def wrapper():
        start = time.time()
        f()
        stop = time.time() - start
        print(f"i made it in {stop:.2f} sec.")
    return wrapper

@time_wrapper
def upload_counteragents():
    new_counteragents = []
    lines = get_file_lines()
    for line in lines:
        counteragent_name = line["Контрагент"]
        value = list(filter(lambda item: item['name'] == counteragent_name, new_counteragents))
        if not value:
            new_counteragents.append({"name": counteragent_name})
    counteragents_bulk_insert_mappings(new_counteragents)

@time_wrapper
def drop_counteragents():
    delete_all_counteragents()


def main():
    upload_counteragents()


if __name__ == "__main__":

    print("deleting conteragents...")
    drop_counteragents()
    print("uploading conteragents...")
    upload_counteragents()
