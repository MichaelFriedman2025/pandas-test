from utils import load_json_into_df,changing_column_types,clearing_an_HTML_column,clearing_an_coupon_used_column,adding_column_order_month,adding_column_high_value_order,adding_column_rating,order_filtering,delivery_status,save_to_CSV_file

def main():
    df = load_json_into_df()
    df = changing_column_types(df)
    df = clearing_an_HTML_column(df)
    df = clearing_an_coupon_used_column(df)
    df = adding_column_order_month(df)
    df = adding_column_high_value_order(df)
    df = adding_column_rating(df)
    df = order_filtering(df)
    df = delivery_status(df)
    save_to_CSV_file(df)

if __name__ == "__main__":
    main()