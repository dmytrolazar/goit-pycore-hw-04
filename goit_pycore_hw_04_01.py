def total_salary(path):
    try:
        with open(path, "r", encoding="utf-8") as file:
            total = 0
            count = 0
            while True:
                line = file.readline()
                if not line:
                    break
                _, salary = line.strip().split(',')
                total += float(salary)
                count += 1
            return [total, total/count]
    except FileNotFoundError:
        print("Файл не знайдено за вказаним шляхом.")
        raise FileNotFoundError
    except ValueError:
        print("Файл пошкоджений або не слідує очікуваному формату.")
        raise ValueError

def main():
    try:
        total, average = total_salary("./salary_file.txt")
        print(f"Загальна сума заробітної плати: {total:0.2f}, Середня заробітна плата: {average:0.2f}")
    except (FileNotFoundError, ValueError) as error:
        pass

if __name__ == '__main__':
    main()