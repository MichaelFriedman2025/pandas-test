import pandas as pd

#level 0
def load_json_into_df():
    df_read = pd.read_json(r"C:\Users\LENOVO\Desktop\pandas_tast\orders_simple.json")
    return df_read


#level 1
def clean_column_total_amount(data):
    data["total_amount"] = data["total_amount"].str.replace("$","")
    return data

def replacing_existing_columns(data,column,type_to):
    if type_to == "float":
        data[column] = data[column].astype(float)
    elif type_to == "int":
        data[column] = pd.to_numeric(data[column])
    elif type_to == "datetime":
        data[column] = pd.to_datetime(data[column])
    return data

def changing_column_types(data):
    data = clean_column_total_amount(data)
    data = replacing_existing_columns(data,"total_amount","float")
    data = replacing_existing_columns(data,"shipping_days","int")
    data = replacing_existing_columns(data,"customer_age","int")
    data = replacing_existing_columns(data,"rating","float")
    data = replacing_existing_columns(data,"order_date","datetime")
    return data

#level 2
def clearing_an_HTML_column(data):
    data['items_html'] = data['items_html'].str.replace("<.*?>",' ',regex=True)
    return data

#level 3
def clearing_an_coupon_used_column(data):
    data["coupon_used"] = data["coupon_used"].str.replace("","no_coupon")
    return data

#level 4
def adding_column_order_month(data):
    data["order_month"] = data["order_date"].dt.month
    return data

#level 5
def adding_column_high_value_order(data):
    avg_total_amount = data["total_amount"].mean()
    data["high_value_order"] = data["total_amount"] > avg_total_amount
    sort_data = data.sort_values("total_amount",ascending=False)
    return sort_data

#level 6
def adding_column_rating(data:pd.DataFrame):
    avg_rating = data.groupby("country")["rating"].mean()
    data["avg_rating_per_country"] = avg_rating[data["country"]].values
    return data

#level 7
def order_filtering(data):
    df = data[(data["total_amount"] > 1000) & (data["rating"] > 4.5)]
    return df

#level 8
def delivery_status(data):
    data["delivery_status"] = data["shipping_days"].apply(lambda x: "delayed" if x > 7 else "on_time")
    return data

#level 9
def save_to_CSV_file(data):
    data.to_csv(r"C:\Users\LENOVO\Desktop\pandas_tast\clean_order_[213289390].csv",index=False)
    return


