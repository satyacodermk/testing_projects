import pandas as pd

def load_dataset(filepath: str) -> pd.DataFrame:
    """Load CSV dataset into a Pandas DataFrame."""
    return pd.read_csv(filepath)

def get_basic_info(df: pd.DataFrame) -> str:
    """Return basic dataset info: shape, columns, dtypes."""
    info_str = f"Shape: {df.shape}\n"
    info_str += f"Columns: {list(df.columns)}\n"
    info_str += f"Data Types:\n{df.dtypes}\n"
    return info_str

def get_summary_stats(df: pd.DataFrame) -> pd.DataFrame:
    """Return summary statistics for numeric columns."""
    return df.describe()

def get_missing_values(df: pd.DataFrame) -> pd.Series:
    """Return count of missing values per column."""
    return df.isnull().sum()

def get_unique_values(df: pd.DataFrame) -> dict:
    """Return unique value counts for each column."""
    return {col: df[col].nunique() for col in df.columns}

def get_department_salary_stats(df: pd.DataFrame) -> pd.DataFrame:
    """Return average salary per department."""
    return df.groupby("Department")["Salary"].mean().reset_index(name="Average Salary")
