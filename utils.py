import pandas as pd

#level 0
def load_json_into_df() -> pd.DataFrame:
    df_read = pd.read_json(r"C:\Users\LENOVO\Desktop\pandas_tast\orders_simple.json")
    return df_read

#level 1
def clean_column_total_amount(data:pd.DataFrame) -> pd.DataFrame:
    data["total_amount"] = data["total_amount"].str.replace("$","")
    return data

def changing_column_types(data:pd.DataFrame) -> pd.DataFrame:
    data = clean_column_total_amount(data)
    # type change to float
    data["total_amount"] = data["total_amount"].astype(float)
    data["rating"] = data["rating"].astype(float)
    # type change to int
    data["shipping_days"] = pd.to_numeric(data["shipping_days"])
    data["customer_age"] = pd.to_numeric(data["customer_age"])
    # type change to datetime
    data["order_date"] = pd.to_datetime(data["order_date"])
    return data

#level 2
def clearing_an_HTML_column(data:pd.DataFrame) -> pd.DataFrame: 
    data['items_html'] = data['items_html'].str.replace("<.*?>",' ',regex=True)
    return data

#level 3
def clearing_an_coupon_used_column(data:pd.DataFrame) -> pd.DataFrame:
    data["coupon_used"] = data["coupon_used"].str.replace("","no_coupon")
    return data

#level 4
def adding_column_order_month(data:pd.DataFrame) -> pd.DataFrame:
    data["order_month"] = data["order_date"].dt.month
    return data

#level 5
def adding_column_high_value_order(data:pd.DataFrame) -> pd.DataFrame:
    avg_total_amount = data["total_amount"].mean()
    data["high_value_order"] = data["total_amount"] > avg_total_amount
    sort_data = data.sort_values("total_amount",ascending=False)
    return sort_data

#level 6
def adding_column_rating(data:pd.DataFrame) -> pd.DataFrame:
    avg_rating = data.groupby("country")["rating"].mean()
    data["avg_rating_per_country"] = avg_rating[data["country"]].values
    return data

#level 7
def order_filtering(data:pd.DataFrame) -> pd.DataFrame:
    data = data[(data["total_amount"] > 1000) & (data["rating"] > 4.5)]
    return data

#level 8
def delivery_status(data:pd.DataFrame) -> pd.DataFrame:
    data["delivery_status"] = data["shipping_days"].apply(lambda x: "delayed" if x > 7 else "on_time")
    return data

#level 9
def save_to_CSV_file(data:pd.DataFrame) -> None:
    data.to_csv(r"C:\Users\LENOVO\Desktop\pandas_tast\clean_order_[213289390].csv",index=False)
    return