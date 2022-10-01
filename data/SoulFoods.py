
import pandas as pd

def main():
    print("hey there")
    # open csv to read
    # open another csv to write
    # iterate over each row, filter pink morsel and combine the quantity and price
    # write each row after combining the fields
    
    df = pd.read_csv("C:\\Users\\Akshay bruh\\Desktop\\quantium-starter\\data\\all_csv_files.csv")
    print(df)

    #remove duplicates
    if len(df[df.duplicated()]):
        df.drop_duplicates(keep='first',inplace=True)
    df = df[df['product'] == "pink morsel"]
    print("----filtered df------")
    print(df)

    df = df.replace("[$]", "", regex=True)

    print("----dollar removed df------")
    print(df)

    df["sales"] = df["price"].astype(float) * df["quantity"].astype(float)
    df2 = df.drop(["quantity", "price"], axis=1)
    print("----final df------")
    print(df2)

    df2.to_csv("C:\\Users\\Akshay bruh\\Desktop\\quantium-starter\\data\\final_csv.csv", encoding='utf-8', index=False)


if __name__ == "__main__":
    main()