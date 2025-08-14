from utils import (
    load_dataset,
    get_basic_info,
    get_summary_stats,
    get_missing_values,
    get_unique_values,
    get_department_salary_stats
)

def main():
    # Load the dataset
    df = load_dataset("dataset.csv")

    print("=== BASIC INFO ===")
    print(get_basic_info(df))

    print("\n=== SUMMARY STATISTICS ===")
    print(get_summary_stats(df))

    print("\n=== MISSING VALUES ===")
    print(get_missing_values(df))

    print("\n=== UNIQUE VALUES ===")
    for col, unique_count in get_unique_values(df).items():
        print(f"{col}: {unique_count} unique values")

    print("\n=== AVERAGE SALARY PER DEPARTMENT *Satyam changed ...* ===")
    print(get_department_salary_stats(df))

if __name__ == "__main__":
    main()

