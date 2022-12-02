import pandas as pd


def main():
    """
    goal is to make a new column titled PitchResult
    which is the same as TaggedHitType except replacing
    'undefined' values with the result from PitchCall
    only had to run this function one time
    :return saved the new csv with the added column discussed above:
    """
    df: pd.DataFrame = pd.read_csv("20220423-Olsen-1.csv")

    for i in range(len(df["TaggedHitType"])):
        if df.at[i, "TaggedHitType"] != "Undefined":
            df.at[i, "PitchResult"]: str = df.at[i, "TaggedHitType"]
        else:
            df.at[i, "PitchResult"]: str = df.at[i, "PitchCall"]

    df.to_csv("20220423-Olsen-1.csv")


if __name__ == "__main__":
    main()
