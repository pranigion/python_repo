import threading
from concurrent.futures import ThreadPoolExecutor


def transformation(input:list):
    src = input['source']
    dest = input['destination']
    print(f"Reading data from {src}")
    print(f"Transforming data from {src}")
    print(f"Writing data to {dest}")

    return f"Copy{src} to {dest} is done"

array_inp=[{"source":"source1","destination":"destination1"},
        {"source":"source2","destination":"destination2"},
        {"source":"source3","destination":"destination3"},
        {"source":"source4","destination":"destination4"}]

with ThreadPoolExecutor(max_workers=3) as executor:
    result = executor.map(transformation,array_inp)

print(F"Processed sucessfully are {list(result)}")





