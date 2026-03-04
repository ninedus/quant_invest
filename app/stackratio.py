import pandas as pd
import logging
import plotly.graph_objects as go
from datetime import datetime

# Configure logging
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)


def get_data():
    try:
        logger.info("Loading ETL SAA data for stacking ratio analysis")

        # Read the CSV file
        df = pd.read_csv(
            "data/ETL_SAA_agre_stack_util_perf_202603031332.csv",
            sep=",",
            engine="c",
            encoding="utf-8-sig",
        )

        logger.info(f"Loaded {df.shape[0]} rows from CSV")

        # Convert stack_date to datetime
        df["stack_date"] = pd.to_datetime(df["stack_date"], format="%Y%m%d")

        # Convert numeric columns
        numeric_cols = [
            "stack_hour",
            "capa_tier_avail",
            "van_f_20",
            "van_f_40",
            "van_m_20",
            "van_m_40",
        ]

        for col in numeric_cols:
            df[col] = pd.to_numeric(df[col], errors="coerce")

        # Calculate used capacity
        # Used Capacity = van_f_20 + van_f_40*2 + van_m_20 + van_m_40*2
        df["used_capacity"] = (
            df["van_f_20"] + df["van_f_40"] * 2 + df["van_m_20"] + df["van_m_40"] * 2
        )

        # Calculate stacking ratio (used / total)
        df["stacking_ratio"] = df["used_capacity"] / df["capa_tier_avail"]

        logger.info(f"Calculated stacking ratios for {df.shape[0]} records")

        # Group by date and extract OHLC values
        ohlc_data = []

        for date, group in df.groupby("stack_date"):

            # Sort by hour to ensure chronological order
            group = group.sort_values("stack_hour")

            if len(group) > 0:
                ratios = group["stacking_ratio"].values

                open_ratio = ratios[0]  # First hour
                high_ratio = ratios.max()  # Highest ratio
                low_ratio = ratios.min()  # Lowest ratio
                close_ratio = ratios[-1]  # Last hour

                ohlc_data.append(
                    {
                        "date": date,
                        "open": open_ratio,
                        "high": high_ratio,
                        "low": low_ratio,
                        "close": close_ratio,
                        "num_hours": len(group),
                        "avg_ratio": ratios.mean(),
                        "std_ratio": ratios.std(),
                    }
                )

        # Create OHLC DataFrame
        ohlc_df = pd.DataFrame(ohlc_data)

        # Sort by date
        ohlc_df = ohlc_df.sort_values("date").reset_index(drop=True)

        logger.info(f"Generated OHLC data for {len(ohlc_df)} days")

        # Export to CSV file
        output_filename = "output/Daily_Stacking_Ratio_OHLC.csv"

        ohlc_df.to_csv(output_filename, index=False, encoding="utf-8-sig")

        logger.info(f"Successfully exported data to {output_filename}!")
        logger.info(f"File location: {output_filename}")
        logger.info(f"Total rows exported: {len(ohlc_df)}")
        logger.info(f"Date range: {ohlc_df['date'].min()} to {ohlc_df['date'].max()}")

        return ohlc_df

    except FileNotFoundError as e:
        logger.error(f"File not found: {str(e)}")
        raise

    except Exception as e:
        logger.error(f"Error processing and exporting data: {str(e)}")
        raise


# Load OHLC data
df = get_data()

# Convert date column
df["date"] = pd.to_datetime(df["date"])

# Create candlestick chart
fig = go.Figure(
    data=[
        go.Candlestick(
            x=df["date"],
            open=df["open"],
            high=df["high"],
            low=df["low"],
            close=df["close"],
            increasing_line_color="green",
            decreasing_line_color="red",
        )
    ]
)

# Layout settings
fig.update_layout(
    title="Daily Yard Stacking Ratio (SAA)",
    xaxis_title="Date",
    yaxis_title="Stacking Ratio",
    xaxis_rangeslider_visible=False,
    template="plotly_dark",
)

# Show chart
fig.show()
