import pandas as pd


def interpret_clusters(df):
    output_tables = []
    summary = []

    grouped = df.groupby("cluster")

    for cluster_id, group in grouped:
        top_diseases = group["Disease"].value_counts().head(3).to_dict()
        avg_age = group["Age"].mean()
        size = len(group)

        recommendation = generate_recommendation(top_diseases)

        summary.append({
            "cluster": int(cluster_id),
            "size": size,
            "avg_age": round(avg_age, 1),
            "top_diseases": top_diseases,
            "recommendation": recommendation
        })

        output_tables.append(group.to_dict(orient="records"))

    return {
        "tables": output_tables,
        "summary": summary
    }


def generate_recommendation(diseases):
    if not diseases:
        return "Insufficient data"

    top = list(diseases.keys())[0].lower()

    if "malaria" in top:
        return "Increase anti-malarial stock and mosquito net distribution by 25%"
    elif "tb" in top or "tuberculosis" in top:
        return "Prioritize TB medication and isolation capacity"
    elif "respiratory" in top:
        return "Increase oxygen supply and pediatric respiratory care"
    else:
        return "Allocate general medical supplies and monitor trend"