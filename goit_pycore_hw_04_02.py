class DuplicateError(Exception):
    pass

def get_cats_info(path):
    try:
        with open(path, "r", encoding="utf-8") as file:
            cats = []
            while True:
                cat = {}
                line = file.readline()
                if not line:
                    break
                cat["id"], cat["name"], cat["age"] = line.strip().split(',')
                if not any(c["id"] == cat["id"] for c in cats):
                    cats.append(cat)
                else:
                    raise DuplicateError
            return cats
    except FileNotFoundError:
        print("Файл не знайдено за вказаним шляхом.")
        raise FileNotFoundError
    except ValueError:
        print("Файл пошкоджений або не слідує очікуваному формату.")
        raise ValueError
    except DuplicateError:
        print("Файл містить неунікальні ідентифікатори.")
        raise DuplicateError

def main():
    try:
        cats_info = get_cats_info("./cats_file.txt")
        expected_result = [
            {"id": "60b90c1c13067a15887e1ae1", "name": "Tayson", "age": "3"},
            {"id": "60b90c2413067a15887e1ae2", "name": "Vika", "age": "1"},
            {"id": "60b90c2e13067a15887e1ae3", "name": "Barsik", "age": "2"},
            {"id": "60b90c3b13067a15887e1ae4", "name": "Simon", "age": "12"},
            {"id": "60b90c4613067a15887e1ae5", "name": "Tessi", "age": "5"},
        ]
        print("Результат правильний." if sorted(cats_info, key=lambda d: d['id']) == sorted(expected_result, key=lambda d: d['id']) else "Результат невірний.")
    except (FileNotFoundError, ValueError, DuplicateError) as error:
        pass

if __name__ == '__main__':
    main()