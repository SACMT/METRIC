#!/usr/bin/env python3
import argparse
import pandas as pd


def csv_to_md(input_file, output_file=None):
    df = pd.read_csv(input_file)
    df = df.fillna("--")
    
    for idx in range(min(5, len(df))):
        row = df.iloc[idx].tolist()
        non_empty = [i for i, x in enumerate(row) if str(x) != '--']
        if non_empty:
            for col_idx in non_empty:
                df.columns.values[col_idx] = str(df.iloc[idx, col_idx])
            df = df.iloc[idx+1:].reset_index(drop=True)
            break
    
    empty_cols = [col for col in df.columns if str(col).startswith('Unnamed') or str(col) == '--']
    df = df.drop(columns=empty_cols, errors='ignore')
    
    df = df.loc[~df.apply(lambda row: all(str(x) == '--' for x in row), axis=1)]
    
    md = df.to_markdown(index=False)
    
    if output_file:
        with open(output_file, 'w') as f:
            f.write(md)
        print(f"Saved to {output_file}")
    else:
        print(md)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Convert CSV to Markdown")
    parser.add_argument("input", help="Input CSV file")
    parser.add_argument("-o", "--output", help="Output Markdown file (optional)")
    args = parser.parse_args()
    
    csv_to_md(args.input, args.output)
