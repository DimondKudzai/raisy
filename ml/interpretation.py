import pandas as pd


def interpret_clusters(df):
    output_tables = []
    summary = []

    grouped = df.groupby("cluster")

    for cluster_id, group in grouped:
        top_diseases = group["Disease"].value_counts().head(3).to_dict()
        avg_age = group["Age"].mean()
        size = len(group)

        cluster_name = generate_cluster_name(top_diseases)
        
        summary.append({
        "cluster": int(cluster_id),
        "cluster_name": cluster_name,
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


def generate_cluster_name(diseases):
    if not diseases:
        return "General Patients"

    top = list(diseases.keys())[0].lower()

    if "malaria" in top:
        return "Malaria Hotspot Cluster"
    elif "tb" in top or "tuberculosis" in top:
        return "Tuberculosis High-Risk Cluster"
    elif "respiratory" in top:
        return "Respiratory Care Cluster"
    elif "diabetes" in top:
        return "Chronic Disease Management Cluster"
    else:
        return "General Care Cluster"
        
        
       
        