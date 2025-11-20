import pandas as pd

import pandas as pd

def check_csv(csv_path, unique_fields=None, null_fields=None, whitespace_fields=None):
    """
    Perform data quality checks directly on a CSV file.

    Parameters:
    -----------
    csv_path : str
        Full path to the CSV file to validate.

    unique_fields : list of str, optional
        Fields that must contain unique values (no duplicates).

    null_fields : list of str, optional
        Fields that must NOT contain null values.

    whitespace_fields : list of str, optional
        Fields that should NOT contain leading or trailing whitespace.
        If the column is not a string type, a warning is shown.

    Returns:
    --------
    results : dict
        A dictionary containing DataFrames of any issues found.
    """

    print("\n===== DATA QUALITY CHECKS =====\n")
    print(f"Reading CSV: {csv_path}")

    # Load the CSV file
    try:
        df = pd.read_csv(csv_path)
    except Exception as e:
        print(f"❌ ERROR: Could not read CSV file:\n{e}")
        return None

    print(f"Loaded {len(df)} rows.\n")

    results = {
        "duplicate_issues": {},
        "null_issues": {},
        "whitespace_issues": {}
    }

    # ------------------------------------------------------------
    # 1. Duplicate Checks
    # ------------------------------------------------------------
    if unique_fields:
        print("Checking for duplicate values...\n")
        for field in unique_fields:
            if field not in df.columns:
                print(f"⚠️ Field '{field}' not found in CSV.")
                continue

            dupes = df[df.duplicated(subset=[field], keep=False)]

            if not dupes.empty:
                print(f"❌ Duplicate values found in '{field}':")
                print(dupes[[field]].drop_duplicates().to_string(index=False))
                results["duplicate_issues"][field] = dupes
            else:
                print(f"✅ No duplicates in '{field}'")

    else:
        print("No uniqueness checks requested.\n")

    print("\n---------------------------------------\n")

    # ------------------------------------------------------------
    # 2. Null Checks
    # ------------------------------------------------------------
    if null_fields:
        print("Checking for null values...\n")
        for field in null_fields:
            if field not in df.columns:
                print(f"⚠️ Field '{field}' not found in CSV.")
                continue

            null_rows = df[df[field].isna()]

            if not null_rows.empty:
                print(f"❌ Null values found in '{field}': {len(null_rows)} rows")
                results["null_issues"][field] = null_rows
            else:
                print(f"✅ No null values in '{field}'")

    else:
        print("No null-value checks requested.\n")

    print("\n---------------------------------------\n")

    # ------------------------------------------------------------
    # 3. Leading/Trailing Whitespace Checks
    # ------------------------------------------------------------
    if whitespace_fields:
        print("Checking for leading/trailing whitespace...\n")

        for field in whitespace_fields:
            if field not in df.columns:
                print(f"⚠️ Field '{field}' not found in CSV.")
                continue

            # Check dtype
            if df[field].dtype != "object":
                print(f"⚠️ Field '{field}' is not a string. Cannot check whitespace.")
                continue

            # Check whitespace
            mask = df[field].apply(
                lambda x: isinstance(x, str) and (x != x.strip())
            )
            issues = df[mask]

            if not issues.empty:
                print(f"❌ Whitespace found in '{field}': {len(issues)} rows")
                results["whitespace_issues"][field] = issues[["player_id", field]]
            else:
                print(f"✅ No leading/trailing whitespace in '{field}'")

    else:
        print("No whitespace checks requested.\n")

    print("\n===== DATA QUALITY CHECK COMPLETE =====\n")

    return results
