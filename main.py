from database import execute_query


def tests():
    execute_query(
        """
        CREATE TABLE IF NOT EXISTS employee (
            first_name CHAR(20) NOT NULL,
            last_name CHAR(20),
            age INT,
            sex CHAR(1),
            income FLOAT,
            date TIMESTAMP
        )
        """
    )

    execute_query("TRUNCATE employee")

    for _ in range(2):
        execute_query(
            """
            INSERT INTO employee (
                first_name,
                last_name,
                age,
                sex,
                income
            )
            VALUES (%s, %s, %s, %s, %s)
            """
            % ("'John'", "'Doe'", 20, "'M'", 250)
        )

    employees = execute_query("SELECT * FROM employee")

    for employee in employees:
        print(employee)


def main():
    tests()


if __name__ == "__main__":
    main()
