from pprint import pprint
import os
path = os.path.join(os.getcwd(), 'sorted')
def union_fail (path):
    result = {}
    files = os.listdir(path)
    for quantity_files in range(len(files)):
        counter = 0
        with open(os.path.join(path, files[quantity_files])) as data:
            for string in data:
                data.readline().strip()
                counter += 1
            result[files[quantity_files]] = counter
    sorted_result = {}
    sorted_keys_result = sorted(result, key=result.get)
    for keys in sorted_keys_result:
        sorted_result[keys] = result[keys]

    with open(os.path.join(os.getcwd(), 'unionfile.txt'), 'w') as log:
        for dict_number in range(len(sorted_result)):
            log.write(list(sorted_result.keys())[dict_number])
            log.write('\n')
            log.write(str(list(sorted_result.values())[dict_number]))
            log.write('\n')
            for count in range(list(sorted_result.values())[dict_number]):
                log.write(f'Строка номер {count + 1} файла номер {str(list(sorted_result.keys())[dict_number])}')
                log.write('\n')

print((union_fail(path)))




