import pandas as pd
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline


def preprocess_data(df):
    df = df.copy()

    # Fill missing values
    df.fillna("Unknown", inplace=True)

    # Expected columns: Age, Location, Disease, Visits
    numeric_features = ["Age", "Visits"]
    categorical_features = ["Location", "Disease"]

    numeric_transformer = StandardScaler()
    categorical_transformer = OneHotEncoder(handle_unknown="ignore")

    preprocessor = ColumnTransformer(
        transformers=[
            ("num", numeric_transformer, numeric_features),
            ("cat", categorical_transformer, categorical_features),
        ]
    )

    processed = preprocessor.fit_transform(df)

    return processed