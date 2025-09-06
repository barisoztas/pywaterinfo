import matplotlib.pyplot as plt

from pywaterinfo import Waterinfo

hic = Waterinfo("hic")

# Get data from start of time series up to next two days
df_ensemble_data = hic.get_ensemble_timeseries_values(
    ts_id=84015010,
    start="2021-01-28",
    end="2021-01-29",
)


fig, ax = plt.subplots(figsize=(10, 4), dpi=300)

for name, group in df_ensemble_data.groupby("ensembledate"):
    _ = ax.plot(
        group["Timestamp"],
        group["0"],
        label=f"Ensemble:{str(name)}",
        linestyle="--",
        alpha=0.5,
    )


df_inconsistent_ensemble_data = hic.get_timeseries_values(
    ts_id=84015010,
    start="2021-01-28",
    end="2021-01-29",
)

ax.plot(
    df_inconsistent_ensemble_data["Timestamp"],
    df_inconsistent_ensemble_data["0"],
    label=(
        "Nonconsistent result returned for a given period"
        "when retrieved with `get_timeseries_values`"
    ),
    color="k",
)

_ = ax.legend(title="Request type")
_ = ax.set_xlabel("Timestamp")
_ = ax.set_ylabel("Value")
_ = ax.set_title("Non-consistent result (black) for 28/01/2021")
_ = ax.grid(True)


plt.show()
