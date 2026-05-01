import pandas as pd

df_1["temperature"] = pd.to_numeric(df_1["temperature"], errors="coerce")

avg_temp = (
    df_1
    .dropna(subset=["city", "temperature"])
    .groupby("city", as_index=False)["temperature"]
    .mean()
)

x = avg_temp["city"].tolist()
y = avg_temp["temperature"].round(2).tolist()